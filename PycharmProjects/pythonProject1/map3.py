print("enter list of old salary empolyees:")
lst=[int(sal) for sal in input().split() if int(sal)>0]
squarelist=list(map(lambda n:n**2,lst))
sqrtlist=list(map(lambda n:n**0.5,lst))
print("\tgiven number\tsquare\tsqrt")
for gn,sqv,sqrtv in zip(lst,squarelist,sqrtlist):
    print("\t{}\t{}\t\t{}".format(gn,sqv,sqrtv))


