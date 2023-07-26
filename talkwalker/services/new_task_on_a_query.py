from talkwalker.services.token import get_token
import requests
import json


def new_task(start_date, stop_date, limit, query, target):
    token = get_token()
    url = f'https://api.talkwalker.com/api/v3/stream/export?access_token={token}'
    print('--->params',query)
    payload = json.dumps({
        "target": "datalab",
        'start': start_date.date().isoformat(),
        'stop': stop_date.date().isoformat(),
        'limit': limit,
        "query": query,
        'target': target,
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    lines = response.iter_lines()
    for line in lines:
        task_id = json.loads(line)['result_tasks']['tasks'][0]['id']
    return task_id
