n=int(input("enter how many numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    i=n
    while(i>=1):
        print("\t {}".format(i))
        i=i-1
    else:
        print("="*40)