from scrapy import Spider
from aistartups.items import AistartupsItem

#spider of A.I Drug Discovery Pipeline 

class AiStartupsSpider(Spider):
    name = 'aistartups_spider'
    allowed_urls = ['https://blog.benchsci.com']
    start_urls = ['https://blog.benchsci.com/startups-using-artificial-intelligence-in-drug-discovery#understand_mechanisms_of_disease']

    def parse(self, response):
        rows = response.xpath('//*[@id="hs_cos_wrapper_post_body"]/div')


        for row in rows:
            company = row.xpath('./div[2]/h4/a//text()').extract_first() 
            if not company:
                continue
            use = row.xpath('./div[2]/p/text()[1]').extract_first().replace(':','').replace('.','').strip() 
            purpose = row.xpath('./div[2]/p/text()[2]').extract_first().replace(':','').replace('.','').strip() 
            founded = int(row.xpath('./div[2]/p/text()[3]').extract_first().replace(':','').replace('.','').strip())
            headquarters = row.xpath('./div[2]/p/text()[4]').extract_first().replace(':','').replace('.','').strip() 

            item = AistartupsItem()
            item['company'] = company
            item['use'] = use
            item['purpose'] = purpose
            item['founded'] = founded
            item['headquarters'] = headquarters
        

            yield item

           
