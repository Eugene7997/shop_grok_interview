import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class QcrawlSpider(CrawlSpider):
    name = 'qCrawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'page/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'quote': response.css('span.text::text').extract(),
            'author': response.css('small.author::text').extract()
        }

         