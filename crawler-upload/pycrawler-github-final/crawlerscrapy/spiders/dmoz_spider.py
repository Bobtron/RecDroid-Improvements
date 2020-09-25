from scrapy.spider import Spider  
from scrapy.selector import Selector  
import scrapy
import copy
import os
import shutil
import time


appId=0
issueId=0
CrashID=0

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    def start_requests(self):
        if(os.path.exists('result')):
           shutil.rmtree('result')
        os.makedirs("result")
        os.makedirs("result/allsteps")
        os.makedirs("result/allstepscrash")
        os.makedirs("result/appPage")
        os.makedirs("result/rotate")
        os.makedirs("result/wholeissue")
        os.makedirs("result/wholecrashes")
        time.sleep(3)


        #aa="okokok"
        urls = [
           #'https://github.com/topics/android-app'
           'file:///home/yu/workspace1/all-crawlers/old/pycrawler-github-final/Topic:android-app-GitHub.html'
           #'file:///home/yu/workspace1/pycrawler2/Topic:%20android-app%20%C2%B7%20GitHub.html'
           #'https://jobs.et/jobs/?searchId=<id>&action=search&page=<page>'
        ]
        for url in urls:
            request=scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            yield request
        print("okokok")


    def parse(self, response):

        for href in response.css('article.border-bottom div.d-flex h3.f3 a::attr(href)'):
            print(href)
            global appId
            appId+=1
            yield response.follow(href, meta={'item' : appId}, callback=self.parse_openapp)
            #time.sleep(30)
        print('asdasd')

    def parse_openapp(self,response):
        appIdPara=response.meta['item']
        filename = './result/appPage/appid-%d.html' % appIdPara
        with open(filename, 'wb') as f:
                     f.write(bytes(response.url, encoding="utf8"))
                     f.write(response.body)
                     time.sleep(1)
                     f.close()        
        print("one page Id")
        print(appIdPara)




        for link in response.css('nav span[itemscope]'):
            linkcopy=copy.deepcopy(link)
            if(link.css('span[itemscope] span[itemprop] ::text').extract()[0]=="Issues"):
               print("luu1")
               href=link.css('a ::attr(href)').extract_first()
               print(href)
               yield response.follow(href, meta={'item' : appIdPara}, callback=self.parse_openissues)


    def parse_openissues(self,response):
         appIdPara=response.meta['item']
         for href in response.css('div.Box-row div.d-table div.float-left a.link-gray-dark ::attr(href)'):
             print("luu2")
             print(href)
             yield response.follow(href, meta={'item' : appIdPara}, callback=self.parse_oneissue)

         
         for href in response.css('div.paginate-container div.pagination a.next_page ::attr(href)'):
                   print("luu4")
                   print(href)
                   yield response.follow(href, meta={'item' : appIdPara}, callback=self.parse_openissues)



    def parse_oneissue(self,response):
         appIdPara=response.meta['item']
         print("luu3")
         global issueId
         issueId+=1

         filename = './result/wholeissue/issueId-%d-appId-%d.html' % (issueId, appIdPara)
         with open(filename, 'wb') as f:
              f.write(bytes(response.url, encoding="utf8"))
              f.write(response.body)
              time.sleep(1)
              f.close()

         #sentencelist=response.css('meta[name="description"] ::attr(content)') this one get a wrong place
         sentencelist=response.css('task-lists table.d-block tbody.d-block tr.d-block td.d-block')

         #for sentence in sentencelist:
         sentence=sentencelist[0]
         if(True):
             list=["click","choose","select","launch","pick","tap","open","press","go","select","input","enter","type","insert","fill","change","write","set","put","add","back","2."]
             if("reproduce" in sentence.extract().lower() or any(word in sentence.extract().lower() for word in list)):
               filename = './result/allsteps/appId-%d-issueId-%d.html' % (appIdPara, issueId)
               with open(filename, 'wb') as f:
                    f.write(bytes(response.url, encoding="utf8"))
                    f.write(response.body)
                    time.sleep(1)
                    f.close()

               #print("what should be record as steps")
               print(sentence.extract())

             if("crash" in sentence.extract().lower() or "exception" in sentence.extract().lower() or "failure" in sentence.extract().lower() or "error" in sentence.extract().lower()): 
                global CrashID
                print("what is the current ID")
                CrashID+=1
                print(CrashID)
                print("what is the current page")
                filename = './result/wholecrashes/issueId-%d-appId-%d-crashId-%d.html' % (issueId, appIdPara,CrashID)
                with open(filename, 'wb') as f:
                    f.write(bytes(response.url, encoding="utf8"))
                    f.write(response.body)
                    time.sleep(1)
                    f.close()
                     #f.write(sentence.extract())
 
                if("rotat" in sentence.extract() or "Rotat" in sentence.extract()):
                     filename = './result/rotate/issueId-%d-appId-%d-crashId-%d.html' % (issueId, appIdPara,CrashID)
                     with open(filename, 'wb') as f:
                          f.write(bytes(response.url, encoding="utf8"))
                          f.write(response.body)
                          time.sleep(1)
                          f.close()

                if("reproduce" in sentence.extract().lower() or any(word in sentence.extract().lower() for word in list)):
                     filename = './result/allstepscrash/issueId-%d-appId-%d-crashId-%d.html' % (issueId, appIdPara,CrashID)
                     with open(filename, 'wb') as f:
                         f.write(bytes(response.url, encoding="utf8"))
                         f.write(response.body)
                         time.sleep(1)
                         f.close()




        






         '''
            print("luu1")
            href=link.css('span[itemscope] span[itemprop]::text').extract()[0]
            print(href)

            print("luu2")
            href=link.extract()
            print(href)


            print("luu3")
            href=link.css('a ::attr(href)')
            print(href)
         '''
            #href=linkcopy.extract()
            #print(href)  
        
        #for link in response.css('nav span'):
            #print("luuu1")
            #href=link.extract()
            #print(href)  



            #print(href)
            #global appId
            #appId+=1
            #yield response.follow(href, priority=2, meta={'item' : appId}, callback=self.parse_openapp)

        #yield response.follow(href, priority=2, meta={'item' : appId}, callback=self.parse_openapp)






        #with open(filename, 'wb') as f:
        #    f.write(bytes(response.url, encoding="utf8"))
        #    f.write(response.body)
        #print('asdasd')





'''
class DmozSpider(Spider):  
    name = "dmoz"  
    #allowed_domains = ["dmoz.org"]  
    start_urls = [  
        'https://github.com/topics/android-app'
    ]  
    
    def parse(self, response):
        sel = Selector(response)  
        sites = sel.xpath('//ul[@class="directory-url"]/li')  
        items = []  
        for site in sites:  
            item = DmozItem()  
            item['title'] = site.xpath('a/text()').extract()  
            item['link'] = site.xpath('a/@href').extract()  
            item['desc'] = site.xpath('text()').extract()  
            items.append(item)  
        return items 
'''

#scrapy crawl dmoz> log 2>&1
