from talkwalker.services.create_posts import create_posts
from talkwalker.services.get_tw_query import get_tw_query
from talkwalker.services.token import get_token
from rest_framework import status
from django.apps import apps

import threading
import requests
import environ
import json


class Asker:
    def __init__(self, project_id, module):
        model = ''
        if module=='Project':
            model = apps.get_model('project', 'Project')
            self.collector_id = f'search-{project_id}-onl-col'
        if module=='ProjectTwentyFourSeven':
            model = apps.get_model('twenty_four_seven', 'ProjectTwentyFourSeven')
            self.collector_id = f'search-{project_id}-tfs-col'
        self.project = model.objects.get(id=project_id)

    token = get_token()
    task_id = ''

    def __01_create_target_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.token}'
        headers = { 'Content-Type': 'application/json' }
        response = requests.request('PUT', url, headers=headers, data={})
        return response.status_code == status.HTTP_200_OK

    def __02_new_task_on_query(self):
        url = f'https://api.talkwalker.com/api/v3/stream/export?access_token={self.token}'
        payload = json.dumps({
            'target': self.collector_id,
            'start':  self.project.start_search_date.date().isoformat(),
            'stop':   self.project.end_search_date.date().isoformat(),
            'limit':  environ.Env()('TALKWALKER_LIMIT'),
            'query':  get_tw_query(self.project),
        })
        headers = { 'Content-Type': 'application/json' }
        response = requests.request('POST', url, headers=headers, data=payload)
        lines = response.iter_lines()
        for line in lines:
            self.task_id = json.loads(line)['result_tasks']['tasks'][0]['id']
        return response.status_code == status.HTTP_200_OK

    def __03_retrieve_status_of_task(self):
        url = f'https://api.talkwalker.com/api/v3/tasks/export/{self.task_id}?access_token={self.token}'
        response = requests.request('GET', url, headers={}, data={})
        lines = response.iter_lines()
        for line in lines:
            try:
                status = json.loads(line)['result_tasks']['tasks'][0]['status']
                print(status)
            except:
                status = ''
                pass
        return status

    def __wait_until_limit_reached(self):
        i = 0
        while i < 200:
            i = i + 1
            status = self.__03_retrieve_status_of_task()
            if status == 'result_limit_reached':
                break

    def __04_read_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}/results?access_token={self.token}&resume_offset=earliest&end_behaviour=stop'
        response = requests.request('GET', url, headers={}, data={})
        lines = response.iter_lines()
        create_posts(self.project, lines)
        return response.status_code == status.HTTP_200_OK

    def __05_delete_collector(self):
        url = f'https://api.talkwalker.com/api/v3/stream/c/{self.collector_id}?access_token={self.token}'
        response = requests.request('DELETE', url, headers={}, data={})
        return response.status_code == status.HTTP_200_OK

    def run_gen(self):
        self.__01_create_target_collector()
        self.__02_new_task_on_query()
        self.__wait_until_limit_reached()
        self.__04_read_collector()
        return self.__05_delete_collector()

    def run(self):
        thread = threading.Thread(target=self.run_gen, name='run')
        thread.start()
