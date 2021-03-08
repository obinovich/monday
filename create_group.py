import requests
import json


apiKey = "YOUR-API-KEY"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query5 = 'mutation { create_group (board_id:YOUR-BOARD-ID, group_name:YOUR-GROUPNAME) { id } }'

data = {'query' : query5}
r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())
