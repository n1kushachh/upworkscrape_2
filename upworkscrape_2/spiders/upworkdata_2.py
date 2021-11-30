import scrapy
from scrapy.loader import ItemLoader
from upworkscrape_2.items import Upworkscrape2Item
from scrapy import Request

class Upworkdata2Spider(scrapy.Spider):
    name = 'upworkdata_2'
    
    new_link = []
    link = 'https://www.advisoryexcellence.com/experts-search/?fwp_paged='
    for x in range(1, 262):
        new_link.append(link+str(x))

    def start_requests(self):
        for link in self.new_link:
            yield scrapy.Request(link, callback=self.parse_info)

    def parse_info(self, response):
        for content in response.xpath('.//div[@class="entry-content-wrapper clearfix laywer_overview_wrapper"]'):
            l = ItemLoader(item=Upworkscrape2Item(), selector=content)
            l.add_xpath('name',      './/div[2]/div[@class="laywer_overview_wrap_all_info"]/div[@class="laywer_overview_name_etc"]/span[@class="lawyer_overview_title"]/following-sibling::text()[1]')
            l.add_xpath('firm_name', './/div[2]/div[@class="laywer_overview_wrap_all_info"]/div[@class="laywer_overview_name_etc"]/span[@class="lawyer_overview_firm"]/following-sibling::text()[1]')
            l.add_xpath('expertise', './/div[2]/div[@class="laywer_overview_wrap_all_info"]/div[@class="laywer_overview_name_etc"]/span[@class="lawyer_overview_practice"]/b/following-sibling::text()[1]')
            l.add_xpath('email',     './/span[@class="__cf_email__"]/@data-cfemail')

            yield l.load_item()
