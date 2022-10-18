import requests

s = requests.Session()
r = s.get("http://www.google.com?q=fuck+you")
with open('fucked.html','w+') as f:
    f.write(r.text)
