import json
import requests
import os
from dotenv import load_dotenv
from modules import checkcity


load_dotenv()

#Loads the API Key and API URL from the .env file.
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

#Asks the user which city he wants to recieve weather information.
while True:
    city_input = input("Enter the name of the city: ")
    # Checks if the entered city is valid
    if checkcity.check_contains_city(city_input) == False:
        print("The city you entered is not valid. \nPlease enter a valid city. \n")
    else:
        #Gets the weather information from the API
        response = requests.get(API_URL + "?q=" + city_input + "&appid=" + API_KEY)
        response_json  = json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8')
        decoded_file = response_json.decode('utf8') #The file must be decoded before it can be written to a file
        with open('json_data.json', 'w') as outfile:
            outfile.write(decoded_file)
        break




