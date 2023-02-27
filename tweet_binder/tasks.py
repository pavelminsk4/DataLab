from .services.historical_search import *
from .services.get_report_state import *
from .services.get_publications import *
from .services.delete_report import *
from .services.basic_search import *
from .services.live_search import *
from tweet_binder.models import *
from .services.login import *
from celery import shared_task

import time
import os
import json

email = os.environ.get("EMAIL_TWEET")
password = os.environ.get("PASSWORD_TWEET")
api_route = os.environ.get("API_ROUTE")

def basic_search_type(keyword, limit):
    basic_search_url = api_route + '/search/twitter/7-day'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(basic_search(keyword, limit, auth_token, basic_search_url))["resourceId"]
    time.sleep(5)
    search(report_id, auth_token)

def historical_search_type(keyword, limit, start_date, end_date):
    historical_search_url = api_route + '/search/twitter/historical'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(historical_search(keyword, limit, start_date, end_date, auth_token, historical_search_url))["resourceId"]
    time.sleep(60)
    search(report_id, auth_token)   

def live_search_type(keyword, limit):
    live_search_url = api_route + '/search/twitter/live'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(live_search(keyword, limit, auth_token, live_search_url))["resourceId"]

@shared_task
def update_all_projects():
    projects = BasicSearchProject.objects.all()
    for project in projects:
        keyword = project.keyword
        limit = project.limit
        if project.search_type == 'basic search':
            basic_search_type(keyword, limit)
