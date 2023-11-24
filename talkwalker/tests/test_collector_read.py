from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from talkwalker.classes.asker import Asker
from project.models import Post

from django.test import TestCase
from django.conf import settings

import responses
import os
import re
import json


class AskerTestCase(TestCase):
    def read_file(self, name):
        return '}\n{'.join(re.sub(r'\s+', '', open(os.path.join(settings.BASE_DIR, name)).read()).split('}{'))

    @responses.activate
    def test_collector_reads_chunks(self):
        """Collector reads posts through all chunks"""
        SpeechFactory(language='English (United States)')
        project = ProjectFactory()
        token   = 'acfaad27-3948-4e13-a617-2d33fd97552a_ZStqaRbxfzpRBT7YfbIqUPJPVwa2.QUzpFqzvPtKdHdc5UNZrYlHyk03MPxVkGKfZ6n3Y4i.meiy.FNZ621ZSmhzzb.gJAlvHtslEq7PP0B3JbDC4BS1y.hwK9fPz7vMQXvSfQFXka9.gEKovum-Pu0LYzy8GSjjSLvBdA1fV5M'

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=earliest&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream1.json')
        )

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=EgT4kpRi&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream2.json')
        )

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=EgSIlpRi&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream3.json')
        )

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=EgTslpRi&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream4.json')
        )

        result = Asker(project.id, 'Project')._Asker__04_read_collector()
        self.assertTrue(result)
        self.assertTrue(project.posts.all().count() > 328)

        project.refresh_from_db()
        self.assertEqual(project.resume_offset, 'EgTslpRi')

    @responses.activate
    def test_collector_reads_updates(self):
        """Collector reads only the last chunk of data when resume offset is set"""
        SpeechFactory(language='English (United States)')
        project = ProjectFactory(resume_offset='EgSIlpRi')
        token   = 'acfaad27-3948-4e13-a617-2d33fd97552a_ZStqaRbxfzpRBT7YfbIqUPJPVwa2.QUzpFqzvPtKdHdc5UNZrYlHyk03MPxVkGKfZ6n3Y4i.meiy.FNZ621ZSmhzzb.gJAlvHtslEq7PP0B3JbDC4BS1y.hwK9fPz7vMQXvSfQFXka9.gEKovum-Pu0LYzy8GSjjSLvBdA1fV5M'

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=EgSIlpRi&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream3.json')
        )

        responses.add(
            responses.GET,
            f'https://api.talkwalker.com/api/v3/stream/c/search-{project.id}-onl-col/results?access_token={token}&resume_offset=EgTslpRi&end_behaviour=stop',
            body=self.read_file('fixtures/talkwalker/collector_stream4.json')
        )

        result = Asker(project.id, 'Project')._Asker__04_read_collector()
        self.assertTrue(result)
        self.assertEqual(project.posts.all().count(), 30)

        project.refresh_from_db()
        self.assertEqual(project.resume_offset, 'EgTslpRi')
