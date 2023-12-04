# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class EksisoItem(scrapy.Item):
    titleId = scrapy.Field()
    title = scrapy.Field()
    author_profile_link = scrapy.Field()
    author = scrapy.Field()
    entryId = scrapy.Field()
    content = scrapy.Field()
    entry_date = scrapy.Field()
    entry_date_from_scape = scrapy.Field()