import scrapy
import json
from licence.items import LicenceItem
import re


class ZhejiangSpider(scrapy.Spider):
    name = "zhejiang"
    allowed_domains = ["zjamr.zj.gov.cn"]
    start_urls = []


    def start_requests(self):
        base_url = "https://ydoa.zjamr.zj.gov.cn:8050/DoAjax.ashx?Flag=getSearchDataList&tabid=1A9CA5C107A74A80AE5CCF0AEF1F21AF&page={}&keyword={}"
        for i in range(101,133):
            keyword = 'SC' + str(i)
            page = '1'
            url = base_url.format(page, keyword)
            yield scrapy.Request(url=url, callback=self.parse_pages, meta={'keyword':keyword})
    

    def parse_pages(self, response):
        base_url = "https://ydoa.zjamr.zj.gov.cn:8050/DoAjax.ashx?Flag=getSearchDataList&tabid=1A9CA5C107A74A80AE5CCF0AEF1F21AF&page={}&keyword={}"
        data = json.loads(response.text)[0]
        rowcount = int(data['rowcount'])
        page_num = rowcount // 100 + 1
        keyword = response.meta.get('keyword')
        for page in range(page_num):
            url = base_url.format(str(page+1), keyword)
            yield scrapy.Request(url=url, callback=self.parse_one_page)
    

    def parse_one_page(self, response):
        base_url = 'https://ydoa.zjamr.zj.gov.cn:8050/DoAjax.ashx?Flag=getSearchData&tabid=1A9CA5C107A74A80AE5CCF0AEF1F21AF&dataid={}'
        data = json.loads(response.text)[0]
        data_ids = [i['data_id'] for i in data['rowdata']]
        for id in data_ids:
            url = base_url.format(id)
            yield scrapy.Request(url=url, callback=self.parse_detail_page)


    def parse_detail_page(self, response):
        data = json.loads(response.text)[0]
        data = data['rowdata'][0]
        item = LicenceItem()

        item['producer_name'] = data['str_1'].replace('%','\\').encode().decode('unicode_escape')
        item['credit_code'] = data['str_10'].replace('%','\\').encode().decode('unicode_escape')
        item['legal_representative'] = data['str_11'].replace('%','\\').encode().decode('unicode_escape')
        item['residence'] = data['str_12'].replace('%','\\').encode().decode('unicode_escape')
        item['address'] = data['str_2'].replace('%','\\').encode().decode('unicode_escape')
        item['food_category'] = data['str_3'].replace('%','\\').encode().decode('unicode_escape')
        item['licence_number'] = data['str_4'].replace('%','\\').encode().decode('unicode_escape')
        item['issuing_authority'] = data['str_5'].replace('%','\\').encode().decode('unicode_escape')
        item['issue_date'] = data['str_6'].replace('%','\\').encode().decode('unicode_escape')
        item['validate_period'] = data['str_7'].replace('%','\\').encode().decode('unicode_escape')

        details = data['str_8'].split('%3C/br%3E%3C/br%3E')
        for detail in details:
            detail = detail.split('%3C/br%3E')
            detail = [d.replace('%','\\').encode().decode('unicode_escape') for d in detail]
            try:
                item['detailed_categories'] = re.search(r'食品、食品添加剂类别：.+', detail[0]).group()[11:] if len(detail[0]) > 11 else ''
            except:
                print(item['licence_number'])
            try:
                item['category_number'] = re.search(r'类别编号：.+', detail[1]).group()[5:] if len(detail[1]) > 5 else ''
            except:
                print(item['licence_number'])
            try:
                item['category_name'] = re.search(r'类别名称：.+', detail[2]).group()[5:] if len(detail[2]) > 5 else ''
            except:
                print(item['licence_number'])
            try:
                item['variety_details'] = re.search(r'品种明细：.+', detail[3]).group()[5:] if len(detail[3]) > 5 else ''
            except:
                print(item['licence_number'])
            try:
                item['notes'] = re.search(r'备注：.*', detail[4]).group()[3:] if len(detail[4]) > 3 else ''
            except:
                print(item['licence_number'])

            yield item



    def parse(self, response):
        pass

