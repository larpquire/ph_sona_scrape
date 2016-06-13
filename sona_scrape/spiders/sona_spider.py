# -*- coding: utf-8 -*-

# spider

import scrapy

from sona_scrape.items import SonaScrapeItem, SonaItemLoader


class SonaSpider(scrapy.Spider):
    name = 'sona'
    start_urls = ['http://www.gov.ph/past-sona-speeches/']

    
    def parse(self, response):
        
        for sel in response.xpath('//td[2]/a|//td[3]/a'):
            url = response.urljoin(sel.xpath('./@href').extract_first())
            
            loader = SonaItemLoader(SonaScrapeItem())
            loader.add_value(
                'title',
                sel.xpath('./text()').extract_first()
            )
            
            request = scrapy.Request(url, callback=self.parse_dir_contents)
            request.meta['loader'] = loader
            
            yield request
    
    
    def parse_dir_contents(self, response):
        loader = response.meta['loader']
        loader.add_value(
            'author',
            response.css('h1.entry-title').xpath('./text()').extract_first()
        )
        loader.add_value(
            'delivered',
            response.xpath('//time/@datetime').extract_first()
        )
        loader.add_value(
            'text',
            response.css('div.entry-content').xpath('.//p/text()').extract()
        )
        
        yield loader.load_item()
