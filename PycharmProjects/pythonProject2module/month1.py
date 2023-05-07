import calendar
m=int(input("enter a month number:"))
if m in range(1,13):
    y=int(input("enter the year:"))
    print(calendar.month(y,m))
else:
    print("{} is invalid month".format(m))

