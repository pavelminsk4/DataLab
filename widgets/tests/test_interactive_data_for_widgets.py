from common.factories.change_sentiment.change_sentiment import ChangingOnlineSentimentFactory
from common.factories.department import DepartmentFactory
from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.speech import SpeechFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from project.models import Project
from rest_framework import status
from project.models import Post
import json
from common.factories.user import UserFactory


class InteractiveWidgetsTests(APITestCase):
    def setUp(self):
        flink = FeedlinkFactory(country='England', source1='Time')
        sp1 = SpeechFactory(language='English')
        sp2 = SpeechFactory(language='Georgian')
        self.post1 = PostFactory(
            feedlink=flink, entry_title='First post title', entry_summary='First', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='neutral'
        )
        self.post2 = PostFactory(
            feedlink=flink, entry_title='Second post title', entry_summary='Second post post title', feed_language=sp2,
            entry_published='2022-09-03T00:00:00Z', entry_author='AFP', sentiment='negative'
        )
        self.post3 = PostFactory(
            feedlink=flink, entry_title='Third post title', entry_summary='Third summary', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='neutral'
        )
        self.post4 = PostFactory(
            feedlink=flink, entry_title='Fourth post title', entry_summary='Fourth summary', feed_language=sp1,
            entry_published='2021-09-03T00:00:00Z', entry_author='AFP', sentiment='negative'
        )
        self.project = ProjectFactory(keywords=['post'])
        self.project.posts.set([self.post1, self.post2])
        self.url = f'/api/widgets/interactive_widgets/{self.project.id}/'
        self.widget_list = self.project.widgets_list_2    
        

    def test_top_10_interactive_widgets(self):
        project = self.project
        widget = self.widget_list.top_languages_id
        data = {
            'first_value': ['English'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)

    def test_sentiment_top_10_interactive_widgets(self):
        project = self.project
        widget = self.widget_list.sentiment_top_languages_id
        data = {
            'second_value': ['negative'],
            'first_value': ['Georgian'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)

    def test_sentiment(self):
        project = self.project
        widget = self.widget_list.sentiment_for_period_id
        data = {
            'first_value': ['Negative'],
            'second_value': [],
            'dates': ['2022-01-03T00:00:00Z', '2022-10-03T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)

    def test_content_volume(self):
        project = self.project
        widget = self.widget_list.volume_id
        data = {
            'first_value': [],
            'second_value': [],
            'dates': ['2022-01-03T00:00:00Z', '2022-10-03T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)

    def test_top_keywords(self):
        project = self.project
        widget = self.widget_list.top_keywords_id
        data = {
            'first_value': ['post'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)

    def test_sentiment_top_keywords(self):
        project = self.project
        widget = self.widget_list.sentiment_top_keywords_id
        data = {
            'first_value': ['post'],
            'second_value': ['Negative'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)

    def test_sentiment_diagram(self):
        project = self.project
        widget = self.widget_list.sentiment_diagram_id
        data = {
            'first_value': ['Negative'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'],  self.post2.id)

    def test_authors_by_country(self):
        project = self.project
        widget = self.widget_list.authors_by_country_id
        data = {
            'first_value': ['AFP'],
            'second_value': ['England'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)

    def test_authors_by_sentiment(self):
        project = self.project
        widget = self.widget_list.authors_by_sentiment_id
        data = {
            'first_value': ['AFP'],
            'second_value': ['Neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content) ['posts'][0]['id'], self.post1.id)

    def test_sources_by_country(self):
        project = self.project
        widget = self.widget_list.sources_by_country_id
        data = {
            'first_value': ['Time'],
            'second_value': ['England'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)

    def test_sources_by_language(self):
        project = self.project
        widget = self.widget_list.sources_by_language_id
        data = {
            'first_value': ['Time'],
            'second_value': ['English'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)

    def test_with_date_interval(self):
        project = self.project
        project.start_search_date = '2022-09-03T00:00:00Z'
        project.save()
        widget = self.widget_list.sources_by_language_id
        data = {
            'first_value': ['Time'],
            'second_value': ['English'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
      
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'first_value': ['Time'],
            'second_value': ['Georgian'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        
        response = self.client.post(f'{self.url}{widget}', data, format='json')
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post2.id)
