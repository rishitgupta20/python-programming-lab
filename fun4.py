def greater(x,y,z):
    if x>y:
        if x>z:
            return x
        else :
            return z
    else : 
         if y>z:
             return y
         else:
            return z
                 
num1=int(input("enter the number\n"))
num2=int(input("enter the number\n"))
num3=int(input("enter the number\n"))
out= greater(num1,num2,num3)
print(out)
