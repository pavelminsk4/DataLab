import factory
from project.models import Post
from .speech import SpeechFactory
from .feedlinks import FeedlinksFactory

class PostFactory(factory.django.DjangoModelFactory):
  class Meta: 
    model = Post

  entry_title =     f"{factory.Faker('name')} post"
  feed_language =   factory.SubFactory(SpeechFactory)
  feedlink =        factory.SubFactory(FeedlinksFactory)
  entry_published = '2020-10-10T00:00:00+00:00'
  entry_author =    'Socrat'
  sentiment =       'neutral'
  entry_summary =   'post text'
  summary_vector =  []
