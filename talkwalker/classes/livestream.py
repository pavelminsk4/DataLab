from talkwalker.services.get_tw_query import get_tw_query
from talkwalker.services.create_post import create_post
from talkwalker.services.token import get_token

from project.models import Project
from rest_framework import status
import requests
import json


class Livestream:
    def __init__(self, project_id):
        self.project = Project.objects.get(id=project_id)
        self.collector_id = f'livestream-{project_id}-col'
        self.stream_id = f'livestream-{project_id}'

    __token = get_token()

    def __05_delete_stream(self):
        url = f'https://api.talkwalker.com/api/v3/stream/s/{self.stream_id}?access_token={self.__token}'
        response = requests.request('DELETE', url, headers={}, data={})
        return response.status_code == status.HTTP_200_OK

    def __04_delete_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.__token}'
        response = requests.request('DELETE', url, headers={}, data={})
        return response.status_code == status.HTTP_200_OK

    def __03_read_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}/results?access_token={self.__token}&end_behaviour=stop'
        response = requests.request('GET', url, headers={}, data={})
        lines = response.iter_lines()
        for line in lines:
            create_post(line)
        print(f'03_read_collector ---> status: {response.status_code}')
        return response.status_code == status.HTTP_200_OK

    def __02_create_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.__token}'
        payload = json.dumps({
            'collector_query': {
                'streams': [
                    self.stream_id
                ]
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request('PUT', url, headers=headers, data=payload)
        print('02_create_collector --->', response.text)
        return response.status_code == status.HTTP_200_OK

    def __01_create_or_update_stream(self):
        url = f'https://api.talkwalker.com/api/v3/stream/s/{self.stream_id}?access_token={self.__token}'
        payload = json.dumps({
            'rules': [
                {
                    'rule_id': f'{self.stream_id}-rule',
                    'query': get_tw_query(self.project)
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request('PUT', url, headers=headers, data=payload)
        print('01_create_or_update_stream --->', response.text)
        return response.status_code == status.HTTP_200_OK

    def create(self):
        self.__01_create_or_update_stream()
        return self.__02_create_collector()

    def read(self):
        return self.__03_read_collector()
    
    def delete(self):
        self.__04_delete_collector()
        return self.__05_delete_stream()
