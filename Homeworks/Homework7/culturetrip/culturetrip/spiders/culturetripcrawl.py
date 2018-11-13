import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class culturetripitem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    response = scrapy.Field()
    
class culturetripSpider(scrapy.Spider):
    name = 'culturetripcrawler'
    allowed_domains = ['https://theculturetrip.com/']
    start_urls = ['https://theculturetrip.com/north-america/usa/articles/the-usa-s-10-most-talented-food-bloggers-to-follow/',
                  'https://theculturetrip.com/north-america/film-and-tv/',
                  'https://theculturetrip.com/middle-east/',
                  'https://theculturetrip.com/asia/',
                  'https://theculturetrip.com/pacific/',
                  'https://theculturetrip.com/pacific/music/',
                  'https://theculturetrip.com/europe/books/',
                  'https://theculturetrip.com/north-america/']
    rules = (Rule(SgmlLinkExtractor(allow=(),restrict_xpaths=('//a[@class="button next"]',)),
                  callback="parse", 
                  follow= True),)



    def parse(self, response):
        hxs = scrapy.Selector(response)
        titles = hxs.xpath('//ul/li')
        item = []
        for title in titles:
            item_object = culturetripitem()
            item_object["title"] = title.xpath("a/text()").extract()
            item_object["link"] = title.xpath("a/@href").extract()
            item_object["response"] = response
            if item_object["title"] != []:
                item.append(item_object)

        return item