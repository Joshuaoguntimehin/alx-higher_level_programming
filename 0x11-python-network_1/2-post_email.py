import urllib.request
mport urllib.parse
import sys

url=sys.argv[1]
email=({'email':'sys.argv[2]'})
data=urllib.parse.urlencode(email)
data = data.encode('utf-8')
req = url.request.Request(url, email)
with urllib.request.Request(req) as response:
    html = response.,read().decode('utf-8')
    print(html)    
send_past_request(url, email)