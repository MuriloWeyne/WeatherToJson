import json
import requests
import os
from dotenv import load_dotenv
from modules import checkcity
from modules import cleanup

load_dotenv()

#Loads the API Key and API URL from the .env file.
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

#Asks the user which city he wants to recieve weather information.
while True:
    city_input = input("Enter the name of the city: ")
    city_clean = cleanup.cleanup(city_input)
    response = requests.get(API_URL + "?q=" + city_input + "&appid=" + API_KEY)
    # Checks if the entered city is valid
    if checkcity.check_contains_city(city_input) == False:
        print("The city you entered is not valid. \nPlease enter a valid city. \n")
    # Handles a commom error that may have been caused by the lack of '' in the .env file
    elif str(response) == '<Response [401]>':
        response = requests.get(API_URL + "?q=" + city_input + "&appid=" + f'{API_KEY}')
    else:
        #Gets the weather information from the API
        response_json  = json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8')
        #File must be decoded before it can be written to a file
        decoded_file = response_json.decode('utf8')
        save_path = 'json_data/'
        file_name = city_clean + '_data.json'
        complete_name = os.path.join(save_path, file_name)
        #Creates a folder to store all the json_files requested by the user
        os.makedirs('json_data', exist_ok=True) 
        with open(complete_name, 'w') as outfile:
            outfile.write(decoded_file)
        break




