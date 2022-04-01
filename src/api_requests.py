import requests

location_search = 'location/search/'
location = 'location/'
# aufgabe 1.1
url = 'https://www.metaweather.com/api/'
params = {'query': 'frankfurt'}


response = requests.get(url+location_search, params)
json = response.json()

print('Response code: ', response.status_code)
print('Response json: ', response.json())
print('Response woeid: ', json[0]['woeid'])
print('Response latt_long: ', json[0]['latt_long'])
# aufgabe 1.2

woeid = json[0]['woeid']
response_weather_frkt = requests.get(url + location + str(woeid))

print('response_weather_frkt code: ', response_weather_frkt.status_code)
print('response_weather_frkt json: ', response_weather_frkt.json())
