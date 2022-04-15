from urllib import response
import requests
import json

response = requests.get('https://hiring.bajajfinservhealth.in/api/renderMe')

# print(response.json())

mylist = []

for data in response.json():
    temp = {}
    temp['login'] = data['login']
    temp['avatar_url'] = data['avatar_url']
    temp['html_url'] = data['url']['html_url']
    temp['type'] = data['type']
    mylist.append(temp)

print(mylist)


# https://pastebin.com/i8GZj3K9
