# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from scrapy import FormRequest
import unicodedata
import numpy as np
import re
from scrapy.item import Item
from scrapy import Field
import urllib

class MyItem(Item):
    image_urls = Field()
    images = Field()
    category=Field()
    subcategory=Field()

class DarazSpider(scrapy.Spider):
    custom_settings={
        "IMAGES_STORE" : '/home/kinaan/Data/daraz/',
        "ITEM_PIPELINES" : {'scrapy.pipelines.images.ImagesPipeline':1}
    }
    name = 'daraz'
    #allowed_domains = ['www.daraz.pk']
    start_urls = ['http://www.daraz.pk/']
    """
    def download(self,category,subcategory,data_url):
        print "download"
        print "in download "
        print category
        print subcategory
        print data_url
        
        characteristics_dict={
            "category":category,
            "subcategory":subcategory,
            "image_url":[data_url],
            #"images":Field()
        }
        print "over here "
        yield characteristics_dict
        #for i in range(length):
        #    file.write(str(array[i]))
        #    file.write('\n')
        #soup=BeautifulSoup(response.body,'lxml')
        #category_name=response.meta['category']
        #subcategory=response.meta['subcategory']
        
        #print "------hi----hi-------___________________________---------"
        #print data_urls
        #print "_______________-ji_------_-"
    """
    def subcategory(self,href,cn,sc):
        
        print "href",href
        yield scrapy.Request(href, callback=self.download, meta={'category':cn,'subcategory':sc})
            
    def subcategory_items(self,response):
        soup=BeautifulSoup(response.body,'lxml')
        category_name=response.meta['category']
        subcategory=response.meta['subcategory']
        counter=response.meta['counter']
        #first_page=response.meta['link']
        #pages=soup.find('section',class_='pagination')
        print "--------------------------------------"
        print "counter = ",counter
        print "--------------------------------------"
        #first_page=soup.select('li.item.-selected')
        #first_page=first_page[0].find('a')['href']
        second_page=soup.select('ul.osh-pagination.-horizontal')
        print second_page
        print type(second_page)
        print len(second_page)
        next_link=None
        if len(second_page)>0:    
            second_page=second_page[0]
            second_page=second_page.find_all('li',class_='item')
            next_page=second_page[-1]
            #print "hello",next_page
            title=next_page.find('a')["title"]
            next_link=None
            if title=="Next":
                next_link=next_page.find('a')["href"]
            #print "first_page ",first_page
            print "next_link ",next_link
            
        #if first_page!=None:
        #    print "calling first page "
        #---------------------------------------------------------------
        soup=BeautifulSoup(response.body,'lxml')
        category_name=response.meta['category']
        subcategory=response.meta['subcategory']
        
        head=soup.find('section',class_='products')
        #print "head",head
        temp1=soup.select('div.sku.-gallery')
        #temp1=head.find_all(attrs={'class':'sku -gallery'})
        temp2=soup.select('div.sku.-gallery.-has-offers')
        #print "temp1",temp1
        #print "temp2",temp2
        products=[]
        products.extend(temp1)
        products.extend(temp2)
        #product_src=soup.select('image.wrapper.default-state')
        #print "length of source files ",len(product_src)
        #print "in function "
        print "_______----------________"
        print " products length ",len(products)
        print "_______----------________"
        #print " inspect ",products[0]
        for prod in products:
            prod_a=prod.find('a',class_='link')
            div=prod.find('div')
            #print div
            img=div.find('img')
            print img
            src=img['data-src']
            print "src",src
            characteristics_dict={
                "category":category_name,
                "subcategory":subcategory,
                "image_urls":[src],
                "images":Field()
            }
            print "before yield"
            yield characteristics_dict
            print "after yield"
            #self.download(category_name,subcategory,src)
            #href=prod_a['href']
        #    self.subcategory(href,category_name,subcategory)
            #print "href",href
        #---------------------------------------------------------------
        link=next_link
        if link!=None:
            yield scrapy.Request(link, callback=self.subcategory_items, meta={'category':category_name,'subcategory':subcategory,'counter':counter+1})
        
        
    def parse(self, response):
        
        soup=BeautifulSoup(response.body,'lxml')
        soups=soup.findAll('li',class_='menu-item')
        array=[]
        for s in soups:
            columns=s.find_all('div',class_='column')
            for col in columns:
                categories=col.find_all('div',class_='categories')
                #print "cats ",categories
                for cat in categories:
                    #print "before initialization ",cat 
                    name=cat.find('a',class_='category')
                    #print "names= ",name
                    #print "andar wala ",c
                    #name=c.find('a',class_='category')
                    if name!=None:
                        #print type(name)
                        name=name.contents[0]
                        #print "final_name ",name
                        #name_href=cat.find('a',class_='category')['href']
                        subcategories=cat.find_all('a',class_='subcategory')
                        for sub in subcategories:
                            sub_name=sub.text
                            sub_href=sub['href']
                            array.append([name,sub_name,sub_href])
        
        #print "hi ", home_body
        #print type(home_body)
        #print len(subcats)
        #print "hello ldlanfkndalkfn ",subcats
        #print "-----------------------------------------"
        length=len(array)
        for i in range(length):
            temp=array[i]
            temp[0]=str(unicodedata.normalize('NFKD', temp[0]).encode('ascii','ignore'))
            temp[1]=str(unicodedata.normalize('NFKD', temp[1]).encode('ascii','ignore'))
            array[i]=[temp[0],temp[1],temp[2]]
        array=np.array(array)
        print "array",array.shape
        for temp in array:
            link=temp[2]
            #link='https://www.daraz.pk/j700h-galaxy-j7-5.5-16-gb-1.5-gb-ram-13-mp-camera-white-brand-warranty-samsung-mpg6434.html'
            print "link ",link
            yield scrapy.Request(link, callback=self.subcategory_items, meta={'category': temp[0],'subcategory':temp[1],'counter':0})
            
        #file=open("workfile","w")
        #for i in range(length):
        #    file.write(str(array[i]))
        #    file.write('\n')
        
        pass
