from random import randint

op = []
for i in range(4):
    a = randint(0, 9)
    op.append(a)

op = list(map(str, op))
otp = ''.join(op)
print(otp)
