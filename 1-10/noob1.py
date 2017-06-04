# -*- coding: UTF-8 -*-

#可进行更少的循环
arr = range(1,5)
lastArr = []
for one in arr:
  arrTwo = arr[:]
  arrTwo.remove(one)
  for two in arrTwo:
    arrThree = arrTwo[:]
    arrThree.remove(two)
    for three in arrThree:
      lastArr.append([one,two,three])

print lastArr
