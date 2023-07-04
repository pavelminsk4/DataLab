from talkwalker.services.token import get_token
import requests


def retrieve_all_recent_tasks_status():
    token = token
    url = f'https://api.talkwalker.com/api/v3/tasks/export?access_token={token}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
