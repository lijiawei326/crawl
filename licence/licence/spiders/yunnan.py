import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By


class YunnanSpider(scrapy.Spider):
    name = "yunnan"
    start_urls = ['http://gsxt.ynaic.gov.cn/xzxk_wbjg/#/licenceListscjgj']

    def __init__(self):
        options = webdriver.ChromeOptions()
        # 设置Chrome浏览器无头模式
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    
    def start_requests(self):
        url = 'http://gsxt.ynaic.gov.cn/xzxk_wbjg/#/licenceListscjgj'
        self.driver.get(url)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/section/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/input').click()
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        search = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/section/div/div[2]/form/div[4]/div/div/div/button')
        
        sc_search = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/section/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/input')
        sc_search.send_keys('sc')
        search.click()
    
    def close(self):
        self.driver.close()



    def parse(self, response):
        pass