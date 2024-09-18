from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Define common headers and API URL
BASE_URL = 'https://api.alteg.io/api/v1'
PARTNER_TOKEN = os.environ.get('PARTNER_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {PARTNER_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.api.v2+json'
}

def authenticate(creds):
    """Authenticate and retrieve a user token."""
    url = f'{BASE_URL}/auth'
    print(url, HEADERS, creds)
    try:
        response = requests.post(url, headers=HEADERS, json=creds)
        response_data = response.json()
        if response.status_code in [200, 201] and response_data['success']:
            user_token = response_data['data'].get('user_token')
            print(f'User Token: {user_token}')
            return user_token
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error during authentication: {e}')
        return None


def get_clients_list(company_id, user_token):
    """Fetch the list of clients for a given company."""
    url = f'{BASE_URL}/company/{company_id}/clients/search'
    headers = {
            'Accept' : 'application/vnd.api.v2+json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {PARTNER_TOKEN}, User {user_token}'
        }

    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print('Clients List:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error fetching clients: {e}')
        return None


def add_client(company_id, first_name, phone_number, user_token, surname = None, patronymic=None, email=None, sex_id=None, importance_id=None, discount=None, card=None, birth_date=None, comment=None, spent=None, balance=None, sms_check=None, sms_not=None, categories=None, custom_fields=None):
    """Add a new client with all possible parameters to the company."""
    url = f'{BASE_URL}/clients/{company_id}'
    
    headers = {
            'Accept' : 'application/vnd.api.v2+json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {PARTNER_TOKEN}, User {user_token}'
    }
    
    # Define the body with optional parameters
    body = {
        "name": first_name,
        "phone": phone_number,
    }

    # Optional parameters
    if surname: body["surname"] = surname
    if patronymic: body["patronymic"] = patronymic
    if email: body["email"] = email
    if sex_id: body["sex_id"] = sex_id
    if importance_id: body["importance_id"] = importance_id
    if discount: body["discount"] = discount
    if card: body["card"] = card
    if birth_date: body["birth_date"] = birth_date
    if comment: body["comment"] = comment
    if spent: body["spent"] = spent
    if balance: body["balance"] = balance
    if sms_check is not None: body["sms_check"] = sms_check
    if sms_not is not None: body["sms_not"] = sms_not
    if categories: body["categories"] = categories
    if custom_fields: body["custom_fields"] = custom_fields

    # Make the POST request
    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 201:
            print('Client added:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error adding client: {e}')
        return None

def get_schedule(company_id, user_token):
    """Fetch the booking schedule for a given company."""
    url = f'{BASE_URL}/book_dates/{company_id}'
    
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Authorization': f'Bearer {PARTNER_TOKEN}',
        'User': user_token
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('Schedule:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error fetching schedule: {e}')
        return None

def get_timetable_seances(company_id, staff_id, date, user_token):
    """Fetch the timetable seances for a specific company, staff member, and date."""
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Authorization': f'Bearer {PARTNER_TOKEN}',
        'User': user_token
    }

    url = f'https://api.alteg.io/api/v1/timetable/seances/{company_id}/{staff_id}/{date}'
    print(url)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('Timetable Seances:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error fetching timetable seances: {e}')
        return None

def get_companies(user_token):
    """Fetch the list of companies."""
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Authorization': f'Bearer {PARTNER_TOKEN}',
        'User': user_token
    }
    
    url = 'https://api.alteg.io/api/v1/companies'
    print(url)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('Companies:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error fetching companies: {e}')
        return None

def get_services(company_id, user_token):
    """Fetch the list of services for a specific company."""
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Authorization': f'Bearer {PARTNER_TOKEN}',
        'User': user_token
    }
    
    url = f'https://api.alteg.io/api/v1/company/{company_id}/services'
    print(url)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print('Service Details:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error fetching services: {e}')
        return None

def create_new_entry(company_id, staff_id, services, client, save_if_busy, datetime, seance_length=None, send_sms=False, comment=None, sms_remain_hours=0, email_remain_hours=0, attendance=0, api_id=None, custom_color=None, record_labels=None, custom_fields=None, user_token=None):
    """Create a new entry for a group event or client."""
    url = f'{BASE_URL}/records/{company_id}'
    
    headers = {
            'Accept' : 'application/vnd.api.v2+json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {PARTNER_TOKEN}, User {user_token}'
    }

    # Create the request body
    body = {
        "staff_id": staff_id,
        "services": services,
        "client": client,
        "save_if_busy": save_if_busy,
        "datetime": datetime,
        "send_sms": send_sms,
        "sms_remain_hours": sms_remain_hours,
        "email_remain_hours": email_remain_hours,
        "attendance": attendance,
    }

    # Optional parameters
    if seance_length: body["seance_length"] = seance_length
    if comment: body["comment"] = comment
    if api_id: body["api_id"] = api_id
    if custom_color: body["custom_color"] = custom_color
    if record_labels: body["record_labels"] = record_labels
    if custom_fields: body["custom_fields"] = custom_fields

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 201:
            print('New Entry Created:', response.json())
            return response.json()
        else:
            print(f'Error: {response.status_code}, {response.text}')
    except requests.RequestException as e:
        print(f'Error creating new entry: {e}')
        return None

