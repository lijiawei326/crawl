# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import csv


class LicenceCsvPipeline(object):
    def process_item(self, item, spider):
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


class FujianLicenceCsvPipeline(object):
    def process_item(self, item, spider):
        file_path = './fujian_licence.csv'
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
                        '发证日期','证书有效期','明细类别名称','明细类别编号','类别名称','品种明细','备注'
                    ]
                    writer.writerow(header)
                writer.writerow(
                    [item[key] for key in item.keys()])
        return item

