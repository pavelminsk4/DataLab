from celery import shared_task
from datetime import datetime
import feedparser
from project.models import Feedlinks, Post, Speech
from django.core.paginator import Paginator
import ssl
from langcodes import *
from dateutil import parser
from  nltk.sentiment import SentimentIntensityAnalyzer
import socket
socket.setdefaulttimeout(5)

def split_links(amount_posts_in_sample):
  all_posts = Feedlinks.objects.all()
  p = Paginator(all_posts, amount_posts_in_sample)
  return p

def add_language(language_code):
  title = Language.get(language_code).display_name()
  if not Speech.objects.filter(language=title):
    Speech.objects.create(language=title)
  return Speech.objects.filter(language=title).first()

def get_string_from_score(sentiments):
  if sentiments['neg'] > sentiments['neu'] and sentiments['neg'] > sentiments['pos']:
      res = 'negative'
  elif sentiments['neu'] > sentiments['pos']:
    res = 'neutral'
  else:
    res = 'positive'
  return res

def add_sentiment_score(title):
  sentiments = SentimentIntensityAnalyzer().polarity_scores(title)
  sentiment = get_string_from_score(sentiments)
  return sentiment

@shared_task
def post_creator():
  ssl._create_default_https_context = ssl._create_unverified_context #fix SSL issue in local machine
  datas = []
  i = 0
  for sample in split_links(1):
  #sample = split_links(10).page(162)
    for feed in sample:
      print('---->i')
      print(feed.url)
      print(i)
      print('---------<')
      i += 1
      url = feed.url
      try:
        print('----try')
        f = feedparser.parse(url)
        print(f)
        fe = f.entries
        ff = f.feed
        for ent in fe:
          if not Post.objects.filter(entry_title=ent.title):
            my_feedlink = feed
            my_sentiment = add_sentiment_score(ent.title)
            try:
                my_title = ent.title
            except:
                my_title = 'None'
            try:
                myid = ent.id
            except:
                myid = 'None'
            try:
                my_title_detail_type = ent.title_detail.type
            except:
                my_title_detail_type = 'None'
            try:
                my_title_detail_base = ent.title_detail.base
            except:
                my_title_detail_base = 'None'
            try:
                my_title_detail_value = ent.title_detail.value
            except:
                my_title_detail_value = 'None'
            try:
                my_links_rel = ent.ent.links[0].rel
            except:
                my_links_rel = 'None'
            try:
                my_links_type = ent.links[0].type
            except:
                my_links_type = 'None'
            try:
                my_links_href = ent.links[0].href
            except:
                my_links_href = 'None'
            try:
                my_title_detail_language = ent.title_detail.language
            except:
                my_title_detail_language = 'None'
            try:
                my_link = ent.link
            except:
                my_link = 'None'
            try:
                my_published = parser.parse(ent.published)
            except:
                my_published = datetime.now()
            try:
                my_published_parsed = ent.published_parsed
            except:
                my_published_parsed = 'None'
            try:
                my_summary = ent.summary
            except:
                my_summary = 'None'

            try:
                myguidislink = ent.guidislink
            except:
                myguidislink = 'None'

            try:
                my_entry_content_type = ent.content[0].type
            except:
                my_entry_content_type = 'None'

            try:
                my_entry_content_language = ent.content[0].language
            except:
                my_entry_content_language = 'None'

            try:
                my_entry_content_base = ent.content[0].base
            except:
                my_entry_content_base = 'None'

            try:
                my_entry_content_value = ent.content[0].value
            except:
                my_entry_content_value = 'None'

            try:
                my_media_thumbnail_url = ent.media_thumbnail[0]['url']

            except:
                my_media_thumbnail_url = 'None'

            try:
                my_media_thumbnail_width = ent.media_thumbnail[0]['width']
            except:
                my_media_thumbnail_width = 'None'

            try:
                my_media_thumbnail_height = ent.media_thumbnail[0]['height']
            except:
                my_media_thumbnail_height = 'None'

            try:
                myhref = ent.href
            except:
                myhref = 'None'

            try:
                my_entry_media_content_type = ent.media_content[0]['type']
            except:
                my_entry_media_content_type = 'None'

            try:
                my_entry_media_content_url = ent.media_content[0]['url']
            except:
                my_entry_media_content_url = 'None'

            try:
                my_entry_media_content_height = ent.media_content[0]['height']
            except:
                my_entry_media_content_height = 'None'

            try:
                my_entry_media_content_medium = ent.media_content[0]['medium']
            except:
                my_entry_media_content_medium = 'None'

            try:
                my_entry_media_content_width = ent.media_content[0]['width']
            except:
                my_entry_media_content_width = 'None'

            try:
                my_entry_media_credit_content = ent.media_credit[0]['content']
            except:
                my_entry_media_credit_content = 'None'

            try:
                my_entry_credit = ent['credit']
            except:
                my_entry_credit = 'None'

            try:
                my_entry_authors = ent['authors'][0]['name']
            except:
                my_entry_authors = 'None'

            try:
                my_entry_author = ent['author']
            except:
                my_entry_author = 'None'

            try:
                my_entry_author_detail = ent['author_detail']
            except:
                my_entry_author_detail = 'None'

            try:
                my_entry_tags_term = ent['tags'][0]['term']
            except:
                my_entry_tags_term = 'None'

            try:
                my_entry_tags_scheme = ent['tags'][0]['scheme']
            except:
                my_entry_tags_scheme = 'None'

            try:
                my_entry_tags_label = ent['tags'][0]['label']
            except:
                my_entry_tags_label = 'None'

            try:
                my_feed_title = ff['title']
            except:
                my_feed_title = 'None'

            try:
                my_feed_title_detail_type = ff['title_detail']['type']
            except:
                my_feed_title_detail_type = 'None'

            try:
                my_feed_title_detail_language = ff['title_detail']['language']
            except:
                my_feed_title_detail_language = 'None'

            try:
                my_feed_title_detail_base = ff['title_detail']['base']
            except:
                my_feed_title_detail_base = 'None'

            try:
                my_feed_title_detail_value = ff['title_detail']['value']
            except:
                my_feed_title_detail_value = 'None'

            try:
                my_feed_links_rel = ff['links'][0]['rel']
            except:
                my_feed_links_rel = 'None'

            try:
                my_feed_links_type = ff['links'][0]['type']
            except:
                my_feed_links_type = 'None'

            try:
                my_feed_links_href = ff['links'][0]['href']
            except:
                my_feed_links_href = 'None'

            try:
                my_feed_link = ff['link']
            except:
                my_feed_link = 'None'


            try:
                my_feed_image_title = ff['image']['title']
            except:
                my_feed_image_title = 'None'

            my_feed_image_title_detail_type = 'None'
            my_feed_image_title_detail_language = 'None'
            my_feed_image_title_detail_base = 'None'
            my_feed_image_title_detail_value = 'None'

            try:
                my_feed_image_href = ff['image']['href']
            except:
                my_feed_image_href = 'None'

            try:
                my_feed_image_link = ff['image']['link']
            except:
                my_feed_image_link = 'None'

            try:
                my_feed_image_links = ff['image']['links']
            except:
                my_feed_image_links = 'None'

            try:
                my_feed_subtitle = ff['subtitle']
            except:
                my_feed_subtitle = 'None'

            try:
                my_feed_subtitle_detail = ff['subtitle_detail']
            except:
                my_feed_subtitle_detail = 'None'

            try:
                my_feed_language = add_language(ff['language'])
            except:
                my_feed_language = Speech.objects.get_or_create(language='Language not specified')[0]

            try:
                my_feed_rights = ff['rights']
            except:
                my_feed_rights = 'None'

            try:
                my_feed_rights_detail = ff['rights_detail']
            except:
                my_feed_rights_detail = 'None'

            try:
                my_feed_updated = ff['updated']
            except:
                my_feed_updated = 'None'

            try:
                my_feed_updated_parsed = ff['updated_parsed']
            except:
                my_feed_updated_parsed = 'None'

            try:
                my_feed_published = ff['published']
            except:
                my_feed_published = datetime.now()
            try:
                my_feed_published_parsed = ff['published_parsed']
            except:
                my_feed_published_parsed = 'None'
            
            try:
                my_feed_tags_term = ff['tags'][0]['term']
            except:
                my_feed_tags_term = 'None'

            try:
                my_feed_tags_scheme = ff['tags'][0]['scheme']
            except:
                my_feed_tags_scheme = 'None'

            try:
                my_feed_tags_label = ff['tags'][0]['label']
            except:
                my_feed_tags_label = 'None'

            try:
                my_feed_tags_list = ff['tags']
            except:
                my_feed_tags_list = 'None'

            try:
                my_feed_ttl = ff['ttl']
            except:
                my_feed_ttl = 'None'

            try:
                my_feed_generator_detail = ff['generator_detail']
            except:
                my_feed_generator_detail = 'None'

            try:
                my_feed_docs = ff['docs']
            except:
                my_feed_docs = 'None'

            try:
                my_feed_generator = ff['generator']
            except:
                my_feed_generator = 'None'

            try:
                my_feed_publisher = ff['publisher']
            except:
                my_feed_publisher = 'None'
            snippet = {
            "feedlink" : my_feedlink,
            "entry_title" : my_title,
            "sentiment": my_sentiment,
            "entry_title_detail_type": my_title_detail_type,
            "entry_title_detail_base": my_title_detail_base,
            "entry_title_detail_value": my_title_detail_value,
            "entry_links_rel": my_links_rel,
            'entry_links_type': my_links_type,
            'entry_links_href': my_links_href,
            'entry_title_detail_language' : my_title_detail_language,
            'entry_link' : my_link,
            'entry_summary' : my_summary,
            'entry_published' : my_published,
            'entry_published_parsed' :  my_published_parsed,
            'entry_id' : myid,
            'entry_guidislink'  : myguidislink,
            'entry_content_type' : my_entry_content_type,
            'entry_content_language' : my_entry_content_language,
            'entry_content_base' : my_entry_content_base,
            'entry_content_value' : my_entry_content_value,
            'entry_media_thumbnail_url' : my_media_thumbnail_url,
            'entry_media_thumbnail_width' : my_media_thumbnail_width,
            'entry_media_thumbnail_height' : my_media_thumbnail_height,
            'entry_href' : myhref,
            'entry_media_content_type' : my_entry_media_content_type,
            'entry_media_content_url' : my_entry_media_content_url,
            'entry_media_content_height' : my_entry_media_content_height,
            'entry_media_content_medium' : my_entry_media_content_medium,
            'entry_media_content_width' : my_entry_media_content_width,
            'entry_media_credit_content' : my_entry_media_credit_content,
            'entry_credit' : my_entry_credit,
            'entry_authors' : my_entry_authors,
            'entry_author' : my_entry_author,
            'entry_author_detail' : my_entry_author_detail,
            'entry_tags_term' : my_entry_tags_term,
            'entry_tags_scheme' : my_entry_tags_scheme,
            'entry_tags_label' : my_entry_tags_label,
            'feed_title' : my_feed_title,
            'feed_title_detail_type' : my_feed_title_detail_type,
            'feed_title_detail_language' : my_feed_title_detail_language,
            'feed_title_detail_base' : my_feed_title_detail_base,
            'feed_title_detail_value' : my_feed_title_detail_value,
            'feed_links_rel' : my_feed_links_rel,
            'feed_links_type' : my_feed_links_type,
            'feed_links_href' : my_feed_links_href,
            'feed_link' : my_feed_link,
            'feed_image_title' : my_feed_image_title,
            'feed_image_title_detail_type' : my_feed_image_title_detail_type,
            'feed_image_title_detail_language' : my_feed_image_title_detail_language,
            'feed_image_title_detail_base' : my_feed_image_title_detail_base,
            'feed_image_title_detail_value' : my_feed_image_title_detail_value,
            'feed_image_href' : my_feed_image_href,
            'feed_image_link' : my_feed_image_link,
            'feed_image_links' : my_feed_image_links,
            'feed_subtitle' : my_feed_subtitle,
            'feed_subtitle_detail' : my_feed_subtitle_detail,
            'feed_language' : my_feed_language,
            'feed_rights' : my_feed_rights,
            'feed_rights_detail' : my_feed_rights_detail,
            'feed_updated' : my_feed_updated,
            'feed_updated_parsed' : my_feed_updated_parsed,
            'feed_published': my_feed_published,
            'feed_published_parsed': my_feed_published_parsed,
            'feed_tags_term' : my_feed_tags_term,
            'feed_tags_scheme' : my_feed_tags_scheme,
            'feed_tags_label': my_feed_tags_label,
            'feed_tags_list':my_feed_tags_list,
            'feed_ttl':my_feed_ttl,
            'feed_docs':my_feed_docs,
            'feed_generator_detail':my_feed_generator_detail
            }
            print('---->')
            print(snippet)
            print('-----<')
            datas.append(snippet)
      except:
        print('Something went wrong!!!')
        pass
    try:
      django_list = [Post(**vals) for vals in datas] 
      Post.objects.bulk_create(django_list)
    except:
      print('error!!!')
      pass
    datas = []
