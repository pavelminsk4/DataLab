from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.speech import SpeechFactory
from project.online_parser import OnlineParser
from talkwalker.models import TalkwalkerPost
from rest_framework.test import APITestCase
from project.models import Post
import os


class TestParser(APITestCase):
  
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        flink1 = FeedlinksFactory(source1='one_source', country = 'England')
        flink2 = FeedlinksFactory(source1='two_source', country = 'USA')
        flink3 = FeedlinksFactory(source1='third_source', country = 'Greece')
        sp = SpeechFactory(language='English')
        PostFactory(entry_title='cat dog', feed_language=sp, feedlink=flink1)
        PostFactory(entry_title='cat cow bird', feed_language=sp, feedlink=flink2)
        PostFactory(entry_title='cat', feed_language=sp, feedlink=flink2)
        PostFactory(entry_title='bird', feed_language=sp, feedlink=flink3)
        PostFactory(entry_title='dog cow', feed_language=sp, feedlink=flink3)
        PostFactory(entry_title='cat bear cow', feed_language=sp, feedlink=flink1)
        PostFactory(entry_title='bear bird wolf cat', feed_language=sp, feedlink=flink2)
        PostFactory(entry_title='dog wolf', feed_language=sp, feedlink=flink2)
        PostFactory(entry_title='bird 2', feed_language=sp, feedlink=flink3)
        PostFactory(entry_title='dog bird wolf', feed_language=sp, feedlink=flink3)

    def test_can_parse_function(self):
        self.assertEqual(OnlineParser("'cat' and (dog or 'bird')").can_parse(), True)
        self.assertEqual(OnlineParser("dsfdsfsd").can_parse(), True)
        self.assertEqual(OnlineParser("'cat' and ('dog' or 'bird cow')").can_parse(), True)
        self.assertEqual(OnlineParser("'cat' and (source:wolf or 'bird cow')").can_parse(), True)
        self.assertEqual(OnlineParser("").can_parse(), False)
        self.assertEqual(OnlineParser(" ").can_parse(), False)

    def test_simple_parse(self):
        posts = Post.objects.filter(OnlineParser("'bird'").get_filter_query())
        self.assertEqual(posts.count(), 5)
        posts = Post.objects.filter(OnlineParser("'bird' or 'dog'").get_filter_query())
        self.assertEqual(posts.count(), 8)
        posts = Post.objects.filter(OnlineParser("'cat' and ('dog' or 'bird')").get_filter_query())
        self.assertEqual(posts.count(), 3)
        posts = Post.objects.filter(OnlineParser("'cat' and ('dog' or 'bird') and not ('cow' or 'wolf')").get_filter_query())
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first().entry_title, 'cat dog')
        posts = Post.objects.filter(OnlineParser("bird and source:'third_source'").get_filter_query())
        self.assertEqual(posts.count(), 3)
        posts = Post.objects.filter(OnlineParser("bird and source:third_source").get_filter_query())
        self.assertEqual(posts.count(), 3)


class TestParserTLW(APITestCase):
    
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        flink1 = TalkwalkerFeedlinksFactory(source1='one_source', country = 'England')
        flink2 = TalkwalkerFeedlinksFactory(source1='two_source', country = 'USA')
        flink3 = TalkwalkerFeedlinksFactory(source1='third_source', country = 'Greece')
        sp = SpeechFactory(language='English')
        TalkwalkerPostFactory(entry_title='cat dog', feed_language=sp, feedlink=flink1)
        TalkwalkerPostFactory(entry_title='cat cow bird', feed_language=sp, feedlink=flink2)
        TalkwalkerPostFactory(entry_title='cat', feed_language=sp, feedlink=flink2)
        TalkwalkerPostFactory(entry_title='bird', feed_language=sp, feedlink=flink3)
        TalkwalkerPostFactory(entry_title='dog cow', feed_language=sp, feedlink=flink3)
        TalkwalkerPostFactory(entry_title='cat bear cow', feed_language=sp, feedlink=flink1)
        TalkwalkerPostFactory(entry_title='bear bird wolf cat', feed_language=sp, feedlink=flink2)
        TalkwalkerPostFactory(entry_title='dog wolf', feed_language=sp, feedlink=flink2)
        TalkwalkerPostFactory(entry_title='bird 2', feed_language=sp, feedlink=flink3)
        TalkwalkerPostFactory(entry_title='dog bird wolf', feed_language=sp, feedlink=flink3)

    def test_can_parse_function_tlw(self):
        self.assertEqual(OnlineParser("'cat' and (dog or 'bird')").can_parse(), True)
        self.assertEqual(OnlineParser("dsfdsfsd").can_parse(), True)
        self.assertEqual(OnlineParser("'cat' and ('dog' or 'bird cow')").can_parse(), True)
        self.assertEqual(OnlineParser("'cat' and (source:wolf or 'bird cow')").can_parse(), True)
        self.assertEqual(OnlineParser("").can_parse(), False)
        self.assertEqual(OnlineParser(" ").can_parse(), False)

    def test_simple_parse_tlw(self):
        posts = TalkwalkerPost.objects.filter(OnlineParser("'bird'").get_filter_query())
        self.assertEqual(posts.count(), 5)
        posts = TalkwalkerPost.objects.filter(OnlineParser("'bird' or 'dog'").get_filter_query())
        self.assertEqual(posts.count(), 8)
        posts = TalkwalkerPost.objects.filter(OnlineParser("'cat' and ('dog' or 'bird')").get_filter_query())
        self.assertEqual(posts.count(), 3)
        posts = TalkwalkerPost.objects.filter(OnlineParser("'cat' and ('dog' or 'bird') and not ('cow' or 'wolf')").get_filter_query())
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first().entry_title, 'cat dog')
        posts = TalkwalkerPost.objects.filter(OnlineParser("bird and source:'third_source'").get_filter_query())
        self.assertEqual(posts.count(), 3)
        posts = TalkwalkerPost.objects.filter(OnlineParser("bird and source:third_source").get_filter_query())
        self.assertEqual(posts.count(), 3)
