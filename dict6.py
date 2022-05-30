# from ast import Break


ls1=list(map(str,input("enter here\n").split()))
ls2=list(map(str,input("enter here\n").split()))
dct=dict(zip(ls1,ls2))
print(dct)
#using dict. comprehension
d={ls1[i]:ls2[i] for i in range(len(ls1))}
print(d)

ls=['a','b','c']
ls2=[1,2,3]
dc={}
for i in range(len(ls)):
    dc[ls[i]]=ls2[i]
print(dc)