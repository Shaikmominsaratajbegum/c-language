n=int(input("enter how many numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    print("="*40)
    print("numbers with in {}".format(n))
    print("="*40)
    i=1
    while(i<=n):
        print("\t {}".format(i))
        i=i+1
    else:
        print("="*50)