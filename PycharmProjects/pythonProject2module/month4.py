from calendar import  month as m1, calendar as c
m=int(input("enter a month number:"))
if m in range(1,13):
    y=int(input("enter the year:"))
    print(m1(y,m))
    year=int(input("enter which year calendar u want:"))
    print(c(year))
else:
    print("{} is invalid month".format(m))

