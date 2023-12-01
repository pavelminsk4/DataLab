from django.core.paginator import Paginator
from project.online_parser import OnlineParser
from project.models import Project, ChangingOnlineSentiment
from expert_filters.services.expert_presets import ExpertPresets
import json


class SearchService:
    def execute(self, request):
        body           = json.loads(request.body)
        department_id  = request.user.user_profile.department
        posts_per_page = body['posts_per_page']
        page_number    = body['page_number']
        sort_posts     = body['sort_posts']

        from api.views.users import default_filter, filter_with_constructor, posts_values, filter_with_dimensions, change_post_sentiment

        project = Project.objects.get(id=body['project_pk'])
        posts = project.posts

        if project.expert_presets.exists():
            posts = ExpertPresets(project, posts).posts
        else:
            if 'date_range' in body:
                posts = posts.filter(entry_published__range=(body['date_range'][0], body['date_range'][1]))

            posts = default_filter(project, posts)
            posts = filter_with_constructor(body, posts)
            posts = filter_with_dimensions(posts, body)

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
        department_changing = ChangingOnlineSentiment.objects.filter(department_id=department_id).values()
        dict_changing       = {x['post_id']: x['sentiment'] for x in department_changing}

        for post in posts_list:
            post = change_post_sentiment(post, dict_changing)

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
