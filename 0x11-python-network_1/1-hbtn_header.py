#!/usr/bin/env python3
import urllib.request
import sys


url = "https://alx-intranet.hbtn.io"
with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(f"{x_request_id}")
    else:
        print("X-Request-Id header not found in the response.")
