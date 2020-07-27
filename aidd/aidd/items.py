# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AiddItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    drug = scrapy.Field()
    therapeutic_area = scrapy.Field()
    indication = scrapy.Field()
    stage = scrapy.Field()
    
