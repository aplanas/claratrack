import scrapy


class VertbaudetSpider(scrapy.Spider):
    name = "vertbaudet"
    allowed_domains = ["vertbaudet.es"]
    # start_urls = ['https://vertbaudet.es/']

    def start_requests(self):
        start_url = "https://vertbaudet.es/"
        sections = (
            "ropa-premama",
            "bebe",
            "nina",
            "nino",
            "calzado",
            "puericultura",
            "habitacion-y-organizacion",
            "textil-hogar-y-decoracion",
            "juguetes",
        )
        for section in sections:
            yield scrapy.Request(url=f"{start_url}{section}.htm", callback=self.parse)

    def parse(self, response):
        for product in response.css("div.product"):
            yield {
                "name": product.css("div.title a::text").get().strip(),
                "price": product.css("span.price::attr(data-price)").get(),
            }
