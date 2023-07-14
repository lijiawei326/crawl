# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LicenceItem(scrapy.Item):
    # define the fields for your item here like:
    producer_name = scrapy.Field()
    licence_number = scrapy.Field()
    credit_code = scrapy.Field()
    legal_representative = scrapy.Field()
    residence = scrapy.Field()
    address = scrapy.Field()
    food_category = scrapy.Field()
    
    issuing_authority = scrapy.Field()
    issue_date = scrapy.Field()
    validate_period = scrapy.Field()
    detailed_categories = scrapy.Field()
    category_number = scrapy.Field()
    # category_name = scrapy.Field()
    variety_details = scrapy.Field()
    notes = scrapy.Field()