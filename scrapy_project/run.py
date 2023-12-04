from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_project.spiders.eksi_sozluk_spider import EksiSozlukSpider


process = CrawlerProcess(get_project_settings())
process.crawl(EksiSozlukSpider)
process.start()