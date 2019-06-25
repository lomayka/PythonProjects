import scrapy


class ArticlesSpider(scrapy.spiders.CrawlSpider):
    name="articles"
    start_urls = [
        "https://www.ukraine-is.com/uk/category/podorozhi-po-ukra%D1%97ni/page/3/",
        "https://www.ukraine-is.com/uk/category/podorozhi-po-ukraїni/page/2/"
    ]

    def parse(self, response):
        for text in response.xpath("//div[@class='content-area']"):
            yield {
                'url': response.url,
                'text': text.select("//p/text()").extract(),
                'images': text.select('//img/@src').extract(),
            }
        for a in response.xpath("//article").xpath(".//a[@class='btn btn-link continue-link']"):
            yield response.follow(a, callback=self.parse)

