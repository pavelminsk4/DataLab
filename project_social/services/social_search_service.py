from expert_filters.services.social_expert_presets import SocialExpertPresets
from project_social.models import ChangingTweetbinderSentiment
from common.utils.change_sentiment import ChangeSentiment
from project_social.social_parser import SocialParser
from project_social.models import ProjectSocial
from tweet_binder.models import TweetBinderPost

from django.core.paginator import Paginator
from functools import reduce
from django.db.models import Q
import json


class SocialSearchService:
    def keywords_posts(self, keys, posts):
        keys = [f'%%{key.upper()}%%' for key in keys]
        posts = posts.extra(where=[
            "UPPER(user_alias) LIKE ANY(%s) OR \
            UPPER(text) LIKE ANY(%s) OR \
            UPPER(user_name) LIKE ANY(%s)"],
            params=[keys, keys, keys]
        )
        return posts

    def additional_keywords_posts(self, posts, additions):
        keys = [f'%%{key.upper()}%%' for key in additions]
        posts = posts.extra(where=[
            "UPPER(user_alias) LIKE ALL(%s) OR \
            UPPER(text) LIKE ALL(%s) OR \
            UPPER(user_name) LIKE ALL(%s)"],
            params=[keys, keys, keys]
        )
        return posts

    def exclude_keywords_posts(self, posts, exceptions):
        keys = [f'%%{key.upper()}%%' for key in exceptions]
        posts = posts.extra(where=[
            "UPPER(user_alias) NOT LIKE ALL(%s) OR \
            UPPER(text) NOT LIKE ALL(%s) OR \
            UPPER(user_name) LIKE ALL(%s)"],
            params=[keys, keys, keys]
        )
        return posts

    def filter_with_constructor(self, posts, body):
        keys = body.get('keywords', [])
        exceptions = body.get('exceptions', [])
        additions = body.get('additions', [])
        country = body.get('country', [])
        language = body.get('language', [])
        source = body.get('source', [])
        author = body.get('author', [])
        sentiment = body.get('sentiment', [])
        posts = self.keywords_posts(keys, posts)
        if additions:
            posts = self.additional_keywords_posts(posts, additions)
        if exceptions:
            posts = self.exclude_keywords_posts(posts, exceptions)
        if country:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(country=c) for c in country]))
        if language:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(language=lan) for lan in language]))
        if source:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(source=s) for s in source]))
        if author:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_name=a) for a in author]))
        if sentiment:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sen) for sen in sentiment]))
        return posts

    def filter_with_dimensions(self, posts, body):
        country_dimensions = body.get('country_dimensions', [])
        language_dimensions = body.get('language_dimensions', [])
        source_dimensions = body.get('source_dimensions', [])
        author_dimensions = body.get('author_dimensions', [])
        sentiment_dimensions = body.get('sentiment_dimensions', [])
        if country_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(country=country) for country in country_dimensions]))
        if language_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(language=language) for language in language_dimensions]))
        if source_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(source=source) for source in source_dimensions]))
        if author_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_name=author) for author in author_dimensions]))
        if sentiment_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in sentiment_dimensions]))
        return posts

    def data_range_posts(self, start_date, end_date):
        interval = [start_date, end_date]
        posts = TweetBinderPost.objects.filter(date__range=interval)
        return posts

    def posts_values(self, posts):
        return posts.values(
            'id',
            'post_id',
            'user_name',
            'user_alias',
            'text',
            'sentiment',
            'date',
            'country',
            'language',
            'count_favorites',
            'count_totalretweets',
            'count_replies',
            'user_picture',
            'images',
            'count_tweetvalue'
        )

    def execute(self, request):
        body = json.loads(request.body)
        date_range = body.get('date_range')
        posts_per_page = body.get('posts_per_page')
        page_number = body.get('page_number')
        sort_posts = body.get('sort_posts')
        department_id = request.user.user_profile.department
        project = ProjectSocial.objects.get(id=body.get('project_pk'))

        posts = self.data_range_posts(date_range[0], date_range[1]).order_by('-creation_date')
        parser = SocialParser(body.get('query_filter'))
        expert_mode = parser.can_parse() and body['expert_mode']
        posts = posts.filter(parser.get_filter_query()) if expert_mode else self.filter_with_constructor(posts, body)

        if project.expert_presets != []:
            posts = SocialExpertPresets().apply_presets(project, posts)

        if sort_posts == 'potential_reach':
            posts = posts.order_by('-count_tweetvalue')
        elif sort_posts == 'potential_reach_desc':
            posts = posts.order_by('count_tweetvalue')
        else:
            posts = posts.order_by('-creation_date')
        
        posts               = self.filter_with_dimensions(posts, body)
        posts               = self.posts_values(posts)
        p                   = Paginator(posts, posts_per_page)
        posts_list          = list(p.page(page_number))
        posts_list          = ChangeSentiment(department_id, posts_list, ChangingTweetbinderSentiment).execute()
        for post in posts_list:
            post['link'] = f'https://twitter.com/user/status/{post["post_id"]}'

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
