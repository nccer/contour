# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from support.support import Redis
from firstspider.items import ProductItem, SupplierItem, GoldProductItem, SupplierProductItem, MolItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class FirstspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ProductItem):
            if Redis.exists('casNumber:%s' % item['casNumber']):
                raise DropItem("Duplicate item found: %s" % item)
            else:
                Redis.set('casNumber:%s' % item['casNumber'], 1)
                string = 'englishName'+','+item['englishName']+'|'+'chineseName'+','+item['chineseName']+'|'+'casNumber'+','+item['casNumber']+'|'+'\n'
                with open('/home/pc/Documents/data/product.txt', 'a+') as f:
                    f.write(string)
                return item
	elif isinstance(item, SupplierItem):
	    if Redis.exists('tel:%s' % item['tel']):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('tel:%s' % item['tel'], 1)
                string = 'supplier'+','+item['supplier']+'|'+'tel'+','+item['tel']+'|'+'fax'+','+item['fax']+'|'+'email'+','+item['email']+'|'+'website'+','+item['website']+'|'+'\n'
                with open('/home/pc/Documents/data/supplier.txt', 'a+') as f:
                    f.write(string)
		return item
        elif isinstance(item, GoldProductItem):
	    if Redis.exists('supplier:%sproduct:%s' % (item['supplier'], item['product'])):
		raise DropItem("Duplicate item found: %s" % item)
	    else:
		Redis.set('supplier:%sproduct:%s' % (item['supplier'], item['product']), 1)
                string = 'supplier'+','+item['supplier']+'|'+'product'+','+item['product']+'|'+'\n'
                with open('/home/pc/Documents/data/goldProduct.txt', 'a+') as f:
                    f.write(string)
		return item
        elif isinstance(item, SupplierProductItem):
            if len(item['products']) > 0:
                if Redis.exists('supplierproduct:%s:%s' % (item['supplier'], item['products'][0])):
                    raise DropItem("Duplicate item found: %s" % item)
                else:
                    Redis.set('supplierproduct:%s:%s' % (item['supplier'], item['products'][0]), 1)
                    string = ''
                    for product in item['products']:
                        string += (product+',')
                    string = item['supplier']+':'+string+'\n'
                    with open('/home/pc/Documents/data/supplierProduct.txt', 'a+') as f:
                        f.write(string)
                    return item
            else:
                raise DropItem("len < 1")
        elif isinstance(item, MolItem):
            if Redis.exists('mol:%s' % item['mol']):
                raise DropItem("Duplicate item found: %s" % item)
            else:
                Redis.set('mol:%s' % item['mol'], 1)
                string = item['mol']+'\n'
                with open('/home/pc/Documents/data/mol.txt', 'a+') as f:
                    f.write(string)
                return item
