from django.utils.timezone import now
from project.models import Post
from datetime import timedelta
from django.db.models import Q
from functools import reduce
import json

class PreviewPosts:
    def get(self, request):
        keywords = request.GET.getlist('keywords')
        exclude = request.GET.getlist('exclude')
        additional = request.GET.getlist('additional')
        country = request.GET.getlist('country')
        language = request.GET.getlist('language')
        source = request.GET.getlist('source')
        author = request.GET.getlist('author')
        sentiment = request.GET.getlist('sentiment')
        posts = Post.objects.extra(where=["entry_published BETWEEN (NOW() - interval '2 days') AND NOW()"]).order_by('-entry_published')
        if additional:
            posts = self.additional_keywords_posts(posts, additional + keywords)
        else:
            posts = self.keywords_posts(keywords, posts)
        if exclude:
            posts = self.exclude_keywords_posts(posts, exclude)
        if source:
            posts = self.filter_posts([Q(feedlink__source1=source) for source in source], posts)
        if language:
            posts = self.filter_posts([Q(feed_language__language=language) for language in language], posts)
        if country:
            posts = self.filter_posts([Q(feedlink__country=country) for country in country], posts)
        if author:
            posts = self.filter_posts([Q(entry_author=author) for author in author], posts)
        if sentiment:
            posts = self.filter_posts([Q(sentiment=sentiment) for sentiment in sentiment], posts)
        
        return  {'posts': list(self.posts_values(posts[:20]))}
    
    def filter_posts(self, filter_list, posts):
        return posts.filter(reduce(lambda x, y: x | y, filter_list))

    def additional_keywords_posts(self, posts, additions):
        for word in additions:
            posts = posts.filter(entry_title__icontains=word)
        return posts

    def posts_values(self, posts):
        return posts.values(
            'id',
            'entry_title',
            'entry_published',
            'entry_summary',
            'entry_media_thumbnail_url',
            'entry_media_content_url',
            'feed_image_href',
            'feed_image_link',
            'feed_language__language',
            'entry_author', 'entry_links_href',
            'feedlink__country',
            'feedlink__source1',
            'feedlink__sourceurl',
            'feedlink__alexaglobalrank',
            'sentiment',
            'category',
        )

    def keywords_posts(self, keys, posts):
        keys = [f'%%{key.upper()}%%' for key in keys]
        posts = posts.extra(
            where=['UPPER(entry_title) LIKE ANY(%s) OR UPPER(entry_summary) LIKE ANY(%s)'],
            params=[keys, keys]
        )
        return posts

    def exclude_keywords_posts(self, posts, exceptions):
        to_be_removed = []
        for post in posts:
            for word in exceptions:
                if word in post.entry_title:
                    to_be_removed.append(post.id)
                    break
        posts = posts.exclude(id__in=to_be_removed)
        return posts
