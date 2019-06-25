import scrapy
from scrapy.spiders import CrawlSpider


class ProductsSpider(CrawlSpider):
    max_pages = 3
    name = "products"
    start_urls = [
        "http://www.instrument.in.ua/bolgarki_uglovye_shlifovalnye_mashiny/c134/page/1/"
    ]
    next_page = "http://www.instrument.in.ua/bolgarki_uglovye_shlifovalnye_mashiny/c134/page/1/"

    def parse(self, response):
        for product in response.css('div.products div.product_item'):
            yield {
                'title': product.css('div.product_item_title a::text').extract(),
                'desc': product.css('div.product_item_text::text').extract_first(),
                'price': product.css('div.products_list_price::text').extract(),
                'img': response.urljoin(product.css('div.product_item_title img::attr(src)').extract_first()),
            }

        self.next_page = self.next_page[:-2] + str((int(self.next_page[76]) + 1)) + "/"

        next_page = self.next_page
        if next_page is not None and int(next_page[76]) <= self.max_pages:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)