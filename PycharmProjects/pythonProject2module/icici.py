bname="icici"
addr="hyd"
def simpleint():
    p=float(input("enter a principle amount:"))
    t=int(input("enter a time: "))
    r=int(input("entera rate:"))
    si=p*t*r/100
    totamt=p+si
    print("simple intersest details")
    print("\t principle amount:{}".format(p))
    print("\t time {}".format(t))
    print("\t rate{}".format(r))
    print("\t totamt to pay:{}".format(totamt))