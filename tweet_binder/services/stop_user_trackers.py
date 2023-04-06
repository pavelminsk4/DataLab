import requests
import json

def stop_user_trackers(auth_token):
    url = "https://api2.tweetbinder.com/user-trackers/delete"

    payload = json.dumps({
    "userTrackers": [
        "0e4b5c3c-e71a-4b82-922b-9aa8e9329439"
    ]
    })
    headers = {
    'Authorization': 'Bearer ' + auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.text
