a=float(input("enter first value:"))
b=float(input("enter second value:"))
c=float(input("enter third value:"))
res = a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "all values are equal"
print("big({},{},{})={}".format(a,b,c,res))
