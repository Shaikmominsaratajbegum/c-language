n=int(input("enter a number u want generate:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    i=1
    while(i<11):
        print("{} X {}={}".format(n,i,n*i))
        i=i+1