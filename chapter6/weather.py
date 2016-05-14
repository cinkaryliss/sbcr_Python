import requests
import pprint
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {'city':'130010'}
weather_data = requests.get(api_url, params=payload).json()
pprint.pprint(weather_data)
