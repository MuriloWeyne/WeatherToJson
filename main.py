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

#Declares the current state and alphabet string used to write the requested data to .json files.
state = 'asking'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVW'

#Declares all lists used to store data while the code is running.
cities = []
clean_cities = []
file_names = []
responses = []
json_responses = []
decoded_files = []
outfiles = []
complete_names = []

while True:
    #Asks the user which city he wants to recieve weather information.
    while (state == 'asking'):
        city_input = input("Enter the name of the city: ")
        more_cities = input("Do you want to input another city? (y/n): ")
        cities.append(city_input)
        if more_cities == 'n':
            break
    
    #Cleans the user input so it can be used to correctly address it to a file name.
    clean_city = cleanup.cleanup(city_input)
    if (len(cities) > 1):
        for i in range(len(cities)):
            clean = cleanup.cleanup(cities[i])
            clean_cities.append(clean)
        for city in cities:
            response = requests.get(API_URL + "?q=" + city + "&appid=" + API_KEY)
            responses.append(response)
        
    else:
            response = requests.get(API_URL + "?q=" + city_input + "&appid=" + API_KEY)
            clean_cities.append(clean_city)
    # Handles a commom error that may have been caused by the lack of '' in the .env file
    if str(response) == '<Response [401]>':
        response = requests.get(API_URL + "?q=" + city_input + "&appid=" + f'{API_KEY}')
        if str(response) == '<Response [401]>':
            print("Please check if you entered your API key correctly in the .env file.")
            break
    # Checks if the entered city is valid
    if checkcity.check_contains_city(city_input) == False:
        print("The city you entered is not valid. \nPlease enter a valid city. \n")
    else:
        #Creates a folder to store all the json_files requested by the user
        os.makedirs('json_data', exist_ok=True)
        if (len(responses) > 1):
            for resp in responses:
                response_json  = json.dumps(resp.json(), indent=4, ensure_ascii=False).encode('utf8')
                json_responses.append(response_json)
                #File must be decoded before it can be written to a file
                decoded_file = response_json.decode('utf8')
                decoded_files.append(decoded_file)
        else:
            response_json  = json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8')
            #File must be decoded before it can be written to a file
            decoded_file = response_json.decode('utf8')
            decoded_files.append(decoded_file)
        save_path = 'json_data/'
        
        #Code below is used to write the request data into files.
        j = 0
        while (j<len(decoded_files)):
            outfiles.append(alphabet[j])
            j += 1
        for city_clean in clean_cities:
            file_name = city_clean + '_data.json'
            file_names.append(file_name)
            complete_name = os.path.join(save_path, file_name)
            complete_names.append(complete_name)
            for k in range(len(complete_names)):
                for outfile in outfiles:
                    with open(complete_names[k], 'w') as outfile:
                            outfile.write(decoded_files[k])
        break




