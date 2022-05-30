def prime_or_not(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
lst=[2,4,7,3,14,10,67]
res=[]
for i in lst:
    if prime_or_not(i):
        res.append(i)
print(res)


