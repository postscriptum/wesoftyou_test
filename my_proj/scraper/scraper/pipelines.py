# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from my_app.models import Gadget


class ScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            Gadget.objects.get(code=item.get('code'))
        except Gadget.DoesNotExist:
            Gadget.objects.create(
                code=item.get('code'),
                category=item.get('category'),
                link=item.get('link'),
                price=item.get('price'),
                cashback=item.get('cashback'),
                full_desc=item.get('full_desc'),
                tech=item.get('tech'),
                photo_links=item.get('photo_links')
            )
            return item
        else:
            raise DropItem('The gadget is already stored in DB')
