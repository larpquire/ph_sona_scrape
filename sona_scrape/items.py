# -*- coding: utf-8 -*-

# Model for the scraped SONA data

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst


class SonaScrapeItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    delivered = scrapy.Field()
    text = scrapy.Field()


class SonaItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    
    author_in = MapCompose(lambda x: x.split(',')[0])
    
    delivered_in = MapCompose(lambda x: x.replace('T', ' '))
    
    text_in = MapCompose(unicode.strip)
    text_out = Join(separator='\r\n')