### "GET SLOTS" BLOCK START
import requests
from datetime import datetime, timedelta

def filter_and_merge_available_slots(timetable_data, duration_minutes):
    """Фильтруем и объединяем доступные временные слоты с добавлением 5 минут к окончанию интервала."""
    current_slot_start = None
    current_slot_end = None
    merged_slots = []

    for entry in timetable_data:
        if entry['is_free']:
            if current_slot_start is None:
                current_slot_start = entry['time']
            current_slot_end = entry['time']
        else:
            if current_slot_start and current_slot_end:
                slot_start_time = datetime.strptime(current_slot_start, "%H:%M")
                slot_end_time = datetime.strptime(current_slot_end, "%H:%M") + timedelta(minutes=5)
                
                # Проверяем, хватает ли длительности интервала для процедуры
                slot_duration = slot_end_time - slot_start_time
                if slot_duration >= timedelta(minutes=duration_minutes):
                    merged_slots.append(f"{current_slot_start} - {slot_end_time.strftime('%H:%M')}")
                
                current_slot_start = None
                current_slot_end = None

    # Добавляем последний интервал, если остался незавершённый интервал
    if current_slot_start and current_slot_end:
        slot_start_time = datetime.strptime(current_slot_start, "%H:%M")
        slot_end_time = datetime.strptime(current_slot_end, "%H:%M") + timedelta(minutes=5) 
        slot_duration = slot_end_time - slot_start_time
        
        if slot_duration >= timedelta(minutes=duration_minutes):
            merged_slots.append(f"{current_slot_start} - {slot_end_time.strftime('%H:%M')}")

    return merged_slots

# Получение сотрудников и продолжительности услуги
def get_services_staff_and_duration(company_id, service_id, user_token):
    """Получаем сотрудников и продолжительность конкретного сервиса."""
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Authorization': f'Bearer {PARTNER_TOKEN}, User {user_token}'
    }
    
    url = f'https://api.alteg.io/api/v1/company/{company_id}/services'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        services = response.json().get('data', [])
        
        for service in services:
            if service['id'] == service_id:
                duration = service['duration']
                if duration == 0:
                    duration = 1200
                duration_minutes = duration // 60  # Конвертируем секунды в минуты
                staff = [{'id': staff['id'], 'name': staff['name']} for staff in service.get('staff', [])]
                return staff, duration_minutes
        
        return [], 0
    else:
        print(f'Error fetching services: {response.status_code}, {response.text}')
        return [], 0
    

def get_timetable_seances(company_id, staff_id, date, user_token):
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {PARTNER_TOKEN}, User {user_token}'
    }
    
    url = f'https://api.alteg.io/api/v1/timetable/seances/{company_id}/{staff_id}/{date}'

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check the response status and handle the data
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return None

# Основная функция для поиска доступных слотов с использованием timetable seances
def find_available_dates_with_seances(company_id, service_id, start_date, user_token):
    """Находим ближайшие свободные даты для записи по каждому сотруднику с учетом сеансов расписания."""
    staff_list, duration_minutes = get_services_staff_and_duration(company_id, service_id, user_token)

    if not staff_list:
        print("Сотрудники не найдены для указанного сервиса.")
        return None

    available_slots_per_staff = {}

    # Начальная дата поиска
    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")

    for staff in staff_list:
        staff_id = staff['id']
        staff_name = staff['name']
        available_slots_per_staff[staff_name] = []

        for day_offset in range(3):  # Ищем на ближайшие N дней
            search_date = (start_date_dt + timedelta(days=day_offset)).strftime("%Y-%m-%d")
            timetable_seances = get_timetable_seances(company_id, staff_id, search_date, user_token)

            if timetable_seances and 'data' in timetable_seances:
                available_slots = filter_and_merge_available_slots(timetable_seances['data'], duration_minutes)
                if available_slots:
                    available_slots_per_staff[staff_name].append({
                        'date': search_date,
                        'slots': available_slots
                    })

    return available_slots_per_staff

# Пример вызова
company_id = COMPANY_ID
service_id = 11850477
start_date = "2024-09-15"
user_token = USER_TOKEN

available_dates = find_available_dates_with_seances(company_id, service_id, start_date, user_token)

# Выводим результат
if available_dates:
    for staff, dates in available_dates.items():
        print(f"Сотрудник: {staff}")
        for date_info in dates:
            print(f"  Дата: {date_info['date']}")
            print(f"  Свободные слоты: {', '.join(date_info['slots'])}")
else:
    print("Нет доступных сотрудников или свободных слотов.")
### "GET SLOTS" BLOCK END