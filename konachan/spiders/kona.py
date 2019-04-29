# -*- coding: utf-8 -*-
import scrapy
#引入定义的item
from  konachan.items import  KonachanItem
# 引入 scrapy 自带的图片爬取通道，注意在setting里面要进行注释。
from  scrapy.pipelines.images import ImagesPipeline

class Kona1Spider(scrapy.Spider):
    name = "kona"
    allowed_domains = ["konachan.net"]
    start_urls = ['http://konachan.net/post']
    cnt=0  #规定要爬取的页数
    def parse(self, response):
        #获得要爬取的url的相对地址
        url_list = response.xpath("//div[@class='inner']//a[@class='thumb']/@href").extract()
        # 获得url的绝对地址
        for url in url_list:
            item1=KonachanItem()
            item1["detailed"] = url
            item1["detailed"] = "http://konachan.net" + item1["detailed"]
            #将绝对地址给第二个解析函数 parse_detail 进行解析
            yield scrapy.Request(
                item1["detailed"],
                callback = self.parse_detail,
                meta={"item":item1}  #meta 以字典的形式传递item信息
            )
        #获得下一页的url
        next_url= response.xpath("//a[@class='next_page']/@href").extract_first()
        next_url='http://konachan.net'+ next_url
        #这里仅仅是测试哈，考虑内存只爬取两页
        if(self.cnt<2):
            self.cnt+=1
            # 回调给自己，继续解析
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
    #定义解析详情页的函数
    def parse_detail(self,response):
        #接受parse函数传递的请求，接受item信息
        item1=response.meta["item"]
        #解析网页
        item1["image_urls"] = response.xpath("//div[@class='content']//img/@src").extract()
        #确定每次都传一个url
        if len(item1["image_urls"])<2:
            item1["image_urls"] = item1["image_urls"]
        yield item1


