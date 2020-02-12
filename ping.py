import requests

url = 'http://34.205.48.205:3000/'

res = requests.get(url)

if res.status_code != 200:
    print("ERROR: There's been a problem with the ping response. Response is", res.status_code)
elif res.text == "":
    print("ERROR: The response body is empty")
else:
    print("Successful Ping. Response is", res.status_code)