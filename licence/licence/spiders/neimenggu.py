import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from licence.items import LicenceItem
import random
import os
import csv


class NeimengguSpider(scrapy.Spider):
    name = "neimenggu"
    start_urls = []

    def __init__(self):
        # # 浏览器路径
        # binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')  
        # # 驱动路径
        # self.driver = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe", firefox_binary=binary)
        options = webdriver.ChromeOptions()
        # 设置Chrome浏览器无头模式
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
    
    def process_item(self, item):
        file_path = './neimenggu_licence.csv'
        if not os.path.isfile(file_path):
            is_first_write = 1
        else:
            is_first_write = 0
        if item:
            with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)
                if is_first_write:
                    header = [
                        '企业名称','许可证编号','社会信用代码','法定代表人',"住所",
                        '生产地址','食品类别','发证机关',
                        '发证日期','证书有效期','明细类别名称','明细类别编号','品种明细','备注'
                    ]
                    writer.writerow(header)
                writer.writerow(
                    [item[key] for key in item.keys()])
        return item

    def isnull(self,text):
        if text is None:
            return ''
        else:
            return text

    def start_requests(self):

        url_origin = 'http://117.161.154.157:7011/dc/jsp/dc/industry/query/fooddrug/spschz_info_list.jsp'
        self.driver.get(url_origin)
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="taskGrid_next"]/a'))
        )
        
        start_page = 42
        start_detail = 2
        for page in range(0,519):
            print('page:',page)
            if page < start_page:
                if page > 0:
                    self.driver.find_element(By.XPATH,'//*[@id="taskGrid_next"]/a').click()
                    WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//li[@class='paginate_button active']"),str(page+1)))
                continue
            elif page > 0:
                # 翻页
                self.driver.find_element(By.XPATH,'//*[@id="taskGrid_next"]/a').click()
                WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//li[@class='paginate_button active']"),str(page+1)))
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="taskGrid"]/tbody/tr[1]/td[2]/a')))
            response = self.driver.page_source
            response = HtmlResponse(url='', body=response, encoding='utf-8')
            detail_urls = response.xpath('//*[@id="taskGrid"]/tbody/tr/td[2]/a')
            for i in range(len(detail_urls)):
                if page == start_page and i < start_detail:
                    continue
                
                WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,"//li[@class='paginate_button active']"),str(page+1)))
                try:
                    self.driver.find_element(By.XPATH,f'//*[@id="taskGrid"]/tbody/tr[{i+1}]/td[2]/a').click()
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ENT_NAME"]')))
                except Exception as e:
                    print(e)
                    continue
                try:
                    time.sleep(0.5)
                    response = self.driver.page_source
                    response = HtmlResponse(url='', body=response, encoding='utf-8')

                    item = LicenceItem()
            
                    item['producer_name'] = self.isnull(response.xpath('//*[@id="ENT_NAME"]/text()').extract_first()).strip()
                    item['licence_number'] = self.isnull(response.xpath('//*[@id="LICENSE_NO"]/text()').extract_first()).strip()
                    item['credit_code'] = self.isnull(response.xpath('//*[@id="ENT_SC_CODE"]/text()').extract_first()).strip()
                    item['legal_representative'] = self.isnull(response.xpath('//*[@id="LEGAL_PRESENT_NAME"]/text()').extract_first()).strip()
                    item['residence'] = self.isnull(response.xpath('//*[@id="ADDRESS"]/text()').extract_first()).strip()
                    item['address'] = self.isnull(response.xpath('//*[@id="ENGAGE_PLACE"]/text()').extract_first()).strip()
                    item['food_category'] = self.isnull(response.xpath('//*[@id="MAIN_FORMAT_CODE"]/text()').extract_first()).strip()
                    
                    item['issuing_authority'] = self.isnull(response.xpath('//*[@id="CERTIFICATION_ORGAN_NAME"]/text()').extract_first()).strip()
                    item['issue_date'] = self.isnull(response.xpath('//*[@id="CERTIFICATION_DATE"]/text()').extract_first()).strip()
                    item['validate_period'] = self.isnull(response.xpath('//*[@id="VALIDITY_TO"]/text()').extract_first()).strip()

                    tbody = self.driver.find_elements(By.XPATH,'//*[@id="productGrid"]/tbody/*')
                    count = len(tbody)

                    for j in range(count):
                        idx = j+1
                        item['detailed_categories'] = self.isnull(response.xpath(f'//*[@id="productGrid"]/tbody/tr[{idx}]/td[2]/span/text()').extract_first()).strip()

                        item['category_number'] = self.isnull(response.xpath(f'//*[@id="productGrid"]/tbody/tr[{idx}]/td[3]/span/text()').extract_first()).strip()

                        item['variety_details'] = self.isnull(response.xpath(f'//*[@id="productGrid"]/tbody/tr[{idx}]/td[5]/span/text()').extract_first()).strip() + ';' + self.isnull(response.xpath(f'//*[@id="productGrid"]/tbody/tr[{idx}]/td[6]/span/text()').extract_first()).strip()
                        
                        item['notes'] = self.isnull(response.xpath(f'//*[@id="productGrid"]/tbody/tr[{idx}]/td[7]/span/text()').extract_first()).strip()

                        self.process_item(item)
                except Exception as e:
                    print(e)
                    print(f'page:{page+1}, detail:{i+1}')
                finally:
                    self.driver.back()
            
    
    def close(self):
        self.driver.close()

    def parse(self, response):
        pass