from talkwalker.services.token import get_token
import requests


def delete_collector(collector_id='datalab'):
    token = get_token()
    url = f'https://api.talkwalker.com/api/v3/stream/c/{collector_id}?access_token={token}'
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)
