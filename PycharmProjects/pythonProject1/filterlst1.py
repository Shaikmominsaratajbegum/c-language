print("enter a list of values separatec by  space:")
lst=[ int(val ) for val in input().split()]
print("given list of values:{}".format(lst))
elist=list(filter(lambda k: (k%2==0) and k>0,lst))
olist=list(filter(lambda k:(k%2!=0) and k>0,lst))
print("even number:{}".format(elist))
print("odd number:{}".format(olist))