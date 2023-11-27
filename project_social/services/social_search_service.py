
from django.core.paginator import Paginator
import json

from expert_filters.services.social_expert_presets import SocialExpertPresets
from project_social.social_parser import SocialParser
from project_social.models import ProjectSocial
from project_social.models import ChangingTweetbinderSentiment
from project_social.views import change_tweet_post_sentiment
from project_social.views import filter_with_constructor
from project_social.views import filter_with_dimensions
from project_social.views import data_range_posts
from project_social.views import posts_values


class SocialSearchService:
    def execute(self, request):
        body = json.loads(request.body)
        date_range = body['date_range']
        posts_per_page = body['posts_per_page']
        page_number = body['page_number']
        #project = ProjectSocial.objects.get(id=body['project_pk'])
        department_id = request.user.user_profile.department

        posts = data_range_posts(date_range[0], date_range[1]).order_by('-creation_date')
        parser = SocialParser(body['query_filter'])
        expert_mode = parser.can_parse() and body['expert_mode']
        posts = posts.filter(parser.get_filter_query()) if expert_mode else filter_with_constructor(posts, body)

        #if project.expert_presets != []:
        #    posts = SocialExpertPresets.apply_presets(project)

        posts               = filter_with_dimensions(posts, body)
        posts               = posts_values(posts)
        p                   = Paginator(posts, posts_per_page)
        posts_list          = list(p.page(page_number))
        department_changing = ChangingTweetbinderSentiment.objects.filter(department_id=department_id).values()
        dict_changing       = {x['tweet_post_id']: x['sentiment'] for x in department_changing}

        for post in posts_list:
            post['link'] = f'https://twitter.com/user/status/{post["post_id"]}'
            post = change_tweet_post_sentiment(post, dict_changing)

        return {'num_pages': p.num_pages, 'num_posts': p.count, 'posts': posts_list}
