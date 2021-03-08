import requests
import json

apiKey = "YOUR-API-KEY"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:YOUR-BOARD-ID, group_id:certificate_management ,item_name:$myItemName, column_values:$columnVals) { id } }'
vars = {
    'myItemName' : 'Cert71!',
    'columnVals' : json.dumps({
        'status' : {'label' : 'Done'},
        'date' : {'date' : '2023-08-27'}
 })
}

data = {'query' : query5, 'variables' : vars}
r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())
