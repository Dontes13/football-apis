import requests
import pandas as pd
import sqlalchemy as db
from pprint import pprint

API_KEY = 'bb56c97b593c449a8bbbe4c46802a239'

headers = {'X-Auth-Token': API_KEY}

url = 'https://api.football-data.org/v4/competitions/PL/standings'

response = requests.get(url, headers=headers)
data = response.json()
competition_year = data['filters']['season']

for item in data['standings'][0]['table']:
  team_name = item['team']['name']
  item['team'] = team_name

#pprint(data['standings'][0]['table'])
#exit()

df = pd.DataFrame(data['standings'][0]['table'])


engine = db.create_engine('sqlite:///football.db')
df.to_sql('standings', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
  query = "SELECT * FROM standings;"
  query_result = connection.execute(db.text(query)).fetchall()
  print(f"Season Start: {competition_year}")
  print(pd.DataFrame(query_result))
