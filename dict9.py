dct={'name':'rishit','sec':'f','rolln':40,'Name':'rishit'}
ls=[]
res=dict()
for key,val in dct.items():
    if val not in ls:
        ls.append(val) 
        res[key]=val
print(res)