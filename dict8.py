dct={'eng':24,'maths':17,'elec':23,'python':18}
c=0
for i in dct:
    if c<dct[i]:
        c=dct[i]
print(c)
for i in dct:
    if c>dct[i]:
        c=dct[i]
print(c)

