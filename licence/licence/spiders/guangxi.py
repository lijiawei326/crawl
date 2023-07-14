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


class GuangxiSpider(scrapy.Spider):
    name = "guangxi"
    start_urls = []

    def __init__(self):
        # 浏览器路径
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')  
        # 驱动路径
        self.driver = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe", firefox_binary=binary)
    
    def process_item(self, item):
        file_path = './guangxi_licence.csv'
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

    def start_requests(self):

        url_origin = 'https://entp.yjj.gxzf.gov.cn/appnet/appEntpList.action?entpType=007'
        self.driver.get(url_origin)
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/table[2]/tbody/tr/td[2]/a'))
        )
        
        for page in range(356,384):
            # if page > 0:
            #     # time.sleep(1)
            #     next_page = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f"//a[@onclick='return gotoPage({page} + 1);']")))
            #     next_page.click()
            #     # self.driver.find_element(By.XPATH,f"//a[@onclick='return gotoPage({page} + 1);']").click()
            self.driver.find_element(By.XPATH,f'/html/body/div/div[1]/div/div/form/select/option[{page+1}]').click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div/table[2]/tbody/tr/td[2]/a')))
                # time.sleep(4)
            response = self.driver.page_source
            response = HtmlResponse(url='', body=response, encoding='utf-8')
            detail_urls = response.xpath('/html/body/div/div[1]/div/table[2]/tbody/tr/td[2]/a')
            for i in range(len(detail_urls)):
                if page == 356 and i < 0:
                    continue
            # for i in range(1):
                
                    # time.sleep(1)
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f"//a[@onclick='return gotoPage({page+1} + 1);']")))
                self.driver.find_element(By.XPATH,f'/html/body/div/div[1]/div/table[2]/tbody/tr[{i+1}]/td[2]/a').click()
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/table/tbody/tr[1]/td[2]')))
                try:
                    time.sleep(0.5)
                    response = self.driver.page_source
                    response = HtmlResponse(url='', body=response, encoding='utf-8')

                    item = LicenceItem()
            
                    item['producer_name'] = response.xpath('/html/body/div[2]/table/tbody/tr[1]/td[2]/text()').extract_first().strip()
                    item['licence_number'] = response.xpath('/html/body/div[1]/fieldset/table/tbody/tr[2]/td[1]/text()').extract_first().strip()
                    item['credit_code'] = response.xpath('/html/body/div[2]/table/tbody/tr[3]/td[2]/text()').extract_first().strip()
                    item['legal_representative'] = response.xpath('/html/body/div[3]/table/tbody/tr/td[2]/text()').extract_first().strip()
                    item['residence'] = response.xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/text()').extract_first().strip()
                    item['address'] = response.xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/text()').extract_first().strip()
                    item['food_category'] = response.xpath('/html/body/div[4]/table/tbody/tr/td[2]/text()').extract_first().strip()
                    
                    item['issuing_authority'] = response.xpath('/html/body/div[1]/fieldset/table/tbody/tr[2]/td[5]/text()').extract_first().strip()
                    item['issue_date'] = response.xpath('/html/body/div[1]/fieldset/table/tbody/tr[2]/td[4]/text()').extract_first().strip()
                    item['validate_period'] = response.xpath('/html/body/div[1]/fieldset/table/tbody/tr[2]/td[3]/text()').extract_first().strip()

                    tbody = self.driver.find_elements(By.XPATH,'/html/body/div[5]/fieldset/table/tbody/*')
                    count = len(tbody)

                    for j in range(count-1):
                        idx = j+2
                        item['detailed_categories'] = response.xpath(f'/html/body/div[5]/fieldset/table/tbody/tr[{idx}]/td[2]/text()').extract_first().strip()

                        item['category_number'] = ''

                        item['variety_details'] = response.xpath(f'/html/body/div[5]/fieldset/table/tbody/tr[{idx}]/td[3]/text()').extract_first().strip()
                        
                        item['notes'] = ''

                        self.process_item(item)
                except:
                    print(f'page:{page+1}, detail:{i+1}')
                finally:
                    self.driver.back()
    
    def close(self):
        self.driver.close()

    def parse(self, response):
        pass