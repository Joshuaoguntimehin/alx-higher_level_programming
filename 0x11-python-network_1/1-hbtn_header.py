#!/usr/bin/python3
"""import statement"""
import urllib.request
import sys
"""send a request"""
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(f"{x_request_id}")
    else:
        exit(1)
