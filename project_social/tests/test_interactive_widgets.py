from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.user import UserFactory


class InteractiveWidgetsTests(APITestCase):
    def setUp(self):
        user = UserFactory(username='Pablo Escobar')
        TweetBinderPostFactory(user_name='First', text='First twitter post', language='En', date='2020-10-10T00:00:00Z',
                               sentiment='neutral', user_location='USA', user_gender='male', user_alias='First')
        TweetBinderPostFactory(user_name='Second', text='Second twitter post', language='Sp', date='2020-10-10T00:00:00Z',
                               sentiment='positive', user_location='England', user_gender='female', user_alias='First')
        TweetBinderPostFactory(user_name='Third', text='3 twitter post', language='En', date='2021-10-10T00:00:00Z',
                               sentiment='neutral', user_location='USA', user_gender='undefined', user_alias='First')
        ProjectSocialFactory(creator=user)

    def test_top_languages(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_languages_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(text='Second twitter post').pk
        data = {
            'first_value': ['Sp'],
            'second_value': [''],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_top_locations(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_locations_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(text='Second twitter post').pk
        data = {
            'first_value': ['England'],
            'second_value': [''],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_top_authors(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_authors_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': [''],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_authors(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_authors_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_locations(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_locations_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['USA'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_languages(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_languages_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['En'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_content_volume_top_authors(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.content_volume_top_authors_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': [''],
            'dates': ['2020-10-10T00:00:00Z', '2022-10-10T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_by_gender(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_by_gender_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['male'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_content_volume(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.content_volume_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': [''],
            'second_value': [''],
            'dates': ['2020-10-10T00:00:00Z', '2020-10-10T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': [''],
            'second_value': ['neutral'],
            'dates': ['2020-10-10T00:00:00Z', '2020-10-10T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_social_gender_volume(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.gender_volume_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['male'],
            'second_value': [''],
            'dates': ['2020-10-10T00:00:00Z', '2020-10-10T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_top_keywords(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_keywords_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['first'],
            'second_value': [''],
            'dates': ['2020-10-10T00:00:00Z', '2020-10-10T00:00:00Z'],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_top_keywords(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_keywords_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['first'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_sentiment_diagram(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_diagram_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['neutral'],
            'second_value': [],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_authors_by_location(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.authors_by_location_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': ['USA'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_authors_by_languages(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.authors_by_language_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': ['En'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_authors_by_sentiment(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.authors_by_sentiment_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': ['neutral'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

    def test_authors_by_gender(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.authors_by_gender_id
        url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk': pr.pk, 'widget_pk': widget_pk})
        post_id = TweetBinderPost.objects.all().get(user_name='First').pk
        data = {
            'first_value': ['First'],
            'second_value': ['male'],
            'dates': [],
            'posts_per_page': 10,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
