# -*- coding: utf-8 -*-
import scrapy


class CulturetripspiderSpider(scrapy.Spider):
    name = 'culturetripspider'
    allowed_domains = ['https://theculturetrip.com']
    start_urls = ['http://https://theculturetrip.com/']

    def parse(self, response):
        pass
