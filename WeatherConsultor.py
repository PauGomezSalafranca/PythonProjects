"""Este sencillo programa utiliza una API externa de openweather.org para conseguir
   información sobre el tiempo meteorológico de cualquier localidad del mundo"""

import requests
from pprint import pprint

ApiKey = 'aa1e8e7b28be41c5ad94d0a3c460bc27'

city = input("Introduce una ciudad: ")
baseUrl = "http://api.openweathermap.org/data/2.5/weather?appid="+ApiKey+"&q="+city

weatherData = requests.get(baseUrl).json()

pprint(weatherData)