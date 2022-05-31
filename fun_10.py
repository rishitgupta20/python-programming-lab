def vote_or_not(age):
    if age>=18:
        print("your age is :",age,"you are eligible to vote")
    else:
        print("your age is :",age,"you are not eligible to vote")
age=int(input("enter your age : "))
vote_or_not(age)
