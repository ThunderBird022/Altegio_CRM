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


