# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from xunying_redis import settings
from pymongo import MongoClient


class XunyingPipeline(object):

    def __init__(self):
        client = MongoClient()
        db = client[settings.MONGODB_DB]
        self.client = db[settings.MONGODB_COLLECTION]

    def process_item(self, item, spider):
        item_dict = {}
        item_dict['name'] = item['name']
        item_dict['director'] = item['director']
        item_dict['screenwriter'] = item['screenwriter']
        item_dict['star'] = item['star']
        item_dict['type'] = item['type']
        item_dict['address'] = item['address']
        item_dict['language'] = item['language']
        item_dict['time'] = item['time']
        item_dict['long'] = item['long']
        item_dict['score'] = item['score']
        item_dict['introduce'] = item['introduce']
        item_dict['tags'] = item['tags']
        item_dict['source'] = item['source']

        is_exist = self.client.find_one({'name': item['name']})
        if is_exist:
           pass
        else:
            self.client.insert(item_dict)


        return item
