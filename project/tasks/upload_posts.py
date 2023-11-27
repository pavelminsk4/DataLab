from celery import shared_task
from datetime import datetime
from project.models import Feedlinks, Post, Speech, Status
from django.core.paginator import Paginator
from langcodes import Language
from dateutil import parser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from ftlangdetect import detect
from transformers import pipeline
import ssl
import socket
import feedparser
import logging

socket.setdefaulttimeout(3)
logger = logging.getLogger()


def split_links(amount_posts_in_sample):
    all_posts = Feedlinks.objects.all().order_by('-alexaglobalrank')
    return Paginator(all_posts, amount_posts_in_sample)


def add_language(language_code):
    title = Language.get(language_code).display_name()
    return Speech.objects.get_or_create(language=title)[0]


def get_string_from_score(sentiments):
    if sentiments['compound'] >= 0.05:
        res = 'positive'
    elif sentiments['compound'] <= - 0.05:
        res = 'negative'
    else:
        res = 'neutral'
    return res


def add_sentiment_score(title):
    sentiments = SentimentIntensityAnalyzer().polarity_scores(title)
    return get_string_from_score(sentiments)


@shared_task
def post_creator():
    ssl._create_default_https_context = ssl._create_unverified_context

    for sample in split_links(10):
        for feed in sample:
            Status.objects.filter(id=Status.objects.first().id).update(progress=1)

            f = feedparser.parse(feed.url)
            fe = f.entries
            ff = f.feed

            datas = []
            for ent in fe:
                if Post.objects.filter(entry_title=ent.title):
                    continue

                my_feedlink = feed
                my_sentiment = add_sentiment_score(ent.title)
                try:
                    my_title = ent.title
                except:
                    my_title = 'None'
                try:
                    my_links_href = ent.links[0].href
                except:
                    my_links_href = 'None'
                try:
                    my_published = parser.parse(ent.published)
                except:
                    my_published = datetime.now()
                try:
                    my_summary = BeautifulSoup(ent.summary, features='lxml').text
                except:
                    my_summary = 'None'
                try:
                    my_media_thumbnail_url = ent.media_thumbnail[0]['url']
                except:
                    my_media_thumbnail_url = 'None'
                try:
                    my_entry_media_content_url = ent.media_content[0]['url']
                except:
                    my_entry_media_content_url = 'None'
                try:
                    my_entry_author = ent['author']
                except:
                    my_entry_author = 'None'
                try:
                    my_feed_title = ff['title']
                except:
                    my_feed_title = 'None'
                try:
                    my_feed_image_href = ff['image']['href']
                except:
                    my_feed_image_href = 'None'
                try:
                    my_feed_image_link = ff['image']['link']
                except:
                    my_feed_image_link = 'None'
                try:
                    my_feed_language = add_language(detect(ent.title)['lang'])
                except:
                    my_feed_language = Speech.objects.filter(language='English (United States)').first()
                snippet = {
                    'feedlink': my_feedlink,
                    'entry_title': my_title,
                    'sentiment': my_sentiment,
                    'entry_links_href': my_links_href,
                    'entry_summary': my_summary,
                    'entry_published': my_published,
                    'entry_media_thumbnail_url': my_media_thumbnail_url,
                    'entry_media_content_url': my_entry_media_content_url,
                    'entry_author': my_entry_author,
                    'feed_title': my_feed_title,
                    'feed_image_href': my_feed_image_href,
                    'feed_image_link': my_feed_image_link,
                    'feed_language': my_feed_language,
                    'is_sentiment': True,
                    'summary_vector': [],
                    'source_type': 'rss'
                }
                datas.append(snippet)
            try:
                django_list = [Post(**vals) for vals in datas]
                Post.objects.bulk_create(django_list)
            except Exception as e:
                logger.error(e)


@shared_task
def imp_sentiment():
    model_path = 'cardiffnlp/twitter-xlm-roberta-base-sentiment'
    sentiment_task = pipeline('sentiment-analysis', model=model_path, tokenizer=model_path, max_length=512, truncation=True)

    for p in Post.objects.filter(imp_sentiment='').order_by('-creationdate')[:20000]:
        if len(p.entry_summary) > 50:
            p.imp_sentiment = sentiment_task(p.entry_summary)[0]['label']
        else:
            p.imp_sentiment = sentiment_task(p.entry_title)[0]['label']
        p.save()