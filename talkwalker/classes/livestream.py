from talkwalker.services.get_tw_query import get_tw_query
from talkwalker.services.create_posts import create_posts
from talkwalker.services.token import get_token
from rest_framework import status
from django.apps import apps
import requests
import json


class Livestream:
    def __init__(self, project_id, module):
        model = ''
        if module == 'Project':
            model = apps.get_model('project', 'Project')
            self.collector_id = f'livestream-{project_id}-onl-col'
        if module == 'ProjectTwentyFourSeven':
            model = apps.get_model('twenty_four_seven', 'ProjectTwentyFourSeven')
            self.collector_id = f'livestream-{project_id}-tfs-col'
        self.project = model.objects.get(id=project_id)
        self.stream_id = f'livestream-{project_id}-'

    token = get_token()

    def __01_create_or_update_stream(self):
        url = f'https://api.talkwalker.com/api/v3/stream/s/{self.stream_id}?access_token={self.token}'
        payload = json.dumps({
            'rules': [
                {
                    'rule_id': f'{self.stream_id}-rule',
                    'query': get_tw_query(self.project)
                }
            ]
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request('PUT', url, headers=headers, data=payload)
        return response.status_code == status.HTTP_200_OK

    def __02_create_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.token}'
        payload = json.dumps({
            'collector_query': {
                'streams': [
                    self.stream_id
                ]
            }
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request('PUT', url, headers=headers, data=payload)
        return response.status_code == status.HTTP_200_OK

    def __read_chunk(self, offset):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}/results?access_token={self.token}&resume_offset={offset}&end_behaviour=stop'

        response = requests.request('GET', url, headers={}, data={})
        lines    = response.iter_lines()

        return create_posts(self.project, lines, offset)

    def __03_read_collector(self):
        resume_offset = self.project.resume_offset or 'earliest'
        while resume_offset:
            resume_offset = self.__read_chunk(resume_offset)

        return True

    def __04_delete_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.token}'
        response = requests.request('DELETE', url, headers={}, data={})
        return response.status_code == status.HTTP_200_OK

    def __05_delete_stream(self):
        url = f'https://api.talkwalker.com/api/v3/stream/s/{self.stream_id}?access_token={self.token}'
        response = requests.request('DELETE', url, headers={}, data={})
        return response.status_code == status.HTTP_200_OK

    def create(self):
        self.__01_create_or_update_stream()
        return self.__02_create_collector()

    def read(self):
        return self.__03_read_collector()

    def delete(self):
        self.__04_delete_collector()
        return self.__05_delete_stream()
