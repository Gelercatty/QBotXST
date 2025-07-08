

import requests
import json

url = "https://api.gpt.ge/v1/chat/completions"
url = "https://api.deepseek.com"

payload = json.dumps({
   "model": "o1-mini",
   "messages": [
      {
         "role": "user",
         "content": "晚上好"
      }
   ],
   "max_completion_tokens": 1688,
   "stream": False
})
secret_key = ""
headers = {
   'Authorization': 'Bearer {}'.format(screat_key),
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)