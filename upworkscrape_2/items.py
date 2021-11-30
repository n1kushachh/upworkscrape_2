# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose,TakeFirst
from w3lib.html import remove_tags, strip_html5_whitespace


def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email 

class Upworkscrape2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    firm_name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    expertise = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    email = scrapy.Field(input_processor = MapCompose(remove_tags, cfDecodeEmail), output_processor = TakeFirst())  
