#!/usr/bin/env python

import scrapy
from tutorial.items import TutorialItem

class MySpider(scrapy.Spider):
	name = 'MySpider'
	start_urls = [
		"http://www.meitulu.com/item/9733.html",
	]

	def parse(self,response):
		for each in response.xpath('//center//img/@src').extract():
			yield {
				'image_urls':each,
			} 
			
