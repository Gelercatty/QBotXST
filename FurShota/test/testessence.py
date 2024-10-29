import requests
import json

url = "http://127.0.0.1:3000/get_essence_msg_list"

payload = json.dumps({
   "group_id": 589648813
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)