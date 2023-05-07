def fibo():
    n=int(input("enter a numbers:"))
    if(n<0):
        print("ivalid inputs:".format(n))
    else:
        print("fibonacci series number")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(2,n):
            n3=n1+n2
            if(n3<n):
                print(n3)
                n1=n2
                n2=n1
fibo()