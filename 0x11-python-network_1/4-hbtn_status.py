#!/usr/bin/python3
"""import statement"""
import requests
"""first test for requeste"""
url='https://alx-intranet.hbtn.io/status'
response =requests.get(url)
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
