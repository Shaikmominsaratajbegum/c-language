n=int(input("enter how many numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    i=1
    while(i<=n):
        print("\t {}".format(i))
        i=i+2