import numpy as n
s=int(input())
a=n.array(list(map(int,input().split(' '))))
o=a.reshape(s,s)
print(o)