import math
def getfirstdigit(x):
    d=int(math.log10(x))
    res=x//(10**d)
    return res
x=int(input("enter x\n"))
print(getfirstdigit(x))