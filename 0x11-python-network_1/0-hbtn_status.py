#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('\t- type:', type(html))
print('\t- content:', html)
utf8_content = html.decode('utf-8')
print('\t- utf8 content:', utf8_content)
