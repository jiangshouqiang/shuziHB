from scrapy.spiders import CrawlSpider,Rule
from scrapy.conf import settings

from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.text import TextResponse
from shuziHB.spiders.parse.btc9Parse import btc9_parse

import json

class ShuZiHBSpider(CrawlSpider):
    name = "shuziHB"
    allowed_domains = ["szzc.com","www.btc9.com"]

    start_urls = [
        "https://www.btc9.com/Index/index.html",
        "https://szzc.com/api/public/tickers"
    ]

    # rules = (Rule(LinkExtractor(allow = ('https://www.btc9.com/Index/index.html', )), callback = 'parse_page',follow = False),)
    def parse(self, response):
        if isinstance(response,HtmlResponse):
            btc9_parse(response)
        else :
            print(response.body)
            if response is not None and response.body is not None:
                jsonRespons = json.loads(response.body.decode('utf-8'))
                for obj in jsonRespons['result']:
                    print(obj)
        # print(isinstance(response,HtmlResponse))
        # print(response.body)dddddd


from scrapy.crawler import CrawlerProcess
if __name__ == "__main__":
    process = CrawlerProcess(settings)
    spiders = ShuZiHBSpider()
    process.crawl(spiders)
    process.start()