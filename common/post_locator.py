from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from talkwalker.models import TalkwalkerPost, TalkwalkerFeedlink
from common.factories.feedlinks import FeedlinksFactory
from common.factories.post import PostFactory
from project.models import Post, Feedlinks
import environ

env = environ.Env()

class PostLocator():

    def __init__(self):
        if env('POST_LOCATOR') == 'talkwalker':
            self.post = TalkwalkerPost
            self.feedlink = TalkwalkerFeedlink
        else:
            self.post = Post
            self.feedlink = Feedlinks
