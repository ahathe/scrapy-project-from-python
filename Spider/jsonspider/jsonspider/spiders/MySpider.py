#!/usr/bin/env python

import scrapy

class MySpider(scrapy.Spider):
	name = 'MySpider'
	start_urls = [
		'http://www.meitulu.com/item/3583.html',
		]
	
	def parse(self,response):
		for each in response.xpath('//center//img'):
			yield {
				'jpg':each.xpath('@src').extract()
			}
			


		next_page = response.xpath('//center//a/@href').extract()[-1]
		if next_page is not None:
			yield response.follow(next_page,callback=self.parse)
