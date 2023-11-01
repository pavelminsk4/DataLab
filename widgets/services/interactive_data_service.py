from django.core.paginator import Paginator
from widgets.common_widget.filters_for_widgets import *
from widgets.models import WidgetDescription
from project.models import Project
import json


class InteractiveDataService:
    def execute(self, request, project_pk, widget_pk):
        project = Project.objects.get(id=project_pk)
        widget = WidgetDescription.objects.get(id=widget_pk)
        posts = post_agregator_with_dimensions(project)
        body = json.loads(request.body)
        posts_per_page = body['posts_per_page']
        page_number = body['page_number']
        first_value = body['first_value']
        second_value = body['second_value']
        dates = body['dates']
        if widget.default_title == 'Top languages':
            posts = language_dimensions_posts(first_value, posts)
        elif widget.default_title == 'Top sources':
            posts = source_dimensions_posts(first_value, posts)
        elif widget.default_title == 'Top countries':
            posts = country_dimensions_posts(first_value, posts)
        elif widget.default_title == 'Top authors':
            posts = author_dimensions_posts(first_value, posts)
        elif widget.default_title == 'Sentiment top sources':
            posts = source_dimensions_posts(first_value, sentiment_dimensions_posts(second_value, posts))
        elif widget.default_title == 'Sentiment top countries':
            posts = country_dimensions_posts(first_value, sentiment_dimensions_posts(second_value, posts))
        elif widget.default_title == 'Sentiment top authors':
            posts = author_dimensions_posts(first_value, sentiment_dimensions_posts(second_value, posts))
        elif widget.default_title == 'Sentiment top languages':
            posts = language_dimensions_posts(first_value, sentiment_dimensions_posts(second_value, posts))
        elif widget.default_title == 'Content Volume by authors':
            posts = author_dimensions_posts(first_value, posts).filter(entry_published__range=dates)
        elif widget.default_title == 'Content Volume by countries':
            posts = country_dimensions_posts(first_value, posts).filter(entry_published__range=dates)
        elif widget.default_title == 'Content Volume by top sources':
            posts = source_dimensions_posts(first_value, posts).filter(entry_published__range=dates)
        elif widget.default_title == 'Sentiment for period':
            posts = posts.filter(sentiment=first_value[0].lower()).filter(entry_published__range=dates)
        elif widget.default_title == 'Content volume':
            posts = posts.filter(entry_published__range=dates)
        elif widget.default_title == 'Top keywords':
            posts = posts.filter(entry_summary__icontains=first_value[0])
        elif widget.default_title == 'Sentiment top keywords':
            posts = sentiment_dimensions_posts(second_value, posts).filter(entry_summary__icontains=first_value[0])
        elif widget.default_title == 'Sentiment diagram':
            posts = posts.filter(sentiment=first_value[0].lower())
        elif widget.default_title == 'Authors by country':
            posts = country_dimensions_posts(second_value, posts).filter(entry_author=first_value[0])
        elif widget.default_title == 'Authors by language':
            posts = language_dimensions_posts(second_value, posts).filter(entry_author=first_value[0])
        elif widget.default_title == 'Authors by sentiment':
            posts = posts.filter(sentiment=second_value[0].lower()).filter(entry_author=first_value[0])
        elif widget.default_title == 'Sources by country':
            posts = country_dimensions_posts(second_value, posts).filter(feedlink__source1=first_value[0])
        elif widget.default_title == 'Sources by language':
            posts = language_dimensions_posts(second_value, posts).filter(feedlink__source1=first_value[0])
        elif widget.default_title == 'Overall top authors':
            posts = posts.filter(sentiment=second_value[0].lower(), entry_author=first_value[0])
        elif widget.default_title == 'Overall top sources':
            posts = posts.filter(sentiment=second_value[0].lower(), feedlink__source1=first_value[0])
        elif widget.default_title == 'Top sharing sources':
            posts = posts.filter(sentiment=second_value[0].lower(), feedlink__source1=first_value[0])
        elif widget.default_title == 'Top keywords by country':
            posts = posts.filter(entry_summary__icontains=first_value[0])
        elif widget.default_title == 'Top languages by country':
            posts = posts.filter(feed_language__language=second_value[0], feedlink__country=first_value[0])
        posts = posts.order_by('id').values(
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
            )
        p = Paginator(posts, posts_per_page)
        posts_list=list(p.page(page_number))
        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}