from shuziHB.spiders.tool.fileHandle import writeFile,readFile,fileTruncate
import json

fileName = 'szzcData'

def szzcParse(response):

    if response is not None and response.body is not None:
        jsonRespons = json.loads(response.body.decode('utf-8'))
        for obj in jsonRespons['result']:
            # 读取szzc记录
            content = readFile(fileName)
            if len(content) > 0:
                content_json = json.loads(content[0])
