n=int(input("enter n value"))
if(n<=0):
    print("Invalid input")
if(n%2==0):
    print("{} is even".format(n))
if(n%2>0):
    print("{} is odd".format(n))