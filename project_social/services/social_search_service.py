from expert_filters.services.social_expert_presets import SocialExpertPresets
from project_social.social_parser import SocialParser
from project_social.models import ProjectSocial
from project_social.models import ChangingTweetbinderSentiment
from tweet_binder.models import TweetBinderPost

from django.core.paginator import Paginator
from functools import reduce
from django.db.models import Q
import json


class SocialSearchService:
    def change_tweet_post_sentiment(self, post, dict_changing):
        if post['id'] in dict_changing:
            new_sentiment = dict_changing[post['id']]
            post['sentiment'] = new_sentiment
        return post
    
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
        keys = body['keywords']
        exceptions = body['exceptions']
        additions = body['additions']
        country = body['country']
        language = body['language']
        source = body['source']
        author = body['author']
        sentiment = body['sentiment']
        posts = self.keywords_posts(keys, posts)
        if additions:
            posts = self.additional_keywords_posts(posts, additions)
        if exceptions:
            posts = self.exclude_keywords_posts(posts, exceptions)
        if country:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_location=c) for c in country]))
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
        country_dimensions = body['country_dimensions']
        language_dimensions = body['language_dimensions']
        source_dimensions = body['source_dimensions']
        author_dimensions = body['author_dimensions']
        sentiment_dimensions = body['sentiment_dimensions']
        if country_dimensions:
            posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_location=country) for country in country_dimensions]))
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
            'user_location',
            'language',
            'count_favorites',
            'count_totalretweets',
            'count_replies',
            'user_picture',
            'images'
        )

    def execute(self, request):
        body = json.loads(request.body)
        date_range = body['date_range']
        posts_per_page = body['posts_per_page']
        page_number = body['page_number']
        department_id = request.user.user_profile.department
        project = ProjectSocial.objects.get(id=body['project_pk'])

        posts = self.data_range_posts(date_range[0], date_range[1]).order_by('-creation_date')
        parser = SocialParser(body['query_filter'])
        expert_mode = parser.can_parse() and body['expert_mode']
        posts = posts.filter(parser.get_filter_query()) if expert_mode else self.filter_with_constructor(posts, body)

        if project.expert_presets != []:
            posts = SocialExpertPresets().apply_presets(project, posts)

        posts               = self.filter_with_dimensions(posts, body)
        posts               = self.posts_values(posts)
        p                   = Paginator(posts, posts_per_page)
        posts_list          = list(p.page(page_number))
        department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=department_id).values()
        dict_changing       = {x['tweet_post_id']: x['sentiment'] for x in department_changing}

        for post in posts_list:
            post['link'] = f'https://twitter.com/user/status/{post["post_id"]}'
            post = self.change_tweet_post_sentiment(post, dict_changing)

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
