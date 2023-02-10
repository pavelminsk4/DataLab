import requests
import json

def basic_search(keyword, limit, auth_token, url):
    payload = json.dumps({
    "query": {
        "must": [keyword,"-RT"],
        "limit": limit
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
