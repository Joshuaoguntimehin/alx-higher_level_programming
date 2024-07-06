#!/usr/bin/python3
"""import statement"""
import sys
import requests
"""more test on requests"""
url = sys.argv[1]
response = requests.get(url)
X_Request_Id = response.headers.get('X-Request-Id')
"""if statement"""
if X_Request_Id:
    print(X_Request_Id)
else:
    print(response.status_code)
