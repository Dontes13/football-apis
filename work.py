import requests

API_KEY = 'bb56c97b593c449a8bbbe4c46802a239'

headers = {'X-Auth-Token': API_KEY}

url = 'https://api.football-data.org/v4/competitions/PL/standings'

response = requests.get(url, headers=headers)
print(response.json())