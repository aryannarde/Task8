import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        bookdata= response.css("h3 > a::attr(title)").getall()
        for title in bookdata:
            yield {
                'Booktitle':title
            }
