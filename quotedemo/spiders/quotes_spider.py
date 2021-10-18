import scrapy
from scrapy.http import FormRequest
from ..items import QuotedemoItem
from scrapy.utils.response import open_in_browser

class QuoteSpider (scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]
    def parse(self, response):
        open_in_browser(response)
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username' : 'karansingh',
            'password' : 'dhichik'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = QuotedemoItem()

        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        #next_page = 'https://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        #if QuoteSpider.page_number < 11:
         #   QuoteSpider.page_number += 1
          #  yield response.follow(next_page, callback=self.parse)