import requests
import json

def stop_user_trackers(url, auth_token, tracker_id):
    payload = json.dumps({
    "userTrackers": [
        f"{tracker_id}"
    ]
    })
    headers = {
    'Authorization': 'Bearer ' + auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.text
