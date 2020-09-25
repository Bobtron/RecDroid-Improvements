import scrapy
import os
import shutil
import time

IDpage=0
IDapp=0
CrashID=0
WholeID=0
step=0
pagelimit=25

class DmozSpider(scrapy.Spider):  
    name = "first2"




    def start_requests(self):

        if(os.path.exists('result')):
            print 'HERERERERERERERERERERER'
            shutil.rmtree('result')
            os.makedirs("result")
            os.makedirs("result/tracefiles")
            os.makedirs("result/tracefiles2")
            os.makedirs("result/allsteps")
            os.makedirs("result/wholecrashes")
            os.makedirs("result/rotate")
            os.makedirs("result/allstepscrash")
            os.makedirs("result/whole")
            os.makedirs("result/crashontop")
            os.makedirs("result/merged")
            time.sleep(3)
        else:
            print 'NOT HERERERERERERERERERE'
            print os.getcwd()

        #aa="okokok"
        urls = [
           'https://code.google.com/archive/search?q=domain:code.google.com%20label:Android&page=1'
        ]
        for url in urls:
            request=scrapy.Request(url=url, priority=0, callback=self.parse, dont_filter=True)
            yield request


    def parse(self, response):     
        #print(response.body)
        global IDpage
        #print("what is the current ID")
        IDpage+=1
        #print(ID)
        #print("what is the current page")
        print(response.url)
        page = response.url.split("/")[-1]
        filename = './result/tracefiles/quotes-pageid-%d.html' % IDpage
        with open(filename, 'wb') as f:
            # resp = bytes(response.url, encoding="utf8")
            resp = bytes(response.url)
            f.write(resp)
            f.write(response.body)
      #  self.log('Saved file %s' % filename)

#################################3

        for href in response.css('div.maia-cols div.maia-col-8 p a[ng-if]::attr(href)'):
            global step
            step+=1
            print("what is current step")
            print(step)
            print(href)
            yield response.follow(href, priority=2, meta={'item' : IDpage}, callback=self.parse_findissues)
        
        global pagelimit
        pagelimit-=1
        if(pagelimit>0):
             print("what is page limit")
             print(pagelimit)

             for link in response.css('a.ng-scope'):
                 if("Next" in link.css('::text').extract()[0]):
                    newpage=link.css('::attr(href)').extract()[0]
                    yield response.follow(newpage, priority=1, callback=self.parse)
        
    def parse_findissues(self, response):
        #############
        #b=self.aa
        IDpagePara=response.meta['item']
        print("what is the page ID")
        print(IDpagePara)

        global IDapp
      #  print("what is the current ID")
        IDapp+=1
        print("what is the current page lunar1")
        print(response.url)
        filename = './result/tracefiles2/quotes-%d-pageid-%d.html' % (IDapp,IDpagePara)
        with open(filename, 'wb') as f:
                     # f.write(bytes(response.url, encoding="utf8"))
                     f.write(bytes(response.url))
                     f.write(response.body)
        for link in response.css('span[ng-hide] li a'):
            if(link.css('::text').extract()[0]=="Issues"):
                 href=link.css('::attr(href)').extract()[0]
                 yield response.follow(href, priority=3, meta={'item' : IDpagePara , 'IDapp': IDapp}, callback=self.parse_buglist)
        
    def parse_buglist(self, response):
        IDpagePara=response.meta['item']
        IDappPara=response.meta['IDapp']



        for href in response.css('table tbody tr.ng-scope td a::attr(href)').extract():

             print("issue url")
             print(response.url)
             yield response.follow(href, priority=5, meta={'item' : IDpagePara , 'IDapp': IDappPara}, callback=self.parse_bugreport)
        
        for link in response.css('a[ng-if].ng-scope'):
            if("Next" in link.css('::text').extract_first()):
                    newpage=link.css('::attr(href)').extract_first()
                    yield response.follow(newpage, priority=4, meta={'item' : IDpagePara , 'IDapp': IDappPara}, callback=self.parse_buglist)
        
    def parse_bugreport(self,response):
        '''
        global ID
        print("what is the current ID")
        ID+=1
        print(ID)
        print("what is the current page")
        print(response.url)
        filename = './files/quotes-%d.html' % ID
        with open(filename, 'wb') as f:
                     f.write(bytes(response.url, encoding="utf8"))
                     f.write(response.body)
        '''


        #list=["click","choose","select","launch","pick","tap","open","press","go","select","input","enter","type","insert","fill","change","write","set","put","add","back"]
        global WholeID
        WholeID+=1
        IDpagePara=response.meta['item']
        IDappPara=response.meta['IDapp']



        # store the whole ID information
        filename = './result/whole/wholeId-%d-page-%d-appid-%d.html' % (WholeID,IDpagePara,IDappPara)
        with open(filename, 'wb') as f:
               # f.write(bytes(response.url, encoding="utf8"))
               f.write(bytes(response.url))
               f.write(response.body)
               f.close()





        sentencelist=response.css('markdown-widget p')

        crashTag=False
        reproduceTag=False
        rotateTag=False
        global CrashID
        #this is for tags
        if len(sentencelist)==0:# may be there is no any markdown-widget
            print 'NO MARKDOWN WIDGET'
            return

        sentence=sentencelist[0]
        # print 'SENTENCE ' + sentence
        # print 'SENTENCE EXTRACT '

	

        if("crash" in sentence.extract().lower() or "exception" in sentence.extract().lower() or "failure" in sentence.extract().lower() or "error" in sentence.extract().lower()): 
               if not crashTag:
                  crashTag=True
                  CrashID+=1
               #print("what is page limit")

        if("steps will reproduce the problem" in sentence.extract().lower()):# or any(word in sentence.extract().lower() for word in list)):
               reproduceTag=True
               print("lunarlunar111")

        if("rotat" in sentence.extract() or "Rotat" in sentence.extract()):
               rotateTag=True

        if reproduceTag:
           filename = './result/allsteps/wholeId-%d-quotes-%d-page-%d-appid-%d.html' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 # f.write(bytes(response.url, encoding="utf8"))
                 f.write(bytes(response.url))
                 f.write(response.body)
                 f.close()

        if crashTag and reproduceTag:
           filename = './result/allstepscrash/wholeId-%d-quotes-%d-page-%d-appid-%d.html' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 # f.write(bytes(response.url, encoding="utf8"))
                 f.write(bytes(response.url))
                 f.write(response.body)
                 f.close()

        mergeTag = False
        merged_list = ["same issue", "merged", "duplicate","merge"]
        for i in merged_list:
            if i in sentence.extract().lower():
                mergeTag=True

        if mergeTag:
            filename = './result/merged/wholeId-%d-quotes-%d-page-%d-appid-%d.html' % (WholeID,CrashID,IDpagePara,IDappPara)
            with open(filename, 'wb') as f:
                # f.write(bytes(response.url, encoding="utf8"))
                f.write(bytes(response.url))
                f.write(response.body)
                f.close()
       


            #WholeID+=1















#scrapy crawl first2> log 2>&1

