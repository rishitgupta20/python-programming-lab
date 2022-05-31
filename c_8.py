def info(a):
    l=len(a)
    b=''
    for i in a:
        if i not in b:
            b=b+i

    l2=len(b)
    if l2==27:
        return "string is panagram"

    else:
        return " string is not panagram"
