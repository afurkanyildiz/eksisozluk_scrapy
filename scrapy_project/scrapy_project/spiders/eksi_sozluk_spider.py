import scrapy
from datetime import datetime


class EksiSozlukSpider(scrapy.Spider):
    name = 'eksisozlukspider'
    start_urls = ['http://eksisozluk1923.com']

    def process_entry(self, title, entry, entry_date_from_scape, title_id):
        entry_item = {
            'titleId': title_id,
            'title': title.strip() if title else None,
            'author_profile_link': entry.css('a.entry-author::attr(href)').get(),
            'author': entry.css('a.entry-author::text').get().strip(),
            'entryId': entry.css('li::attr(data-id)').get(),
            'content': entry.css('div.content').xpath('string()').get().strip(),
            'entry_date': entry.css('a.entry-date::text').get(),
            'entry_date_from_scape': entry_date_from_scape
        }
        return entry_item

    def parse(self, response):
        for link in response.css('ul.topic-list li a::attr(href)').extract():
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_topic)

    def parse_topic(self, response):
        title = response.css('span[itemprop="name"]::text').get()
        title_id = response.css('h1#title::attr(data-id)').get()

        entries = self.extract_entries(response)
        for entry in entries:
            entry_date_from_scape = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield self.process_entry(title, entry, entry_date_from_scape, title_id)

        total_pages = int(response.css('div.pager::attr(data-pagecount)').get())
        for page_number in range(2, total_pages + 1):
            next_page_url = f'{response.url}&p={page_number}'
            yield scrapy.Request(url=next_page_url, callback=self.parse_page)

    def parse_page(self, response):
        title = response.css('span[itemprop="name"]::text').get()
        title_id = response.css('h1#title::attr(data-id)').get()

        entries = self.extract_entries(response)
        for entry in entries:
            entry_date_from_scape = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield self.process_entry(title, entry, entry_date_from_scape, title_id)

    def extract_entries(self, response):
        return response.css('ul#entry-item-list li')
