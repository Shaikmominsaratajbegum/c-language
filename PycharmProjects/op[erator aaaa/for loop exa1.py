n=int(input("enter how many numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    print("numbers from 1 to {} ".format(n))
    for i in range(1,n+1):
        print("{}".format(i))
    print()
    print("=======")
    for i in range(n,0,-1):
        print("{}".format(i))
    print()
    print("--------")
