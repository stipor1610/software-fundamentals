'''
    API: Application Programming Interface
    Nasa API: https://api.nasa.gov/
    API_KEY_NASA: YOUR NASA API_key
    Developer: Joan C. Ayala
    Date: 09112025
    Script description: Get and read data from NASA API about comets and others
    https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}
'''
import requests
import os

os.system('cls')

def get_nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726710?api_key={api_key}"

    #Realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status() #=> Valida si se presenta algún error en la petición
    data = response.json() #Convertir la respuesta a formato JSON (JS Object Notation)

    print(data)

API_KEY_NASA = 't5u4Rmymd0b3wdNbAQ3QszcXhEVlBbd6pvFyUXRo'
get_nasa_data(API_KEY_NASA)
