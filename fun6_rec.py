def sum(num):
    if num<=1:
        return num
    return num + sum(num-1)
out=sum(int(input("enter the number")))
print(out)
# NOT IN SYLLABUS
