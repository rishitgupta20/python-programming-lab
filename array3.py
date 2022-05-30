import numpy as np
m,n=map(int,input().split(' '))
a=np.array(list(map(int,input().split(' ')))).reshape(m,n)
tr=np.transpose(a)
fl=np.ravel(a)
print(tr)
print(fl)