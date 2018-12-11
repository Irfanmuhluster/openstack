import requests
import json

url = "http://rocky-controller.jcamp.net:5000/v3/auth/tokens"
data = '{ "auth": { "identity": { "methods": ["password"],"password": {"user": {"domain": {"name": "'"Default"'"},"name": "'"irvan"'", "password": "'"M0nalisa"'"} } }, "scope": { "project": { "domain": { "name": "'"Default"'" }, "name":  "'"irvan"'" } } }}'
r = requests.post(url, data)

header = {'X-Auth-Token': r.headers['X-Subject-Token']}

instance = requests.get(
    "http://rocky-controller.jcamp.net:8774/v2.1/servers", headers=header)
json = json.loads(instance.content)

for ext in json['servers']:
    id = ext['id']
    name = ext['name']
    print(f'nama : {name}')
    print(f'Id : {id}')
    print('====')
