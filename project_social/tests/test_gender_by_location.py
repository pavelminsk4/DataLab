from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class GenderByLocationTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(user_gender='male', locationString='USA')
        TweetBinderPostFactory(user_gender='male', locationString='England')
        TweetBinderPostFactory(user_gender='female', locationString='England')
        TweetBinderPostFactory(user_gender='undefined', locationString='England')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.gender_by_location_id
        url = reverse('project_social:social_gender_by_location', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'England': {'male': 1, 'female': 1, 'undefined': 1}, 
                'USA': {'male': 1, 'female': 0, 'undefined': 0}
            }
        self.assertEqual(json.loads(response.content), res)
