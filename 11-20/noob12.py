# -*- coding: utf-8 -*-

#11就是斐波那契数列， 这是12 素数
import math

arr = []
for i in range(101,201):
  for j in range(2, int(math.ceil(i / 2)) + 1):
    if i % j == 0:
      break
  else :
    arr.append(i)

print 'length: ', len(arr), 'arr:', arr
