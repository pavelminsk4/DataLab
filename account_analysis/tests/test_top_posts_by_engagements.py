from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopPostsByEngagementsWidgetTests(APITestCase):

    def test_response_list(self):
        tw_1 = TweetBinderPostFactory(type=['original', 'reply', 'retweet'])
        tw_2 = TweetBinderPostFactory(type=['original', 'reply'], text = 'Second twitter post')
        tw_3 = TweetBinderPostFactory(text = 'Third twitter post')
        tw_4 = TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', type=['original', 'reply', 'retweet'], text = 'Fourth twitter post')
        AccountAnalysisProjectFactory()
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.top_posts_by_engagements_id
        url = reverse('account_analysis:top_posts_by_engagements', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
                {'id': str(tw_4.post_id), 'alias': 'First_name', 'type': 'retweet', 'text': 'Fourth twitter post', 'sentiment': 'neutral', 'engagements': 4, 'engmt_rate': 4.00, 'date': 'Oct 10, 2020 12:00 AM'},
                {'id': str(tw_1.post_id), 'alias': 'First_name', 'type': 'retweet', 'text': 'First twitter post', 'sentiment': 'neutral', 'engagements': 2, 'engmt_rate': 2.00, 'date': 'Oct 10, 2020 12:00 AM'},
                {'id': str(tw_2.post_id), 'alias': 'First_name', 'type': 'reply', 'text': 'Second twitter post', 'sentiment': 'neutral', 'engagements': 2, 'engmt_rate': 2.00, 'date': 'Oct 10, 2020 12:00 AM'},
                {'id': str(tw_3.post_id), 'alias': 'First_name', 'type': 'text', 'text': 'Third twitter post', 'sentiment': 'neutral', 'engagements': 2, 'engmt_rate': 2.00, 'date': 'Oct 10, 2020 12:00 AM'}
              ]
        self.assertEqual(json.loads(response.content), res)
