
screat_key = "sk-Zaf2uleEp063EhFt81D9225c4b98470b84Fb0cE595E9Fe0c"

import requests
import json

url = "https://api.gpt.ge/v1/chat/completions"

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
headers = {
   'Authorization': 'Bearer {}'.format(screat_key),
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)