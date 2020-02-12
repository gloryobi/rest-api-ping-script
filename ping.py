import requests
import json

#replace url with whatever URL you'd like to ping
url = 'http://34.205.48.205:3000/'

res = requests.get(url)
logged_response = ""

if res.status_code != 200:
    logged_response = "ERROR: There's been a problem with the ping response. Response is {}".format(res.status_code)
elif res.text == "":
    logged_response = "ERROR: The response body is empty"
else:
    logged_response = "Successful Ping. Response is {}".format(res.status_code)

print(logged_response)


# Posting to a Slack channel

# replace webhook_url with the URL for the webhook you've created in your slack channel
webhook_url = "ENTER_WEBHOOK_URL_HERE"
def send_message_to_slack(text):
    post = {"text": "{0}".format(text)}
 
    try:
        json_data = json.dumps(post)
        req = requests.post(webhook_url, data=json_data.encode('ascii'), headers={'Content-Type': 'application/json'}) 
        res = req.text
    except Exception as em:
        print("EXCEPTION: " + str(em))

# uncomment this if you have a valid webhook_url initiated
# send_message_to_slack(logged_response)