import scrapy
import json
from licence.items import LicenceItem
import re

class TianjinSpider(scrapy.Spider):
    name = "tianjin"
    allowed_domains = ["spxk.scjg.tj.gov.cn"]
    start_urls = ["http://spxk.scjg.tj.gov.cn/"]

    def start_requests(self):
        for i in range(10):
            data = {
                'ec_i': 'ec',
                'ec_efn': '',
                'ec_crd': '200',
                'ec_p': str(i+1),
                'ec_s_SCZMC': '',
                'ec_s_SHXYDM': '',
                'ec_s_FDDBR': '',
                'ec_s__5': '',
                "map['FDDBR']":'', 
                "map['SCZMC']": '公司',
                "map['ZS']": '',
                "map['SHXYDM']": '',
                'ec_totalpages': '10',
                'ec_totalrows': '1975',
                'ec_pg': '1',
                'ec_rd': '200'
            }
            url = 'http://spxk.scjg.tj.gov.cn/enterpriseSearch/enterpriseSearchAction!spscList.dhtml'
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_pages)
    
    def parse_pages(self, response):
        ids = response.xpath('//a[@title="详情"]/@onclick').extract()
        ids = [id.split('\'')[1] for id in ids]

        base_url = 'http://spxk.scjg.tj.gov.cn/enterpriseSearch/enterpriseSearchAction!spscView.dhtml?xkzid='
        for id in ids:
            url = base_url + str(id)
            
            yield scrapy.Request(url=url,
                                 callback=self.parse)

    def parse(self, response):

        item = LicenceItem()
        
        item['producer_name'] = response.xpath('//div[@class="la-right"]/text()').extract_first()
        item['licence_number'] = response.xpath('/html/body/div[2]/div/div/div[5]/div[2]/text()').extract_first()
        item['credit_code'] = response.xpath('/html/body/div[2]/div/div/div[3]/div[4]/div[1]/text()').extract_first()
        item['legal_representative'] = response.xpath('/html/body/div[2]/div/div/div[3]/div[4]/div[2]/text()').extract_first()
        item['residence'] = response.xpath('/html/body/div[2]/div/div/div[7]/div[2]/text()').extract_first()
        item['address'] = response.xpath('/html/body/div[2]/div/div/div[8]/div[2]/text()').extract_first()
        item['food_category'] = response.xpath('/html/body/div[2]/div/div/div[4]/div[2]/text()').extract_first()
        
        item['issuing_authority'] = response.xpath('/html/body/div[2]/div/div/div[9]/div[2]/text()').extract_first()
        item['issue_date'] = response.xpath('/html/body/div[2]/div/div/div[10]/div[2]/text()').extract_first()
        item['validate_period'] = response.xpath('/html/body/div[2]/div/div/div[11]/div[2]/text()').extract_first()

        item['detailed_categories'] = response.xpath('/html/body/div[2]/div/div/div[6]/div[2]/text()').extract_first()
        yield item


        
