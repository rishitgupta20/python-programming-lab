def sum(inti_sum=0,*elements):
    res=inti_sum
    for x in elements:
        res=res+x
    return res
print(sum(5,20,20,30))
print(sum(0,1))
print(sum())