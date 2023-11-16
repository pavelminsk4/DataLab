from project_social.social_parser import SocialParser
from tweet_binder.models import TweetBinderPost
from django.db.models import Q
from functools import reduce


def keywords_posts(keys, posts):
    keys = [f'%%{key.upper()}%%' for key in keys]
    posts = posts.extra(where=[
        "UPPER(user_alias) LIKE ANY(%s) OR \
         UPPER(text) LIKE ANY(%s) OR \
         UPPER(user_name) LIKE ANY(%s)"],
        params=[keys, keys, keys]
    )
    return posts


def exclude_keywords_posts(posts, exceptions):
    to_be_removed = []
    for post in posts:
        for word in exceptions:
            if word in post.text:
                to_be_removed.append(post.id)
                break
    posts = posts.exclude(id__in=to_be_removed)
    return posts


def additional_keywords_posts(posts, additions):
    for word in additions:
        posts = posts.filter(text__icontains=word)
    return posts


def data_range_posts(start_date, end_date):
    interval = [start_date, end_date]
    posts = TweetBinderPost.objects.filter(date__range=interval)
    return posts


def source_filter_posts(sources, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(source=source) for source in sources]))
    return posts


def language_filter_posts(languages, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(language=language) for language in languages]))
    return posts


def country_filter_posts(countries, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(locationString=country) for country in countries]))
    return posts


def author_filter_posts(authors, posts):
    posts.filter(reduce(lambda x, y: x | y, [Q(user_name=author) for author in authors]))
    return posts


def sentiment_filter_posts(sentiments, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment.lower()) for sentiment in sentiments]))
    return posts


def author_dimensions_posts(authors, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_name=author) for author in authors]))
    return posts


def language_dimensions_posts(languages, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(language=language) for language in languages]))
    return posts


def country_dimensions_posts(countries, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(locationString=country) for country in countries]))
    return posts


def source_dimensions_posts(sources, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(source=source) for source in sources]))
    return posts


def sentiment_dimensions_posts(sentiments, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
    return posts


def posts_aggregator(project):
    posts = data_range_posts(project.start_search_date, project.end_search_date)
    parser = SocialParser(project.query_filter)
    if parser.can_parse() and project.expert_mode:
        return posts.filter(parser.get_filter_query())

    posts = keywords_posts(project.keywords, posts)
    if project.additional_keywords:
        posts = additional_keywords_posts(posts, project.additional_keywords)
    else:
        posts = keywords_posts(project.keywords, posts)
    if project.ignore_keywords:
        posts = exclude_keywords_posts(posts, project.ignore_keywords)
    if project.source_filter:
        posts = source_filter_posts(project.source_filter, posts)
    if project.language_filter:
        posts = language_filter_posts(project.language_filter, posts)
    if project.country_filter:
        posts = country_filter_posts(project.country_filter, posts)
    if project.author_filter:
        posts = author_filter_posts(project.author_filter, posts)
    if project.sentiment_filter:
        posts = sentiment_filter_posts(project.sentiment_filter, posts)
    return posts


def post_agregator_with_dimensions(project):
    posts = posts_aggregator(project)
    if project.author_dimensions:
        posts = author_dimensions_posts(project.author_dimensions, posts)
    if project.language_dimensions:
        posts = language_dimensions_posts(project.language_dimensions, posts)
    if project.country_dimensions:
        posts = country_dimensions_posts(project.country_dimensions, posts)
    if project.source_dimensions:
        posts = source_dimensions_posts(project.source_dimensions, posts)
    if project.sentiment_dimensions:
        posts = sentiment_dimensions_posts(project.sentiment_dimensions, posts)
    return posts


def post_agregetor_for_each_widget(widget, posts):
    if widget.author_dimensions:
        posts = author_dimensions(widget.author_dimensions, posts)
    if widget.language_dimensions:
        posts = language_dimensions(widget.language_dimensions, posts)
    if widget.country_dimensions:
        posts = country_dimensions(widget.country_dimensions, posts)
    if widget.source_dimensions:
        posts = source_dimensions(widget.source_dimensions, posts)
    if widget.sentiment_dimensions:
        posts = sentiment_dimensions(widget.sentiment_dimensions, posts)
    return posts


def author_dimensions(authors, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(user_name=author) for author in authors]))
    return posts


def language_dimensions(languages, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(language=language) for language in languages]))
    return posts


def country_dimensions(countries, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(locationString=country) for country in countries]))
    return posts


def source_dimensions(sources, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(source=source) for source in sources]))
    return posts


def sentiment_dimensions(sentiments, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
    return posts
