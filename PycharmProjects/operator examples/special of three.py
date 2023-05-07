a=float(input("enter first value:"))
b=float(input("enter second value:"))
c=float(input("enter third value:"))
res=a if (a<=b>c) else b if (a<b>=c) else c if (a<=c>b) else "all values are equal"
print("big({},{},{})={}".format(a,b,c,res))
