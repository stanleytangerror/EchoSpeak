import requests
import json

r = requests.post("http://localhost:8080/chat", json={'message': 'Hi, it is sunny outside!'})

print(r.status_code, r.reason)
resp = json.loads(r.text)
print(f"refine: {resp['refine']}")
print(f"reply: {resp['reply']}")
