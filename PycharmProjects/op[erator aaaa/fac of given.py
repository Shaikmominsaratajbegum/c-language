n=int(input("enter a number:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("factors of {}".format(n))
    for i in range(1,(n//2)+1):
        if(n%i==0):
            print("\t{}".format(i))