from urllib import response
import requests
import json

response = requests.get('https://hiring.bajajfinservhealth.in/api/renderMe')

# print(response.json())

for data in response.json():
    print(data['login'])
    print(data['avatar_url'])
    print(data['url']['html_url'])
    print(data['type'])
    
# https://pastebin.com/GjBa7dRk
