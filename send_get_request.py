import requests
import json

# A simple function to send a get request to given URL
def send_get_request(url):
    response = requests.get(url)
    return response

# A simple function to send a post request to given URL
def send_post_request(url, data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

if __name__ == "__main__":
    response = send_get_request("http://0.0.0.0:8000")
    # response = send_get_request("http://sgondala-dummy-server.up.railway.app")
    # response = send_post_request("http://sgondala-dummy-server.up.railway.app/get_email/", data={"name": "Sai Gondala"})
    print(response.text)
