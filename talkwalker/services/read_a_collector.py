from talkwalker.services.token import get_token
import requests


def read_collector(collector_id='datalab'):
    token = get_token()
    url = f'https://api.talkwalker.com/api/v3/stream/c/{collector_id}/results?access_token={token}&resume_offset=earliest&end_behaviour=stop'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    lines = response.iter_lines()
    return lines
