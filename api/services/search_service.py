from expert_filters.services.expert_presets import ExpertPresets
from project.models import Project
from django.core.paginator import Paginator
import json

from django.db.models import Q
from functools import reduce
from common.utils.change_sentiment import ChangeSentiment

class SearchService:
    def execute(self, request):
        body           = json.loads(request.body)
        department_id  = request.user.user_profile.department
        posts_per_page = body.get('posts_per_page', 20)
        page_number    = body.get('page_number', 1)
        sort_posts     = body.get('sort_posts', [])

        from api.views.users import posts_values

        project = Project.objects.get(id=body['project_pk'])
        posts = project.posts.exclude(projectpost__exclude=True)

        if project.expert_presets.exists():
            posts = ExpertPresets(project, posts).posts
        else:
            if 'date_range' in body:
                posts = posts.filter(entry_published__range=(body['date_range'][0], body['date_range'][1]))

            posts = default_filter(project, posts)
            posts = default_filter_dimensions(project, posts)

        if sort_posts == 'source':
            posts = posts.order_by('feedlink__source1')
        elif sort_posts == 'country':
            posts = posts.order_by('feedlink__country')
        elif sort_posts == 'language':
            posts = posts.order_by('feed_language__language')
        elif sort_posts == 'potential_reach_desc':
            posts = posts.order_by('-feedlink__alexaglobalrank')
        elif sort_posts == 'potential_reach':
            posts = posts.order_by('feedlink__alexaglobalrank')
        elif sort_posts == 'date_desc':
            posts = posts.order_by('-entry_published')
        else:
            posts = posts.order_by('entry_published')

        posts               = posts_values(posts)
        p                   = Paginator(posts, posts_per_page)
        posts_list          = list(p.page(page_number))
        posts_list          = ChangeSentiment(department_id, posts_list).execute()

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}

def default_filter(project, posts):
    if project.country_filter:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__country=country) for country in project.country_filter]))
    if project.language_filter:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feed_language__language=lang) for lang in project.language_filter]))
    if project.source_filter:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__source1=source) for source in project.source_filter]))
    if project.author_filter:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in project.author_filter]))
    if project.sentiment_filter:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in project.sentiment_filter]))

    return posts

def default_filter_dimensions(project, posts):
    if project.country_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__country=country) for country in project.country_dimensions]))
    if project.language_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feed_language__language=lang) for lang in project.language_dimensions]))
    if project.source_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(feedlink__source1=source) for source in project.source_dimensions]))
    if project.author_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(entry_author=author) for author in project.author_dimensions]))
    if project.sentiment_dimensions:
        posts = posts.filter(reduce(lambda x, y: x | y, [Q(sentiment=sentiment) for sentiment in project.sentiment_dimensions]))

    return posts
