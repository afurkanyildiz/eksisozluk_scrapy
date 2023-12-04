import pymongo
from scrapy.exceptions import DropItem
from .items import EksisoItem


class MongoDBPipeline:
    collection_name = 'api_eksisozluk_entries'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE')

        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            if isinstance(item, dict) and 'entryId' in item:
                existing_entry = self.db[self.collection_name].find_one({'entryId': item['entryId']})
                if existing_entry:
                    print(f"Duplicate entry with entryId {item['entryId']} found. Skipping.")
                else:
                    self.db[self.collection_name].insert_one(item)
                return item
            else:
                raise DropItem(f"Invalid item type or structure: {item}")
        except pymongo.errors.DuplicateKeyError as e:
            print(f"DuplicateKeyError: {e}")
            print(f"Problematic item: {item}")
            raise
