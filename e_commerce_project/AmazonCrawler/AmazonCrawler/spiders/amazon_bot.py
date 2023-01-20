from urllib.parse import urlencode

import scrapy

queries = ['oneplus mobiles', 'vivo mobiles']
class AmazonBotSpider(scrapy.Spider):
    name = 'amazon-bot'
    # allowed_domains = ['example.com']
    # start_urls = ['https://www.amazon.in/s?k=mobile+phone']

    def start_requests(self):
        for query in queries:
            url = 'https://www.amazon.com/s?' + urlencode({'k': query})
            yield scrapy.Request(url=url, callback=self.parse_keyword_response)
    def parse(self, response):
        pass
