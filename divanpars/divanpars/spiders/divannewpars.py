import scrapy

ALLOWED_DOMAINS = ["https://divan.ru"]
START_URLS = ["https://www.divan.ru/category/svet"]

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        divans = response.css("div._Ud0k")
        for divan in divans:
            yield {
                "name": divan.css("div.lsooF span::text").get(),
                "price": divan.css("div.pY3d2 span::text").get(),
                "url": ALLOWED_DOMAINS[0] + divan.css("a").attrib["href"]
            }
