import requests
import json

def basic_search(keyword_and, keyword_or, keyword_nor, limit, auth_token, url):
    keywords_and = []
    [keywords_and.append(key) for key in keyword_and]
    keywords_or = []
    [keywords_or.append(key) for key in keyword_or]
    keywords_nor = []
    [keywords_nor.append(key) for key in keyword_nor]
    payload = json.dumps({
    "query": {
        "must": keywords_and,
        "or": keywords_or,
        "nor": keywords_nor,
        "limit": limit
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
