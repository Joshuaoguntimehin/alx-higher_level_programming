import sys
import urllib.parse
import urllib.request
def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email}).encode() 
    request = urllib.request.Request(url, data=data) 
    with urllib.request.urlopen(request) as response: 
        response_body = response.read().decode('utf-8') 
        # Print the response body 
        print(response_body) 
        if __name__ == "__main__"
        url = sys.argv[1]
        email = sys.args[2]
