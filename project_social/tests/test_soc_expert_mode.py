from rest_framework.test import APITestCase
from project_social.social_parser import SocialParser
from .factories.tweet_binder_post import TweetBinderPostFactory
from tweet_binder.models import TweetBinderPost

class TestParser(APITestCase):
  def setUp(self):
    TweetBinderPostFactory(post_id=0, text='bird', sentiment='positive')
    TweetBinderPostFactory(post_id=1, text='bird dog', sentiment='negative')
    TweetBinderPostFactory(post_id=2, text='dog cat', sentiment='positive')
    TweetBinderPostFactory(post_id=3, text='bird', locationString='Scotland')
    TweetBinderPostFactory(post_id=4, text='wolf cat bear', locationString='Scotland')
    TweetBinderPostFactory(post_id=5, text='cat fish', sentiment='positive')
    TweetBinderPostFactory(post_id=6, text='wolf', sentiment='positive')
    TweetBinderPostFactory(post_id=7, text='cat bear cow', user_followers=100)
    TweetBinderPostFactory(post_id=8, text='bear bird wolf cat', user_followers=200)
    TweetBinderPostFactory(post_id=9, text='dog bird wolf', user_followers=200)

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
