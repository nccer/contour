# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from firstspider.items import ProductItem, SupplierItem, GoldProductItem, SupplierProductItem, MolItem
from firstspider.allurls import ALL_URLS

class ChemicalbookSpider(CrawlSpider):
    name = 'cb'
    allowed_domains = ['chemicalbook.com']
    start_urls = ALL_URLS

    rules = (
        Rule(LinkExtractor(allow=r'\/ShowSupplierProductsList\d+\/0\.htm'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'\/ProdSupplierGNCB\d+\.htm'), callback='parse_supplier', follow=True),
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_product', follow=True),
        Rule(LinkExtractor(allow=r'\/ProdSupplierGN\.aspx\?CBNumber=CB\d+\&ProvID\=\d+\&start\=\d+'), callback='parse_supplier', follow=True),
    )

    def parse_product(self, response):
	productItem = ProductItem()
        supplierProductItem = SupplierProductItem()

	englishNames = response.xpath(u"//table/descendant::*[@align='left'][@width='46%'][position()>1]/a/text()").extract()
	chineseNames = response.xpath(u"//table/descendant::*[@align='left'][@width='32%'][position()>1]/text()").extract()
	casNumbers = response.xpath(u"//table/descendant::*[@align='left'][@width='16%'][position()>1]/text()").extract()
        supplier = response.xpath(u"//title/text()").re(u".+(?=产品目录)")
        products = []
	for englishName, chineseName, casNumber in zip(englishNames, chineseNames, casNumbers):
	    productItem['englishName'] = englishName
	    productItem['chineseName'] = chineseName
	    productItem['casNumber'] = casNumber
            products.append(casNumber)
	    yield productItem
        supplierProductItem['supplier'] = supplier[0].strip(' ')
        supplierProductItem['products'] = products
        yield supplierProductItem

    def parse_supplier(self, response):
	goldProductItem = GoldProductItem()
	supplierItem = SupplierItem()
        molItem = MolItem()

	presentProduct = response.xpath(u"//div[@class='search_from']/input[@type='text']/@value").extract()
	suppliersWhoProductGoldProduct = response.xpath(u"//font[text() = '黄金产品']/preceding-sibling::a[@onclick]/text()").extract()
	
	suppliers = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::a[@onclick][position() = 1]/text()").extract()
	tels = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 5]/text()").extract()
	faxs = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 7]/text()").extract()
	emails = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 9]/text()").extract()
	websites = response.xpath(u"//table[@class='ProdGN_4'][@cellpadding='2']/descendant::td[position() = 15]/a/text()").extract()

        molURL = Selector(response=response).re(u"\/CAS/mol.+?mol")
        baseURL = 'http://www.chemicalbook.com'
        if len(molURL) > 0:
            mol = baseURL+molURL[0]
            molItem['mol'] = mol
            yield molItem

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
