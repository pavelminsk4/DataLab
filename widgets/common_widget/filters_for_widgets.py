from project.online_parser import OnlineParser
from project.models import Post
from django.db.models import Q
from functools import reduce


def keywords_posts(keys, posts):
    keys = [f'%%{key.upper()}%%' for key in keys]
    posts = posts.extra(
        where=['UPPER(entry_title) LIKE ANY(%s) OR UPPER(entry_summary) LIKE ANY(%s)'],
        params=[keys, keys]
    )
    return posts


def exclude_keywords_posts(posts, exceptions):
    to_be_removed = []
    for post in posts:
        for word in exceptions:
            if word in post.entry_title:
                to_be_removed.append(post.id)
                break
    posts = posts.exclude(id__in=to_be_removed)
    return posts


def additional_keywords_posts(posts, additions):
    for word in additions:
        posts = posts.filter(entry_title__icontains=word)
    return posts


def data_range_posts(start_date, end_date):
    interval = [start_date, end_date]
    posts = Post.objects.filter(entry_published__range=interval).order_by('entry_published')
    return posts


def source_filter_posts(source, posts):
    posts = posts.filter(feedlink__source1=source)
    return posts


def language_filter_posts(language, posts):
    posts = posts.filter(feed_language__language=language)
    return posts


def country_filter_posts(country, posts):
    posts = posts.filter(feedlink__country=country)
    return posts


def author_filter_posts(author, posts):
    posts = posts.filter(entry_author=author)
    return posts


def sentiment_filter_posts(sentiment, posts):
    posts = posts.filter(sentiment=sentiment)
    return posts


def author_dimensions_posts(authors, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in authors]))
    return posts


def language_dimensions_posts(languages, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feed_language__language=language) for language in languages]))
    return posts


def country_dimensions_posts(countries, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__country=country) for country in countries]))
    return posts


def source_dimensions_posts(sources, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__source1=source) for source in sources]))
    return posts


def sentiment_dimensions_posts(sentiments, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment.lower()) for sentiment in sentiments]))
    return posts


def posts_agregator(project):
    posts = data_range_posts(project.start_search_date, project.end_search_date)
    parser = OnlineParser(project.query_filter)
    if parser.can_parse() and project.expert_mode:
        return posts.filter(parser.get_filter_query())

    posts = keywords_posts(project.keywords, posts)
    if project.additional_keywords != []:
        posts = additional_keywords_posts(posts, project.additional_keywords)
    else:
        posts = keywords_posts(project.keywords, posts)
    if project.ignore_keywords != []:
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
    posts = posts_agregator(project)
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


def posts_with_filters(project, posts):
    interval = [project.start_search_date, project.end_search_date]
    posts = posts.filter(entry_published__range=interval).order_by('entry_published')
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
    if widget.author_dim_pivot:
        posts = author_dim_pivot(widget.author_dim_pivot, posts)
    if widget.country_dim_pivot:
        posts = country_dim_pivot(widget.country_dim_pivot, posts)
    if widget.source_dim_pivot:
        posts = source_dim_pivot(widget.source_dim_pivot, posts)
    if widget.language_dim_pivot:
        posts = language_dim_pivot(widget.language_dim_pivot, posts)
    if widget.sentiment_dim_pivot:
        posts = sentiment_dim_pivot(widget.sentiment_dim_pivot, posts)
    return posts.all()


def author_dim_pivot(authors, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in authors]))
    return posts


def language_dim_pivot(languages, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feed_language__language=language) for language in languages]))
    return posts


def country_dim_pivot(countries, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__country=country) for country in countries]))
    return posts


def source_dim_pivot(sources, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__source1=source) for source in sources]))
    return posts


def sentiment_dim_pivot(sentiments, posts):
    posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in sentiments]))
    return posts


def missing_authors_filter(posts):
    missing_authors = [None, '', 'null', 'None', 'Missing in source']
    return posts.exclude(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in missing_authors]))
