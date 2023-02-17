from datetime import datetime
import requests
import json

def historical_search(keyword, limit, start_date, end_date, auth_token, historical_search_url):
    payload = json.dumps({
    "query": {
        "must": [keyword, "-RT"],
        "limit": limit,
        "startDate": int(datetime.timestamp(start_date)),
        "endDate": int(datetime.timestamp(end_date)),    
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("POST", historical_search_url, headers=headers, data=payload)
    return response.text

