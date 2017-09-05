#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import TutorialItem
from scrapy.loader import ItemLoader

class Meitulu(scrapy.Spider):
	name = 'Meitu'
	allowed_domains = ['meitulu.com','mtl.ttsqgs.com']
	start_urls = ['https://www.meitulu.com/item/7869.html'] #可以换个number.html

	def parse(self,response):
		yield self.parse_item(response)
		each = response.xpath('//center//div//a/@href').extract()[-1]
		if each is not None:
			yield response.follow(each,callback=self.parse)

	def parse_item(self,response):
		il = ItemLoader(item=TutorialItem(),response=response)
		il.add_xpath('image_urls','//center//img/@src')
		return il.load_item()
