import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

#Loads the API Key and API URL from the .env file
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

def check_contains_city(city_input):
    checker = requests.get(API_URL + "?q=" + city_input + "&appid=" + API_KEY)
    if (checker.content.decode('utf8')) == '{"cod":"404","message":"city not found"}':
        return False
    else:
        return True