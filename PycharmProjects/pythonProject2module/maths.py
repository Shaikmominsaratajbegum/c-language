def factorial(n):
    if(n<0):
        print("Invalid input={}".format(n))
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        else:
            print("factorial of number({})={}".format(n,f))

