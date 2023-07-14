import scrapy
import json
from licence.items import LicenceItem
import re


class ShanghaiSpider(scrapy.Spider):
    name = "shanghai"
    # allowed_domains = ["xk.scjgj.sh.gov.cn/"]
    start_urls = []

    def start_requests(self):
        url = 'https://xk.scjgj.sh.gov.cn/xzxk_wbjg/query/public/licInfo'
        for i in range(31):
            postdata = {"zszl":"00101,00102","fzjg":"","rows":50,"page":i+1,"xkzbh":"sc"}
            yield scrapy.http.JsonRequest(
                        url=url,
                        callback=self.parse_pages,
                        data=postdata
                    )
    

    def parse_pages(self, response):
        url = "https://xk.scjgj.sh.gov.cn/xzxk_wbjg/query/public/licenceDetail"
        data = json.loads(response.text)['data']['resultList']
        for res in data:
            postdata = {"id": res['id'], 
                        "xkzh": res['xkzbh'],
                        "licenceType":res['sqsxdm']}
            yield scrapy.http.JsonRequest(
                        url=url,
                        callback=self.parse,
                        data=postdata
                    )


    def parse(self, response):
        foodlicence = json.loads(response.text)
        item = LicenceItem()

        item['producer_name'] = foodlicence.get('jyzmc','')
        item['credit_code'] = foodlicence.get('shxydm','')
        item['legal_representative'] = foodlicence.get('fddbrFzr','')
        item['residence'] = foodlicence.get('zs','')
        item['address'] = foodlicence.get('jycs','')
        item['food_category'] = foodlicence.get('sccplbmc','')
        item['licence_number'] = foodlicence.get('xkzbh','')
        item['issuing_authority'] = foodlicence.get('fzjgmc','')
        item['issue_date'] = foodlicence.get('yxqq','')
        item['validate_period'] = foodlicence.get('yxqz','')

        details = foodlicence['pdVo']['apprFoproductDetailsList']
        for detail in details:
            item['detailed_categories'] = detail.get('splb','')
            item['category_number'] = detail.get('lbbh','')
            item['category_name'] = detail.get('lbmc','')
            item['variety_details'] = detail.get('pzmx','')
            item['notes'] = detail.get('bz','')

            yield item
