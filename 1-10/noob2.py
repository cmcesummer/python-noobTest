# -*- coding: UTF-8 -*-

money = int(raw_input('输入净利润（万元）：'))
moneyArr = [10, 20, 40, 60, 100]
pointArr = [0.1, 0.075, 0.05, 0.03, 0.15, 0.1]

#似乎没有 for( i<length) 的
#也没有三元表达式 不过 Boolean and a or b 就是三元表达式了
total = 0
for item in range(len(moneyArr)):
  if money > moneyArr[item] :
    total += (item == 0 and 10 or moneyArr[item] - moneyArr[item-1]) * pointArr[item]
    if money > 100 or money <= moneyArr[item + 1]:
      total += (money - moneyArr[item]) * pointArr[item + 1]
  elif money <= 10:
    total += money * 0.1
    break

print total

#如果倒着来算确实简单一些  就跟他例子一样
