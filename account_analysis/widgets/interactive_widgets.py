from account_analysis.models import AccountAnalysisWidgetDescription
from account_analysis.models import ProjectAccountAnalysis
from django.core.paginator import Paginator
from django.http import JsonResponse
from .filter_for_posts import *
import json

def interactive_widgets(request, project_pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=project_pk)
    posts_account = posts_aggregator(project).filter(user_alias=project.profile_handle)
    posts_mentions = posts_aggregator(project).filter(text__icontains=f'@{project.profile_handle}')
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    body = json.loads(request.body)
    posts_per_page = body['posts_per_page']
    page_number = body['page_number']
    first_value = body['first_value']
    second_value = body['second_value']
    dates = body['dates']
    weekDays={'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    if widget.default_title == 'Profile timeline':
        posts = posts_account.filter(date__range=dates)
    elif widget.default_title == 'Most frequent post types':
        if first_value[0] == 'tweets':
            first_value=['original']
        elif first_value[0] == 'replies':
            first_value=['reply']
        elif first_value[0] == 'retweets':
            first_value=['retweet']
        posts = posts_account.filter(type__contains=first_value)
    elif widget.default_title == 'Most engaging post types':
        if first_value[0] == 'tweets':
            first_value=['original']
        elif first_value[0] == 'replies':
            first_value=['reply']
        elif first_value[0] == 'retweets':
            first_value=['retweet']
        posts = posts_account.filter(type__contains=first_value)
    elif widget.default_title == 'Most frequent media types':
        if first_value[0] == 'text':
            posts = posts_account.filter(count_textlength__gt=0)
        elif first_value[0] == 'video':
            posts = posts_account.filter(videos__isnull=False)
        elif first_value[0] == 'link':
            posts = posts_account.filter(count_links__gt=0)
        elif first_value[0] == 'photo':
            posts = posts_account.filter(count_images__gt=0)
        elif first_value[0] == 'combination':
            posts = posts_account.filter(
                                              (Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                              (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(videos__isnull=False) & Q(count_images__gt=0))
                                            )
    elif widget.default_title == 'Most engaging media types':
        if first_value[0] == 'text':
            posts = posts_account.filter(count_textlength__gt=0)
        elif first_value[0] == 'link':
            posts = posts_account.filter(count_links__gt=0)
        elif first_value[0] == 'video':
            posts = posts_account.filter(videos__isnull=False)
        elif first_value[0] == 'photo':
            posts = posts_account.filter(count_images__gt=0)
        elif first_value[0] == 'combination':
            posts = posts_account.filter(
                                              (Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                              (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(videos__isnull=False) & Q(count_images__gt=0))
                                            )
    elif widget.default_title == 'Mention timeline':
        posts = posts_mentions.filter(date__range=dates)
    elif widget.default_title == 'Most frequent mention media types':
        if first_value[0] == 'text':
            posts = posts_mentions.filter(count_textlength__gt=0)
        elif first_value[0] == 'link':
            posts = posts_mentions.filter(count_links__gt=0)
        elif first_value[0] == 'video':
            posts = posts_mentions.filter(videos__isnull=False)
        elif first_value[0] == 'photo':
            posts = posts_mentions.filter(count_images__gt=0)
        elif first_value[0] == 'combination':
            posts = posts_mentions.filter(
                                              (Q(count_links__gt=0) & Q(count_textlength__gt=0)) | 
                                              (Q(count_links__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_links__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(count_textlength__gt=0) & Q(videos__isnull=False)) | 
                                              (Q(count_textlength__gt=0) & Q(count_images__gt=0)) | 
                                              (Q(videos__isnull=False) & Q(count_images__gt=0))
                                            )
    elif widget.default_title == 'Optimal post length':
        posts = posts_account.filter(Q(count_textlength__gte=first_value[0]) & Q(count_textlength__lte=(first_value[1] if first_value[0] != '140' else 10000)))
    elif widget.default_title == 'Optimal post time':
        posts = posts_account.filter(date__week_day=weekDays[first_value[0]]).filter(date__hour=second_value[0])
    elif widget.default_title == 'Top hashtags':
        posts = posts_account.filter(hashtags__contains=first_value)
    elif widget.default_title == 'Optimal number of hashtags':
        if first_value[0] == '0 hashtags':
            posts = posts_account.filter(count_hashtags=0)
        elif first_value[0] == '1-2 hashtags':
            posts = posts_account.filter(Q(count_hashtags=1) | Q(count_hashtags=2))
        elif first_value[0] == '3-4 hashtags':
            posts = posts_account.filter(Q(count_hashtags=3) | Q(count_hashtags=4))
        elif first_value[0] == '5+ hashtags':
            posts = posts_account.filter(count_hashtags_gte=5) 
    elif widget.default_title == 'Mention sentiment':
        posts = posts_mentions.filter(sentiment=first_value[0].lower())
    elif widget.default_title == 'Average engagements by day':
        posts = posts_account.filter(date__week_day=weekDays[first_value[0]])
    elif widget.default_title == 'Average engagements by day (mentions)':
        posts = posts_mentions.filter(date__week_day=weekDays[first_value[0]])
    elif widget.default_title == 'Audience mention time':
        posts = posts_mentions.filter(date__week_day=weekDays[first_value[0]]).filter(date__hour=second_value[0])
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
