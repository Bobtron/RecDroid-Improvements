import scrapy
import os
import shutil
import time

IDpage=0
IDapp=0
CrashID=0
WholeID=0
step=0
pagelimit=1

class DmozSpider(scrapy.Spider):  
    name = "first223"




    def start_requests(self):

        if(os.path.exists('result')):
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
             time.sleep(3)


        #aa="okokok"
        urls = [
           'https://code.google.com/archive/p/moniono/issues/2'
        ]
        for url in urls:
            request=scrapy.Request(url=url, priority=0, callback=self.parse, dont_filter=True)
            yield request


    def parse(self, response):     
        
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


        list=["click","choose","select","launch","pick","tap","open","press","go","select","input","enter","type","insert","fill","change","write","set","put","add","back"]
        global WholeID
        WholeID+=1
        IDpagePara=1
        IDappPara=1


        # store the whole ID information
        filename = './result/whole/wholeId-%d-page-%d-appid-%d.html' % (WholeID,IDpagePara,IDappPara)
        with open(filename, 'wb') as f:
               f.write(bytes(response.url, encoding="utf8"))
               f.write(response.body)





        sentencelist=response.css('markdown-widget')
        crashTag=False
        reproduceTag=False
        rotateTag=False
        global CrashID
        #this is for tags

        if len(sentencelist)==0:# may be there is no any markdown-widget
           return

        sentence=sentencelist[0]

	

        if("crash" in sentence.extract().lower() or "exception" in sentence.extract().lower() or "failure" in sentence.extract().lower() or "error" in sentence.extract().lower()): 
               if not crashTag:
                  crashTag=True
                  CrashID+=1
               #print("what is page limit")

        if("steps will reproduce the problem" in sentence.extract().lower() or any(word in sentence.extract().lower() for word in list)):
               reproduceTag=True
               print("lunarlunar111")

        if("rotat" in sentence.extract() or "Rotat" in sentence.extract()):
               rotateTag=True

        if rotateTag and crashTag:
           filename = './result/rotate/wholeId-%d-quotes-%d-page-%d-appid-%d.html' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 f.write(bytes(response.url, encoding="utf8"))
                 f.write(response.body)


        if crashTag:
           filename = './result/crashontop/wholeId-%d-quotes-%d-page-%d-appid-%d' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 sentence=sentencelist[0]
                 f.write(bytes(sentence.extract(), encoding="utf8"))

        if reproduceTag:
           filename = './result/allsteps/wholeId-%d-quotes-%d-page-%d-appid-%d' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 sentence=sentencelist[0]
                 f.write(bytes(sentence.extract(), encoding="utf8"))

        if crashTag and reproduceTag:
           filename = './result/allstepscrash/wholeId-%d-quotes-%d-page-%d-appid-%d' % (WholeID,CrashID,IDpagePara,IDappPara)
           with open(filename, 'wb') as f:
                 sentence=sentencelist[0]
                 f.write(bytes(sentence.extract(), encoding="utf8"))

	
        #sentencelist=response.css('markdown-widget')
        #for sentence in sentencelist:
        '''
            if("crash" in sentence.extract().lower() or "exception" in sentence.extract().lower() or "failure" in sentence.extract().lower() or "error" in sentence.extract().lower()): 
                print("what is my print")
                print(sentence.extract())
                global CrashID
                print("what is the current ID")
                print(CrashID)
                print("what is the current page")
                print(response.url)
                filename = './result/wholecrashes/quotes-%d-page-%d-isssue-%d.html' % (CrashID,IDpagePara,IDappPara)
                with open(filename, 'wb') as f:
                     f.write(bytes(response.url, encoding="utf8"))
                     f.write(response.body)
            
            if("rotat" in sentence.extract() or "Rotat" in sentence.extract()):


                     filename = './result/rotate/quotes-%d-page-%d-isssue-%d.html' % (CrashID,IDpagePara,IDappPara)
                     with open(filename, 'wb') as f:
                          f.write(bytes(response.url, encoding="utf8"))
                          f.write(response.body)
         '''


            #WholeID+=1















#scrapy crawl first> log 2>&1

