import scrapy


class WorkUaSpider(scrapy.Spider):
    name = "work-ua"
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/"]

    def parse(self, response):
        pass
