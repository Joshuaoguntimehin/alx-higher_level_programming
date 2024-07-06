#!/usr/bin/python3
import sys
import urllib.parse
import urllib.request
url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8') 
request = urllib.request.Request(url, data=data) 
with urllib.request.urlopen(request) as response: 
    html = response.read().decode('utf-8') 
    # Print the response body 
    print(html) 
