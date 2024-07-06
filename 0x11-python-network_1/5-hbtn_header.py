#!/usr/bin/python3
import sys
import requests
url=sys.arge[1]
response = requests.get(url)
X_Request_Id = response.header.get('X-Request-Id'):
    if X_Request_Id:
        print(X_Request_Id)
    else:
        print(response.status_code)
