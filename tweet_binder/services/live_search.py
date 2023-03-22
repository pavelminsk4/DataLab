import requests
import json

def live_search(keyword, keyword_and, keyword_or, keyword_nor, limit, auth_token, live_search_url):
    keywords_and = ["-RT", keyword]
    [keywords_and.append(key) for key in keyword_and]
    keywords_or = ["-RT"]
    [keywords_or.append(key) for key in keyword_or]
    keywords_nor = []
    [keywords_nor.append(key) for key in keyword_nor]
    webhook = "https://staging.datalab.net/webhook/"
    payload = json.dumps({
                            "query": {
                                        "must": keywords_and,
                                        "or": keywords_or,
                                        "nor": keywords_nor,
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
