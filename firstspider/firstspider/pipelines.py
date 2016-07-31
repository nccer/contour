# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from support.support import Redis

class FirstspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if 'casNumber' in item:
            if Redis.exists('casNumber:%s' % item['casNumber']):
                raise DropItem("Duplicate item found: %s" % item)
            else:
                Redis.set('casNumber:%s' % item['casNumber'], 1)
                return item
	elif 'tel' in item:
	    if Redis.exists('tel:%s' % item['tel']):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('tel:%s' % item['tel'], 1)
		return item
	else:
	    if Redis.exists('supplier:%sproduct:%s' % (item['supplier'], item['product'])):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('supplier:%sproduct:%s' % (item['supplier'], item['product']), 1)
		return item
