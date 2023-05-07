a=float(input("enter a value:"))
b=float(input("enter b value:"))
res = a if a>b else b if b>a else "both are equal"
print("big({},{})={}".format(a,b,res))