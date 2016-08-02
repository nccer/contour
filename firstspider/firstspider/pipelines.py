# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from support.support import Redis
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
                string = 'englishName'+','+item['englishName']+'|'+'chineseName'+','+item['chineseName']+'|'+'casNumber'+','+item['casNumber']+'|'+'\n'
                with open('/home/pc/Documents/data/product.txt', 'a+') as f:
                    f.write(string)
                return item
	elif 'tel' in item:
	    if Redis.exists('tel:%s' % item['tel']):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('tel:%s' % item['tel'], 1)
                string = 'supplier'+','+item['supplier']+'|'+'tel'+','+item['tel']+'|'+'fax'+','+item['fax']+'|'+'email'+','+item['email']+'|'+'website'+','+item['website']+'|'+'\n'
                with open('/home/pc/Documents/data/supplier.txt', 'a+') as f:
                    f.write(string)
		return item
	else:
	    if Redis.exists('supplier:%sproduct:%s' % (item['supplier'], item['product'])):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('supplier:%sproduct:%s' % (item['supplier'], item['product']), 1)
                string = 'supplier'+','+item['supplier']+'|'+'product'+','+item['product']+'|'+'\n'
                with open('/home/pc/Documents/data/goldProduct.txt', 'a+') as f:
                    f.write(string)
		return item
