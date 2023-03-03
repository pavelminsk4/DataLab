from .services.historical_search import *
from .services.get_report_state import *
from .services.get_publications import *
from .services.delete_report import *
from .services.basic_search import *
from .services.live_search import *
from tweet_binder.models import *
from datetime import datetime
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

@shared_task
def update_all_projects():
    projects = BasicSearchProject.objects.all()
    for project in projects:
        keyword = project.keyword
        limit = project.limit
        if project.search_type == 'basic search':
            basic_search_type(keyword, limit)

def add_post_to_database(data_tweets):
  tweets = []
  for tweet in data_tweets:
    new_tweet = {
                'post_id': tweet['_id'],
                'async_ops': tweet['asyncOps'],
                'binders': tweet['binders'],
                'count_textlength': int(tweet['counts']['textLength']),
                'count_sentiment': tweet['counts']['sentiment'],
                'count_retweets': tweet['counts']['retweets'],
                'count_totalretweets': tweet['counts']['totalRetweets'],
                'count_favorites': tweet['counts']['favorites'],
                'count_hashtags': tweet['counts']['hashtags'],
                'count_images': tweet['counts']['images'],
                'count_links': tweet['counts']['links'],
                'count_linksandimages': tweet['counts']['linksAndImages'], 
                'count_mentions': tweet['counts']['mentions'], 
                'count_originals': tweet['counts']['originals'], 
                'count_clears': tweet['counts']['clears'],
                'count_replies': tweet['counts']['replies'],
                'count_publicationscore': tweet['counts']['publicationScore'], 
                'count_uservalue': tweet['counts']['userValue'], 
                'count_tweetvalue': tweet['counts']['tweetValue'], 
                'createdat': tweet['createdAt'],
                'creation_date': datetime.fromtimestamp(tweet['createdAt']), 
                'favorites': tweet['favorites'], 
                'hashtags': tweet['hashtags'], 
                'images': tweet['images'], 
                'inreplyto': tweet['inReplyTo'],  
                'inreplytoid': tweet['inReplyToId'],  
                'language': tweet['lang'],  
                'links': tweet['links'],  
                'mentions': tweet['mentions'],  
                'locationString': tweet['rawLocation']['locationString'],  
                'retweets': tweet['retweets'],  
                'sentiment_vote': tweet['sentiment']['vote'],  
                'source': tweet['source'],  
                'text': tweet['text'],  
                'type': tweet['type'],  
                'updatedat': tweet['updatedAt'],  
                'user_id': tweet['user']['id'],  
                'user_name': tweet['user']['name'],  
                'user_alias': tweet['user']['alias'], 
                'user_picture': tweet['user']['picture'],
                'user_followers': tweet['user']['followers'], 
                'user_following': tweet['user']['following'], 
                'user_verified': tweet['user']['verified'], 
                'user_bio': tweet['user']['bio'], 
                'user_age': tweet['user']['age'], 
                'user_counts_lists':tweet['user']['counts']['lists'], 
                'user_statuses': tweet['user']['counts']['statuses'], 
                'user_location': tweet['user']['location'],
                'user_gender': tweet['user']['gender'], 
                'user_value': tweet['user']['value'],
                'videos': tweet['videos'],
            }
    tweets.append(new_tweet)
    try:
      django_list = [TweetBinderPost(**vals) for vals in tweets if not TweetBinderPost.objects.filter(post_id=vals['post_id'])] 
      TweetBinderPost.objects.bulk_create(django_list)
    except:
      print('error!!!')
      pass

@shared_task
def search(report_id, auth_token):
    while json.loads(get_report_state(report_id, auth_token))['status'] == "waiting":
        print(json.loads(get_report_state(report_id, auth_token))['status'])
    if json.loads(get_report_state(report_id, auth_token))['status'] == "generated":
        data_tweets = json.loads(get_publications(report_id, auth_token))
        add_post_to_database(data_tweets['data'])
        pagination = data_tweets['pagination']['nextResults']
        while pagination != None:
            data_tweets = json.loads(get_publications_next_page(report_id, auth_token, pagination))
            add_post_to_database(data_tweets['data'])
            pagination = data_tweets['pagination']['nextResults']
    else:
       print('Report not generated') 
       print(json.loads(get_report_state(report_id, auth_token))['status'])
    delete_report(auth_token, report_id)
