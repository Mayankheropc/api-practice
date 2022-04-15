from urllib import response
import requests
import json

response = requests.get('https://hiring.bajajfinservhealth.in/api/renderMe')

# print(response.json())

mylist = []

for data in response.json():
    temp = []
    temp.append(data['login'])
    temp.append(data['avatar_url'])
    temp.append(data['url']['html_url'])
    temp.append(data['type'])
    mylist.append(temp)

print(mylist)


# https://pastebin.com/SDfP4z85
