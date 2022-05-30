def fact_recursive(n):
    if n==0 or n==1:
        return 1
    else :
        return n* fact_recursive(n-1)
out= fact_recursive(5)
print(out)