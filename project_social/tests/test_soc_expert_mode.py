from rest_framework.test import APITestCase
from project_social.social_parser import SocialParser
from common.factories.tweet_binder_post import TweetBinderPostFactory
from tweet_binder.models import TweetBinderPost

class TestParser(APITestCase):
  def setUp(self):
    TweetBinderPostFactory(text='bird', sentiment='positive')
    TweetBinderPostFactory(text='bird dog', sentiment='negative')
    TweetBinderPostFactory(text='dog cat', sentiment='positive')
    TweetBinderPostFactory(text='bird', locationString='Scotland')
    TweetBinderPostFactory(text='wolf cat bear', locationString='Scotland')
    TweetBinderPostFactory(text='cat fish', sentiment='positive')
    TweetBinderPostFactory(text='wolf', sentiment='positive')
    TweetBinderPostFactory(text='cat bear cow', user_followers=100)
    TweetBinderPostFactory(text='bear bird wolf cat', user_followers=200)
    TweetBinderPostFactory(text='dog bird wolf', user_followers=200)

  def test_simple_parse(self):
    posts = TweetBinderPost.objects.filter(SocialParser('bird').get_filter_query())
    self.assertEqual(posts.count(), 5)
    posts = TweetBinderPost.objects.filter(SocialParser('bird or dog').get_filter_query())
    self.assertEqual(posts.count(), 6)
    posts = TweetBinderPost.objects.filter(SocialParser('bird and not location:Scotland').get_filter_query())
    self.assertEqual(posts.count(), 4)
    posts = TweetBinderPost.objects.filter(SocialParser('(bird or wolf) and sentiment:positive').get_filter_query())
    self.assertEqual(posts.count(), 2)
    posts = TweetBinderPost.objects.filter(SocialParser('(cow or wolf) and followers: >150').get_filter_query())
    self.assertEqual(posts.count(), 2)
    posts = TweetBinderPost.objects.filter(SocialParser('(cow or wolf) and followers: =100').get_filter_query())
    self.assertEqual(posts.count(), 1)
