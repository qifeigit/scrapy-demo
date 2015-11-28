import scrapy
import json
from tutorial.items import DmozItem
from scrapy.http import Request 
str1 = "http://www.lagou.com/jobs/positionAjax.json?px=default&yx=15k-25k&first=false&pn=2&kd=%E7%88%AC%E8%99%AB"
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    	str1
    ]
    def parse(self, response):
    	obj = json.loads(response.body)
    	result = obj['content']['result']
    	for data in result:
    		yield Request(url='http://www.lagou.com/jobs/'+bytes(data['positionId'])+'.html', callback=self.parse_dataPosition, dont_filter=True)
    def parse_dataPosition(self,response):
    	 item = DmozItem()
    	 item['desc'] = response.xpath("//dd[@class='job_bt']/p/text()").extract()
         item["company"] =  response.xpath("//dl[@class='job_detail']//h1/div/text()").extract()
    	 return item
