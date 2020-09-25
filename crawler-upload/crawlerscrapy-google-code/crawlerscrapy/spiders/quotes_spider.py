import scrapy


class DmozSpider(scrapy.Spider):  
    name = "quotes"
    start_urls = [
        'https://code.google.com/archive/p/opensudoku-android/issues/173',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
