import scrapy
from licence.items import LicenceItem
import json


class FujianSpider(scrapy.Spider):
    name = "fujian"
    allowed_domains = ["220.160.53.129"]
    start_urls = []

    def start_requests(self):
        base_url = "https://220.160.53.129:8192/kong/kong-gateway/lic-online-service/onlinePub/getProdLicenseList"    
        for i in range(403):
            data = {"condition":{"holderName":"","licNo":"","licStatus":["10"]},"current":f'{i+1}',"size":'30'}
            yield scrapy.http.JsonRequest(
                        base_url,
                        callback=self.parse_pages,
                        data=data
                    )
    

    def parse_pages(self, response):
        base_url = "https://220.160.53.129:8192/kong/kong-gateway/lic-online-service/onlinePub/getFoodProdLicense"
        data = json.loads(response.text)
        data = data['data']['records']
        for record in data:
            id = record['id']
            licno = record['licNo']
            postdata = {"id":id,"licNo":licno}
            yield scrapy.http.JsonRequest(
                        base_url,
                        callback=self.parse_detail_page,
                        data=postdata
                    )
    

    def parse_detail_page(self, response):
        data = json.loads(response.text)
        data = data['data']
        item = LicenceItem()

        foodlicence = data.get('foodProdLicense','')
        item['producer_name'] = foodlicence.get('holderName','')
        item['credit_code'] = foodlicence.get('socialCreditCode','')
        item['legal_representative'] = foodlicence.get('legalPrincipal','')
        item['residence'] = foodlicence.get('regAddressDetail','')
        item['address'] = foodlicence.get('prodAddressDetail','')
        item['food_category'] = foodlicence.get('foodType','')
        item['licence_number'] = foodlicence.get('licNo','')
        item['issuing_authority'] = foodlicence.get('issueOrgName','')
        item['issue_date'] = foodlicence.get('issueDate','')
        item['validate_period'] = foodlicence.get('validityDateEnd','')

        try:
            details = data['prodProductToDoLvl3']
            for detail in details:
                item['detailed_categories'] = detail.get('typeName','')
                item['category_number'] = detail.get('foodTypeCode','')
                item['category_name'] = detail.get('foodTypeCodeName','')
                item['variety_details'] = detail.get('foodTypeDetail','')
                item['notes'] = detail.get('foodRemark','').strip()

                yield item
        except:
            yield item



    def parse(self, response):
        pass
