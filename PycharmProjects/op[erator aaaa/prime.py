n=int(input("enter a number"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOTPRIME"
            break
    if(res=="PRIME"):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))