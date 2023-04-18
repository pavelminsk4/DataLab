from rest_framework.test import APITestCase
from project.expert_mode import Parser
from project.models import Post, Feedlinks, Speech
from datetime import datetime
from widgets.common_widget.filters_for_widgets import *


class TestParser(APITestCase):
  def setUp(self):
    flink1 = Feedlinks.objects.create(source1='one_source', country = 'England')
    flink2 = Feedlinks.objects.create(source1='two_source', country = 'USA')
    flink3 = Feedlinks.objects.create(source1='third_source', country = 'Greece')
    sp = Speech.objects.create(language='English')
    Post.objects.create(feedlink=flink1, entry_title='cat dog', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='cat cow bird', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='cat', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='bird', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='dog cow', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink1, entry_title='cat bear cow', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='bear bird wolf cat', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='dog wolf', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='bird', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='dog bird wolf', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])

  def test_can_parse_function(self):
    self.assertEqual(Parser("'cat' and (dog or 'bird')").can_parse(), True)
    self.assertEqual(Parser("dsfdsfsd").can_parse(), True)
    self.assertEqual(Parser("'cat' and ('dog' or 'bird cow')").can_parse(), True)
    # self.assertEqual(Parser("'cat' and ('dog' or 'bird cow:')").can_parse(), False)
    # self.assertEqual(Parser("'cat' and (source: or 'bird cow:')").can_parse(), False)
    self.assertEqual(Parser("'cat' and (source:wolf or 'bird cow')").can_parse(), True)
    # self.assertEqual(Parser("fsdf dsfs").can_parse(), False)
    self.assertEqual(Parser("").can_parse(), False)
    self.assertEqual(Parser(" ").can_parse(), False)
    # there should be more tests

  def test_simple_parse(self):
    posts = Post.objects.filter(Parser("'bird'").get_filter_query())
    self.assertEqual(posts.count(), 5)
    posts = Post.objects.filter(Parser("'bird' or 'dog'").get_filter_query())
    self.assertEqual(posts.count(), 8)
    posts = Post.objects.filter(Parser("'cat' and ('dog' or 'bird')").get_filter_query())
    self.assertEqual(posts.count(), 3)
    posts = Post.objects.filter(Parser("'cat' and ('dog' or 'bird') and not ('cow' or 'wolf')").get_filter_query())
    self.assertEqual(posts.count(), 1)
    self.assertEqual(posts.first().entry_title, 'cat dog')
    posts = Post.objects.filter(Parser("bird and source:'third_source'").get_filter_query())
    self.assertEqual(posts.count(), 3)
