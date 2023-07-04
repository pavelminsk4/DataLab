from talkwalker.services.token import get_token
import requests
import json


def create_target_collector(collector_id='datalab'):
    token = get_token()
    url = f'https://api.talkwalker.com/api/v3/stream/c/{collector_id}?access_token={token}'
    print('--->url', url)
    payload = json.dumps({})
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    req_id = json.loads(response.text)['request_id']
    print('--->', response.text)
    return collector_id
