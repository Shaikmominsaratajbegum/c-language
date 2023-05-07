from calendar import *
m=int(input("enter a month number:"))
if m in range(1,13):
    y=int(input("enter the year:"))
    print(month(y,m))
    print(calendar(int(input("enter which year caleder u want"))))
else:
    print("{} is invalid month".format(m))

