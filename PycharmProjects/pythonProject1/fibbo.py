def calfact():
    n=int(input("enter a factorial number:"))
    if(n<0):
        print("inavalid input:".format(n))
    else:
        f=1
        for i in range(1,n):
            f=f*i
        print("fact({})={}".format(f,n))
calfact()
calfact()