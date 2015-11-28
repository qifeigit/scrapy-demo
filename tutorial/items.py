import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    dataPositon = scrapy.Field()
    job_desc = scrapy.Field()
    company = scrapy.Field()
