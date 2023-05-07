n=int(input("enter n value:"))
res="invalid input" if n<0 else "even" if n%2==0 else "odd"
print("{} is {}".format(n,res))
