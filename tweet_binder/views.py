from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tweet_binder.models import TweetBinderPost
from datetime import datetime
import pprint
import json

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for el in data:
            tweet = el['value']['data']
            new_tweet = {
                'post_id': tweet["_id"],
                'async_ops': tweet['asyncOps'],
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
            TweetBinderPost.objects.create(**new_tweet)
        return HttpResponse("Webhook received!")
    

