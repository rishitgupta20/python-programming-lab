f=open("sample.txt","a")
a=int(input())
for i in range(a):
  name=input("Enter name to store : ")
  f.write(name)
  f.write('\n')
f.close()