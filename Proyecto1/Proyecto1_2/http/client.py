import requests

x = requests.get('http://127.0.0.1/')

print(x.content)