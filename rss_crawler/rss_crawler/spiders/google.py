import scrapy
import feedparser
import ssl
import re
import socket
import os
from rss_crawler.items import RssCrawlerItem, CrawlerKeyword, Feedlinks
from serpapi import GoogleSearch
from urllib.parse import urlparse

socket.setdefaulttimeout(3)
ssl._create_default_https_context = ssl._create_unverified_context

class GoogleSpider(scrapy.Spider):
    name = 'google'

    keywords = CrawlerKeyword.objects.all().values_list('word', flat=True)
    secret_key = os.environ.get('GOOGLE_SEARCH_SECRET_KEY')

    def collect_start_urls(keywords, secret_key):
        start_urls = []
        for word in keywords:
            search = GoogleSearch({"q": word, "num":"10000", "api_key": secret_key, "tbm": "nws"})
            result = search.get_dict()
            for block in result['news_results']:
                start_urls.append(block['link'])
        return start_urls

    allowed_domains = collect_start_urls(keywords, secret_key)
    start_urls = collect_start_urls(keywords, secret_key)

    def parse(self, response):
        links = []

        feeds = response.xpath("//a[contains(@href, 'rss')]/@href").extract()
        links += feeds

        feeds = response.xpath("//a[contains(@href, 'feed')]/@href").extract()
        links += feeds

        feeds = response.xpath('//a[@class="icon-rss"]/@href').extract()
        links += feeds

        feeds = response.xpath('//link[@type="application/rss+xml"]/@href').extract()
        links += feeds

        feeds = response.xpath('//link[@type="applictation/xml"]/@href').extract()
        links += feeds

        feeds = response.xpath('//a[@class="icon_rss"]/@href').extract()
        links += feeds

        feeds = response.xpath('//a[@title="RSS"]/@href').extract()
        links += feeds

        for ind, val in enumerate(links):
            if '.' not in links[ind] or ('.xml' in links[ind] and links[ind].count('.')==1):
                scheme = urlparse(response.request.url).scheme
                netloc = urlparse(response.request.url).netloc
                links[ind] = scheme + '://' + netloc + links[ind]

        for feed in links:
            if not re.match('(?:http|ftp|https)://', feed):
                feed = 'http://{}'.format(feed)
            in_feedlinks = Feedlinks.objects.filter(url=feed)
            if feedparser.parse(feed).bozo == False and len(feedparser.parse(feed).entries)!=0 and not in_feedlinks:
                item = RssCrawlerItem()
                item['url'] = feed
                try:
                    f = feedparser.parse(feed)
                    item['sourceurl'] = f.feed.link
                    item['source1'] = f.feed.title
                except:
                    print('Error')
                yield item
