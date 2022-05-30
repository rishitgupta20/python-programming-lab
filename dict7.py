dct={'eng':24,'maths':17,'elec':23,'python':18}
ls=[]
dc={}
for key in dct:
    ls.append(key)
ls.sort()
for i in ls:
    dc[i]=dct[i]
print(dc)
# 
dct={'name':'rishit','sec':'f','rolln':40}
print(sorted(dct))
