hike=lambda sal:sal*(10/100)
#main program
oldlist=[10,20,30,50]
mapobj=map(hike,oldlist)
newlist=list(mapobj)l
print("===========================")
print("\t old list\t new list")
print("============================")
for ol,nl in zip(oldlist,newlist):
    print("\t{} \t\t{}".format(ol,nl))
