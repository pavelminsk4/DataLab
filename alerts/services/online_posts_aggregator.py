from django.shortcuts import get_object_or_404
from project.models import Project, Post
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
        posts = posts.filter(entry_title__contains=word)
    return posts


def posts_aggregator(project_id, start_date=None, end_date=None):
    project  = get_object_or_404(Project, pk=project_id)

    interval = [start_date, end_date] if start_date else [project.start_search_date, project.end_search_date]
    posts    = Post.objects.filter(entry_published__range=interval)
    posts    = keywords_posts(project.keywords, posts)

    if project.additional_keywords and project.additional_keywords != []:
        posts = additional_keywords_posts(posts, project.additional_keywords)
    if project.ignore_keywords and project.ignore_keywords != []:
        posts = exclude_keywords_posts(posts, project.ignore_keywords)
    if project.country_filter is not None:
        posts = posts.filter(feedlink__country=project.country_filter)
    if project.language_filter is not None:
        posts = posts.filter(feed_language__language=project.language_filter)
    if project.source_filter is not None:
        posts = posts.filter(feedlink__source1=project.source_filter)
    if project.author_filter is not None:
        posts = posts.filter(entry_author=project.author_filter)
    if project.sentiment_filter is not None:
        posts = posts.filter(sentiment=project.sentiment_filter)

    return posts
