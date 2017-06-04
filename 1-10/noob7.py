# -*- coding: utf-8 -*-

# 7,8,9,10 都在这里了

import time
for i in range(1,10):
  if(i != 1):
    print
  for j in range(1, i+1):
    time.sleep(1)
    print '%d * %d = %d' % (i, j, i*j)
    print time.localtime(time.time())
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
