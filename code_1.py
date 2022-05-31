import random as r
a=r.randint(1,100)
for i in range(8):
    b=int(input())
    if b>a:
        print("You enter greater no.")
    elif b<a:
        print("You enter smaller no.")
    elif b==a:
        print('congrats you won !')
else:
    print("sorry!,better luck next time")
