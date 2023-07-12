from datetime import datetime
import requests
import json

def historical_search(keyword, keyword_and, keyword_or, keyword_nor, limit, start_date, end_date, auth_token, historical_search_url):
    keywords_and = [keyword]
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

