# -*- coding: utf-8 -*-

import time

#当前时间戳
print time.time()
print time.localtime(time.time())
print time.strftime("%Y-%m-%d", time.localtime())

# time.strptime 可以把时间格式化成时间元组 tuple
timeDay = raw_input('time(yyyy-mm-dd):')

day = time.strptime(timeDay, "%Y-%m-%d").tm_yday

print '第',day , '天'

#最好根据输入做一下正则验证
