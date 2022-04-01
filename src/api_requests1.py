import requests
# Get Request to https://www.metaweather.com/api/location/650272/
params = {'query': 'frankfurt'}
headers = {"Content-Type": 'application/json'}
result = requests.get(
    'https://www.metaweather.com/api/location/650272/',
    params=params,
    headers=headers
)

json = result.json()
print('JSON Response: ', json)
print('wetter_5day: ', json[0]['id'])
print('weather_state_name: ', json[0]['weather_state_name'])
print('weather_state_abbr: ', json[0]['weather_state_abbr'])
print('wind_direction_compass: ', json[0]['wind_direction_compass'])
