import scrapy
import geonamescache
import feedparser
import ssl
import re
import socket
from rss_crawler.items import RssCrawlerItem, CrawlerKeyword

socket.setdefaulttimeout(3)

class RsssearchhubSpider(scrapy.Spider):
    name = 'rsssearchhub'

    base_url = 'http://www.rsssearchhub.com/'
    search_suffix = 'feeds?q='
    keywords = CrawlerKeyword.objects.all()

    gc =geonamescache.GeonamesCache()
    cities = gc.get_cities()

    reqs_urls = []

    for keyword in keywords:
        reqs_urls.append(base_url + search_suffix + keyword.word)

    # for city in cities:
    #     for alternatename in cities[city]['alternatenames']:
    #         reqs_urls.append(base_url + search_suffix + alternatename)

    allowed_domains = [base_url]
    start_urls = reqs_urls

    def parse(self, response):
        ssl._create_default_https_context = ssl._create_unverified_context
        feeds = response.xpath('//div[@class="result"]')
        for feed in feeds:
            url = feed.xpath('p//a/text()').extract()
            source1 = feed.xpath('h2//a/text()').extract()
            sourceurl = feed.xpath('p//span//text()').extract()
            
            
            if not re.match('(?:http|ftp|https)://', url[0]):
                url[0] = 'http://{}'.format(url[0])
            
            if not re.match('(?:http|ftp|https)://', sourceurl[0]):
                sourceurl[0] = 'http://{}'.format(sourceurl[0])            

            if feedparser.parse(url[0]).bozo == False and len(feedparser.parse(url[0]).entries)!=0:
                item = RssCrawlerItem()
                item['url'] = url[0]
                item['source1'] = source1[0]
                item['sourceurl'] = sourceurl[0]
                yield item
