a=int(input("enter the size"))
b=[]
print("enter the elements of list")
i=0
while(i<a):
    b.append(int(input()))
    i=i+1
print(b)
c=b[::-1]
m=0
for n in range(0,a):
    if c[n]==b[n]:
        m=m+1
if(m==a):
    print("transpose is equal")
else:
    print("not transpose")