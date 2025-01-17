from langcodes import Language
from datetime import datetime
from project.models import Speech, Post, Feedlinks
from django.utils import timezone
from django.db import transaction

import json
import logging

logger = logging.getLogger()


def language(language_code):
    title = Language.get(language_code).display_name()
    return Speech.objects.get_or_create(language=title)[0]


def define_sentiment(value):
    sent = 'neutral'
    if value < 0:
        sent = 'negative'
    if value > 0:
        sent = 'positive'
    return sent


def create_posts(project, response, offset=None):
    resume_offset = None

    for line in response.iter_lines():
        try:
            resume_offset = json.loads(line)['chunk_control']['resume_offset']
            continue
        except:
            try:
                data = json.loads(line)['chunk_result']['data']['data']
            except Exception as e:
                logger.error(e)
                continue
        try:
            acountry = data['extra_source_attributes']['world_data']['country']
        except:
            acountry = ''
        try:
            asourceurl = data['host_url']
        except:
            asourceurl = ''
        try:
            aalexaglobalrank = data['reach']
        except:
            aalexaglobalrank = 0
        try:
            asource1 = data['extra_source_attributes']['name']
        except:
            asource1 = ''
        try:
            aentry_title = data['title']
        except:
            aentry_title = ''
        try:
            aentry_summary = data['content']
        except:
            aentry_summary = ''
        try:
            afeed_language = language(data['lang'])
        except:
            afeed_language = Speech.objects.filter(language='English (United States)').first()
        try:
            aentry_media_content_url = data['images'][0]['url']
        except:
            aentry_media_content_url = ''
        try:
            aentry_links_href = data['url']
        except:
            aentry_links_href = ''
        try:
            aentry_author = data['extra_source_attributes']['name']
        except:
            aentry_author = ''
        try:
            aentry_published = timezone.make_aware(datetime.fromtimestamp(data['published'] / 1000))
        except:
            aentry_published = timezone.now()
        try:
            asentiment = define_sentiment(data['sentiment'])
        except:
            asentiment = 'neutral'
        try:
            acategory = data['tokens_content'][0]
        except:
            acategory = ''
        try:
            with transaction.atomic():
                fl = Feedlinks.objects.filter(sourceurl=asourceurl).order_by('-alexaglobalrank').first()
                if fl is None:
                    fl = Feedlinks.objects.create(
                        sourceurl=asourceurl,
                        country=acountry,
                        alexaglobalrank=aalexaglobalrank,
                        source1=asource1
                    )

                post = Post.objects.filter(entry_title=aentry_title, entry_author=aentry_author).first()
                if post is None:
                    post = Post.objects.create(
                        entry_title=aentry_title,
                        entry_author=aentry_author,
                        entry_summary=aentry_summary,
                        feed_language=afeed_language,
                        entry_media_content_url=aentry_media_content_url,
                        entry_links_href=aentry_links_href,
                        entry_published=aentry_published,
                        sentiment=asentiment,
                        category=acategory,
                        feedlink=fl,
                        summary_vector=[],
                        source_type='talkwalker'
                    )

                project.posts.add(post)
        except Exception as e:
            logger.error(e)

    if resume_offset and resume_offset != 'earliest':
        project.resume_offset = resume_offset
        project.save()

    return resume_offset if resume_offset != offset and resume_offset != 'earliest' else None
