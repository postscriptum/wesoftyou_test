# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from my_app.models import Gadget


class ScraperPipeline(object):
    def process_item(self, item, spider):
        # print('ITEM: ', item['tech'])
        return item
