def check(l):
    a=l[0]
    b=l[1]
    c=0
    while(a>=b):
        a=a-b
        c=c+1
    return c
l=list(map(int,input().split()))
print(check(l))