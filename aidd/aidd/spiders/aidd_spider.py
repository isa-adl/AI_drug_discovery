from scrapy import Spider
from aidd.items import AiddItem

#spider of A.I Drug Discovery Pipeline 

class AiddSpider(Spider):
    name = 'aidd_spider'
    allowed_urls = ['https://blog.benchsci.com']
    start_urls = ['https://blog.benchsci.com/drugs-in-the-artificial-intelligence-in-drug-discovery-pipeline']

    def parse(self, response):
        rows = response.xpath('//*[@id="hs_cos_wrapper_post_body"]/div[2]/div')

        for row in rows:
            company = row.xpath('./div[1]//text()').extract_first()
            drug = row.xpath('./div[2]//text()').extract_first()
            therapeutic_area = row.xpath('./div[3]//text()').extract_first()
            indication = row.xpath('./div[4]//text()').extract_first() 
            stage = row.xpath('./div[5]/div/text()').extract_first()

            item = AiddItem()
            item['company'] = company
            item['drug'] = drug
            item['therapeutic_area'] = therapeutic_area
            item['indication'] = indication
            item['stage'] = stage
        

            yield item

            