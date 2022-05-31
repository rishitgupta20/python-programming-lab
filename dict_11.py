phonebook={}
num=int(input("enter the len of ph book\n"))
for i in range(num):
    name,mobile=input("enter the information\n").split()
    phonebook[name]=mobile
for i in range(num):
    q=input("enter the name:\n")
    v=phonebook.get(q)
    if v:
        print(f"{q}={v}")
    else:
        print("Not found")

