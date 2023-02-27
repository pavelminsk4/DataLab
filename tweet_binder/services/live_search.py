import requests
import json

def live_search(keyword, limit, auth_token, live_search_url):
    webhook = "https://staging.datalab.net/webhook/"
    payload = json.dumps({
                            "query": {
                                    "must": [keyword, "-RT"],
                                    "limit": limit,
                                    },
                            "webhookURL": webhook,
                        })
    headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + auth_token
              }
    response = requests.request("POST", live_search_url, headers=headers, data=payload)
    return response.text
