import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AidiSpider(CrawlSpider):
    name = "aidi"
    allowed_domains = ['aldi.com.au']
    start_urls = ['https://www.aldi.com.au/']

    rules = (
        Rule(LinkExtractor(allow='groceries', deny=('shopping-list','social-bookmarks.html', r'.*-recipe')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'product_title': "".join(a.strip() for a in response.css("h1.detail-box--price-box--title *::text").extract()),
            'price': response.css('span.box--value::text').get()+response.css('span.box--decimal::text').get(),
            'pack_size': response.css('span.detail-box--price-box--price--amount.box--amount ::text').get(),
            'price_per_unit': response.css('span.detail-box--price-box--price--detailamount.box--detailamount::text').get(),
        }