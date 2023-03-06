from .services.historical_search import *
from .services.get_report_state import *
from .services.get_publications import *
from .services.delete_report import *
from .services.basic_search import *
from .services.live_search import *
from tweet_binder.models import *
from .services.login import *

@shared_task
def update_all_projects():
    projects = BasicSearchProject.objects.all()
    for project in projects:
        keyword = project.keyword
        limit = project.limit
        basic_search_type(keyword, limit)
