# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import win_unicode_console
win_unicode_console.enable()

class ScrapyCrxPipeline(object):

    def process_item(self, item, spider):
        print(item['filename'])
        print(item['problem'])
        print(item['imr_url'])
        return item
