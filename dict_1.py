dct={'name':'rishit','sec':'f','rolln':40}
lst={'name':'ram','sec':6, 'class':9}
#3ways to merge 2 dictionary
# 1
dct.update(lst)
print(dct)
# 2
for key in lst:
    dct[key]=lst[key]
print(dct)
# 3
for a,b in lst.items():
    dct[a]=b
print(dct)
