from account_analysis.models import AccountAnalysisWidgetDescription
from account_analysis.models import ProjectAccountAnalysis
from django.core.paginator import Paginator
from django.http import JsonResponse
from .filter_for_posts import *
import json

def interactive_widgets(request, project_pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=project_pk)
    posts = posts_aggregator(project)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    posts_per_page = body['posts_per_page']
    page_number = body['page_number']
    first_value = body['first_value']
    second_value = body['second_value']
    dates = body['dates']
    if widget.default_title == 'Profile timeline':
        posts = posts.filter(date__range=dates)
    elif widget.default_title == 'Most frequent post types':
        if first_value[0] == 'tweets':
            first_value=['original']
        elif first_value[0] == 'replies':
            first_value=['reply']
        elif first_value[0] == 'retweets':
            first_value=['retweet']
        posts = posts.filter(type__contains=first_value)
    elif widget.default_title == 'Most engaging post types':
        if first_value[0] == 'tweets':
            first_value=['original']
        elif first_value[0] == 'replies':
            first_value=['reply']
        elif first_value[0] == 'retweets':
            first_value=['retweet']
        posts = posts.filter(type__contains=first_value)
    elif widget.default_title == 'Most frequent media types':
        if first_value[0] == 'text':
            posts = posts.filter(count_textlength__gt=0)
        elif first_value[0] == 'video':
            posts = posts.filter(videos__isnull=False)
        elif first_value[0] == 'link':
            posts = posts.filter(count_links__gt=0)
        elif first_value[0] == 'photo':
            posts = posts.filter(count_images__gt=0)
        elif first_value[0] == 'combination':
            posts = posts.filter(
                                              (Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                              (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(videos__isnull=False) & Q(count_images__gt=0))
                                            )
    elif widget.default_title == 'Most engaging media types':
        if first_value[0] == 'text':
            posts = posts.filter(count_textlength__gt=0)
        elif first_value[0] == 'link':
            posts = posts.filter(count_links__gt=0)
        elif first_value[0] == 'video':
            posts = posts.filter(videos__isnull=False)
        elif first_value[0] == 'photo':
            posts = posts.filter(count_images__gt=0)
        elif first_value[0] == 'combination':
            posts = posts.filter(
                                              (Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                              (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(videos__isnull=False) & Q(count_images__gt=0))
                                            )
    elif widget.default_title == 'Optimal post length':
        posts = posts.filter(Q(count_textlength__gte=first_value) & Q(count_textlength__lte=second_value))
    elif widget.default_title == 'Top hashtags':
        posts = posts.filter(reduce(lambda x,y: x | y, [Q(hashtags=hashtag) for hashtag in first_value]))
    posts = posts.values(
                          'id',
                          'post_id',
                          'user_name',
                          'user_alias',
                          'text',
                          'sentiment',
                          'date',
                          'locationString',
                          'language',
                          'count_favorites',
                          'count_totalretweets',
                          'count_replies',
                          'user_picture',
                          'images',
                        )
    p = Paginator(posts, posts_per_page)
    posts_list=list(p.page(page_number))
    res = { 'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list }
    return JsonResponse(res, safe = False)
