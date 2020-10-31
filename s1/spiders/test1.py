# -*- coding: utf-8 -*-
import scrapy
import urllib
import urllib.request
import xml.etree.ElementTree
from s1.items2 import Clole1Item

class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['w.atwiki.jp']
    start_urls = ['https://www5.atwiki.jp/hmiku/tag/%E6%AE%BF%E5%A0%82%E5%85%A5%E3%82%8A?&p=0']

    def parse(self, response):
        for title in response.css('div.cmd_tag li'):
            item = Clole1Item()
            
            link = 'https:' + title.css('a::attr(href)').extract_first()
            link2 = response.urljoin(link)
            print(link2)
            yield scrapy.Request(link2,
                                 callback=self.parse_detail,
                                 meta={'item': item})


    def parse_detail(self, response):
        print("check1")
        item = response.meta['item']
        item['title'] = response.css('div#wikibody a::attr(title)').extract_first()
        item['body']= response.css('div#wikibody div::text').extract()
        temp = response.css('div#wikibody iframe::attr(src)').extract_first()
        s = temp[temp.rfind('sm'):]
        print('抽出したアドレス：',s)
        item['date']= self.test(s)
        yield item




    def getthumbinfo(self, video_id):
        u = urllib.request.urlopen('http://ext.nicovideo.jp/api/getthumbinfo/' + video_id)
        t = u.read()
        u.close()
        return t

    def test(self, video_id):
        x = self.getthumbinfo(video_id)
        e = xml.etree.ElementTree.XML(x)
        status = e.get('status')
        if status == 'ok':
            thumb = list(e)[0]
            first_retrieve = thumb.find('first_retrieve').text
            return first_retrieve
        else:
            return 'none'
