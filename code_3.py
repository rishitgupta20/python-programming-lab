sum=0
for temp in range(100,1000):
    i=temp
    while i > 0:
        r=i%10
        sum=sum + r**3
        i=i//10
    if sum == temp:
        print(sum)
