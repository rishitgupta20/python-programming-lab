def remove_and_strip(string,replace):
    newstr=string.replace(replace,"  ")
    return newstr.strip()
sen="      coder welcome to vs code    "
n=remove_and_strip(sen,"coder")
print(n)