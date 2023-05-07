n=int(input("enter how many factorial  numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    f=1
    for i in range(n,0,-1):
        f=f*i
    else:
        print("fact{}!={}".format(n,f))