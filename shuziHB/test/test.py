# -*- coding:utf-8 -*-
from datetime import datetime
day = datetime.now().strftime('%m-%d')
print(day)

# md5
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import hashlib
md5 = hashlib.md5()
md5.update('官方公告】关于卡拉特取消涨跌停制度的通知'.encode("utf-8"))
print(md5.hexdigest())

from datetime import datetime
now = datetime.now().strftime()

str = '2017-06-22'
cday = datetime.strptime(str,'%Y-%m-%d')
print(cday.strftime('%Y%m%d'))