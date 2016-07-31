# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from firstspider.items import ProductItem, SupplierItem, GoldProductItem


class ChemicalbookSpider(CrawlSpider):
    name = 'chemicalbook'
    allowed_domains = ['chemicalbook.com']
    start_urls = ['http://www.chemicalbook.com/ShowSupplierProductsList3999/0.htm']

    rules = (
        Rule(LinkExtractor(allow=r'\/ShowSupplierProductsList\d+\/0\.htm'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'\/ProdSupplierGNCB\d+\.htm'), callback='parse_supplier', follow=True),
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'\/ProdSupplierGN\.aspx\?CBNumber=CB\d+\&ProvID\=\d+\&start\=\d+'), callback='parse_supplier', follow=True),
    )

    def parse_product(self, response):
	i = ProductItem()
	englishNames = response.xpath(u"//table/descendant::*[@align='left'][@width='46%'][position()>1]/a/text()").extract()
	chineseNames = response.xpath(u"//table/descendant::*[@align='left'][@width='32%'][position()>1]/text()").extract()
	casNumbers = response.xpath(u"//table/descendant::*[@align='left'][@width='16%'][position()>1]/text()").extract()
	for englishName, chineseName, casNumber in zip(englishNames, chineseNames, casNumbers):
	    i['englishName'] = englishName
	    i['chineseName'] = chineseName
	    i['casNumber'] = casNumber
	    yield i

    def parse_supplier(self, response):
	goldProductItem = GoldProductItem()
	supplierItem = SupplierItem()
	presentProduct = response.xpath(u"//div[@class='search_from']/input[@type='text']/@value").extract()
	suppliersWhoProductGoldProduct = response.xpath(u"//font[text() = '黄金产品']/preceding-sibling::a[@onclick]/text()").extract()
	
	suppliers = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::a[@onclick][position() = 1]/text()").extract()
	tels = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 5]/text()").extract()
	faxs = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 7]/text()").extract()
	emails = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 9]/text()").extract()
	websites = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 15]/a/text()").extract()
	for supplier, tel, fax, email, website in zip(suppliers, tels, faxs, emails, websites):
	    supplierItem['supplier'] = supplier
	    supplierItem['tel'] = tel
	    supplierItem['fax'] = fax
	    supplierItem['email'] = email
	    supplierItem['website'] = website
	    yield supplierItem
	
	for supplier in suppliersWhoProductGoldProduct:
	    goldProductItem['supplier'] = supplier
	    goldProductItem['product'] = presentProduct[0]
	    yield goldProductItem
