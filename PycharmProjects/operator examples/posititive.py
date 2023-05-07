n=int(input("enter n number"))
res="+ve" if n>0 else "-ve" if n<0 else "zero"
print("{} is {}".format(n,res))