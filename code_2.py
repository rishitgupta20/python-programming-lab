year=int(input("Enter year to be checked:"))
print("The year is a leap year!") if(year%4==0 and year%100!=0 or year%400==0) else print("The year isn't a leap year!")
