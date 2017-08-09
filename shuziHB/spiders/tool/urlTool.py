# -*- coding: utf-8 -*-
from urllib import request
import json

def urlShort(url=str,defaultUrl=str):
    shortUrl = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long='
    with request.urlopen(shortUrl+url) as f:
        data = f.read()
        if data is not None:
            json_data = json.loads(data.decode('utf-8'))
            return json_data[0]['url_short']
        return defaultUrl
print(urlShort('https://www.btc9.com/Art/details/id/462.html','www.btc9.com/Art/details/id/462.html'))