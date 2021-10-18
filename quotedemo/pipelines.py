# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#scraped data -> item containers -> pipelines -> SQL/Mongodb

import pymongo


class QuotedemoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['myquotes']
        self.colection = db['quotes_tb']

    def process_item(self, item, spider):
        print('Pipeline : '+item['title'][0])
        self.colection.insert(dict(item))
        return item
