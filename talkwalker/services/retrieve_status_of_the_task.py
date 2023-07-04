from talkwalker.services.token import get_token
import requests
import json


def retrieve_status_of_the_task(task_id):
    print('------>ret_status')
    token = get_token()
    url = f'https://api.talkwalker.com/api/v3/tasks/export/{task_id}?access_token={token}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    lines = response.iter_lines()
    for line in lines:
        try:
            status = json.loads(line)['result_tasks']['tasks'][0]['status']
        except:
            status = ''
            pass
    return status
