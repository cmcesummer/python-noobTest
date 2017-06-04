
#0 1 1 2 3 5 8 13 21



def fib(num):
  arr = [0,1]
  for i in range(num):
    arr.append(arr[-2] + arr[-1])
  return arr

print fib(8)
