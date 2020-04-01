#! python3

import json, sys, requests

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location lorem ')
    sys.exit()
location = ' '.join(sys.argv[1:])

key = 'b1b15e88fa797225412429c1c50c122a1'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location, key)
print(url)
response = requests.get(url)
#response.raise_for_status()
print(response.text)
