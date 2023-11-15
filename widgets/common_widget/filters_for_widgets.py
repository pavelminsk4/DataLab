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
    return posts.exclude(id__in=to_be_removed)

def additional_keywords_posts(posts, additions):
    for word in additions:
        posts = posts.filter(entry_title__icontains=word)
    return posts

def data_range_posts(start_date, end_date):
    interval = [start_date, end_date]
    posts = Post.objects.filter(entry_published__range=interval).order_by('entry_published')
    return posts

def posts_agregator(project):
    posts = project.posts
    parser = OnlineParser(project.query_filter)
    if parser.can_parse() and project.expert_mode:
        return posts.filter(parser.get_filter_query())

    if project.additional_keywords != []:
        posts = additional_keywords_posts(posts, project.additional_keywords)
    else:
        posts = keywords_posts(project.keywords, posts)
    if project.ignore_keywords != []:
        posts = exclude_keywords_posts(posts, project.ignore_keywords)
    return filter_project_posts(project, posts)

def filter_project_posts(project, posts):
    if project.source_filter:
        posts = filter_posts([Q(feedlink__source1=source) for source in project.source_filter], posts)
    if project.language_filter:
        posts = filter_posts([Q(feed_language__language=language) for language in project.language_filter], posts)
    if project.country_filter:
        posts = filter_posts([Q(feedlink__country=country) for country in project.country_filter], posts)
    if project.author_filter:
        posts = filter_posts([Q(entry_author=author) for author in project.author_filter], posts)
    if project.sentiment_filter:
        posts = filter_posts([Q(sentiment=sentiment) for sentiment in project.sentiment_filter], posts)
    return posts

def filter_posts(filter_list, posts):
    return posts.filter(reduce(lambda x, y: x | y, filter_list))

def post_agregator_with_dimensions(project):
    posts = posts_agregator(project)
    return filter_dimentions_posts(project, posts)
    
def filter_dimentions_posts(project, posts):
    if project.author_dimensions:
        posts = filter_posts([Q(entry_author=author) for author in project.author_dimensions], posts)
    if project.language_dimensions:
        posts = filter_posts([Q(feed_language__language=language) for language in project.language_dimensions], posts)
    if project.country_dimensions:
        posts = filter_posts([Q(feedlink__country=country) for country in project.country_dimensions], posts)
    if project.source_dimensions:
        posts = filter_posts([Q(feedlink__source1=source) for source in project.source_dimensions], posts)
    if project.sentiment_dimensions:
        posts = filter_posts([Q(sentiment=sentiment) for sentiment in project.sentiment_dimensions], posts)
    return posts

def posts_with_filters(project, posts):
    interval = [project.start_search_date, project.end_search_date]
    posts = posts.filter(entry_published__range=interval).order_by('entry_published')
    posts = filter_project_posts(project, posts)
    return filter_dimentions_posts(project, posts)

def post_agregetor_for_each_widget(widget, posts):
    if widget.author_dim_pivot:
        posts = filter_posts([Q(entry_author=author) for author in widget.author_dim_pivot], posts)
    if widget.country_dim_pivot:
        posts = filter_posts([Q(feedlink__country=country) for country in widget.country_dim_pivot], posts)
    if widget.source_dim_pivot:
        posts = filter_posts([Q(feedlink__source1=source) for source in widget.source_dim_pivot], posts)
    if widget.language_dim_pivot:
        posts = filter_posts([Q(feed_language__language=language) for language in widget.language_dim_pivot], posts)
    if widget.sentiment_dim_pivot:
        posts = filter_posts([Q(sentiment=sentiment) for sentiment in widget.sentiment_dim_pivot], posts)
    return posts.all()

def missing_authors_filter(posts):
    missing_authors = [None, '', 'null', 'None', 'Missing in source']
    return posts.exclude(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in missing_authors]))
