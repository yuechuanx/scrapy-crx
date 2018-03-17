import scrapy
from Scrapy_CRX.items import ScrapyCrxItem
import json
import os


class CRXSpider(scrapy.Spider):
    name = "crx"

    base_url = 'https://openi.nlm.nih.gov/retrieve.php?q=&coll=cxr&m='
    img_base_url = 'https://openi.nlm.nih.gov/'

    param_min = 1
    param_max = 30

    start_urls = []

    while param_max <= 7470:
        url = base_url + str(param_min) + "&n=" + str(param_max)
        start_urls.append(url)
        param_min += 30
        param_max += 30


    def parse(self, response):
        filename = []
        problem = []
        img_url = []

        # print(response)
        json_data = json.loads(response.body_as_unicode())
        for i in json_data['list']:
            filename.append(os.path.split(i['imgLarge'])[1])
            problem.append(i['Problems'])
            img_url.append(self.img_base_url + i['imgLarge'])

        for i in range(len(filename)):
            label = ScrapyCrxItem()
            label['filename'] = filename[i]
            label['problem'] = problem[i]
            label['img_url'] = img_url[i]
            yield label
