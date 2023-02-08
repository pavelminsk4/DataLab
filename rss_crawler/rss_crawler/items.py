# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from project.models import NewFeedlinks, CrawlerKeyword, Feedlinks

class RssCrawlerItem(DjangoItem):
    django_model = NewFeedlinks

class CrawlerKeywordItem(DjangoItem):
    django_model = CrawlerKeyword

class FeedlinksItem(DjangoItem):
    django_model = Feedlinks
