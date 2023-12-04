import os

BOT_NAME = "scrapy_project"

SPIDER_MODULES = ["scrapy_project.spiders"]
NEWSPIDER_MODULE = "scrapy_project.spiders"

ROBOTSTXT_OBEY = True


DJANGO_CONNECTION_STRING = 'http://127.0.0.1:8000'

ITEM_PIPELINES = {
    "scrapy_project.pipelines.MongoDBPipeline": 300,
}

MONGO_URI =os.getenv('MONGO_URI')

MONGO_DATABASE = 'gundems'


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


