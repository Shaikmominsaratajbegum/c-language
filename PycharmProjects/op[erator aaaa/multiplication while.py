n=int(input("enter a number u want generate:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    for i in range(1,11):
        print("{} X {}={}".format(n,i,n*i))
