a=float(input("enter a value:"))#
b=float(input("enter b value:"))
small = a if a<b else b if b<a else"both are same value"
print("small({},{})={}".format(a,b,small))