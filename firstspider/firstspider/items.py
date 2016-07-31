# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductItem(scrapy.Item):
    englishName = scrapy.Field()
    chineseName = scrapy.Field()
    casNumber = scrapy.Field()


class SupplierItem(scrapy.Item):
    supplier = scrapy.Field()
    product = scrapy.Field()
    tel = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()


class GoldProductItem(scrapy.Item):
    supplier = scrapy.Field()
    product = scrapy.Field()
