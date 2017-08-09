# -*- coding: utf-8 -*-
from datetime import datetime
from shuziHB.spiders.tool.emailTool import sendEmail
from shuziHB.spiders.tool.fileHandle import writeFile
from shuziHB.spiders.tool.strTool import isEqual,strMd5
from shuziHB.spiders.tool.urlTool import urlShort

def btc9_parse(response):
    newList = response.css(".newlist");
    for news in newList:
        for new in news.xpath("tr/td"):
            day = new.xpath("span/text()").extract()[0]
            title = new.xpath("a/span/text()").extract()[0]
            content = "http://" + response.meta['download_slot'] + new.xpath("a/@href").extract()[0]
            contentShort =  urlShort(content,content)

            nowDay = datetime.now().strftime('%m-%d')
            contentMd5 = strMd5((day + content).encode('utf-8'))
            if isEqual('btc9Data',contentMd5):
                continue
            writeFile('btc9Data',contentMd5)
            sendEmail('币久 ' + title,contentShort)



