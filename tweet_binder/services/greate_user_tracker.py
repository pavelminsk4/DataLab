import requests
import json

def greate_user_tracker(user_alias, auth_token, url):
    payload = json.dumps([
    {
        "alias": user_alias
    }
    ])
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
