import requests

s = requests.Session()
r = s.get("http://motherfuckingwebsite.com")
with open('mfwebsite.html','w+') as f:
    f.write(r.text)