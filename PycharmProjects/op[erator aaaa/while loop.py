n=int(input("enter how many numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    print("numbers from 1 to {} ".format(n))
    i=1
    while(i<=n):
        print("\t{}".format(i),end="\t")
        i=i+1
    else:
        print()
        print("numbers from {} to 1".format(n),end="\t")
        i=n
    while(i>=1):
            print("\t{}".format(i),end="\t")
            i=i-1
    else:
        print()
        print("===")

