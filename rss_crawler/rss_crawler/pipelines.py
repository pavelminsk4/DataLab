# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interfacez
from project.models import NewFeedlinks

class RssCrawlerPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
