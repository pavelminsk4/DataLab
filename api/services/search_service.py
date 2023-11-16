from django.core.paginator import Paginator
from widgets.common_widget.filters_for_widgets import posts_with_filters, data_range_posts
from project.online_parser import OnlineParser
from project.models import Project, ChangingOnlineSentiment
import json


class SearchService:
    def execute(self, request):
        body           = json.loads(request.body)
        department_id  = request.user.user_profile.department
        date_range     = body['date_range']
        posts_per_page = body['posts_per_page']
        page_number    = body['page_number']
        sort_posts     = body['sort_posts']
        query_filter   = body['query_filter']

        from api.views.users import filter_with_constructor, posts_values, filter_with_dimensions, change_post_sentiment

        if 'project_pk' in body:
            project = Project.objects.get(id=body['project_pk'])
            posts = project.posts
            posts = posts_with_filters(project, posts)
        else:
            posts = data_range_posts(date_range[0], date_range[1])
            parser = OnlineParser(query_filter)
            expert_mode = parser.can_parse() & body['expert_mode']
            posts = posts.filter(parser.get_filter_query()) if expert_mode else filter_with_constructor(body, posts)
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
        elif sort_posts == 'date':
            posts = posts.order_by('entry_published')

        posts               = posts_values(posts)
        p                   = Paginator(posts, posts_per_page)
        posts_list          = list(p.page(page_number))
        department_changing = ChangingOnlineSentiment.objects.filter(department_id=department_id).values()
        dict_changing       = {x['post_id']: x['sentiment'] for x in department_changing}

        for post in posts_list:
            post = change_post_sentiment(post, dict_changing)

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
