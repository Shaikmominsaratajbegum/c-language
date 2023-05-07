print("enter list of old salary empolyees:")
oldlist=[int(sal) for sal in input().split() if int(sal)>0]
newlist=list(map(lambda sal:sal+sal*1.1,oldlist))
print("------------")
print("\t oldlist \t\t newlist")
print("===========")
for ol,nl in zip(oldlist,newlist):
    print("\t{}\t\t{}".format(ol,nl))