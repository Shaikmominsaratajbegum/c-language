n=int(input("enter how many natural numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    print("+"*50)
    print("sum of {} natural numbers ")
    print("="*50)
    s=0
    i=1
    while(i<=n):
        s=s+i
        print("{}".format(i),end=" ")
        i=i+1
    else:
        print()
        print("{} sum on first n natural numbers".format(s))


