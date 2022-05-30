a=input("enter the string")
n=int(input("enter the node"))
r=int(input("enter the number of repitation"))
b=''
c=''
l=len(a)
for i in range(n,l):
    if a[i]!=' ':
        b=b+a[i]
for i in range(0,n):
    if a[i]!=' ':
        c=c+a[i]
print(*((b+c)*r))