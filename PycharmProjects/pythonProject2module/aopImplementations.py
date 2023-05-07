def readvalues(op):
    a=int(input("enter first value for '{}':".format(op)))
    b=int(input("enter second value for'{}':".format(op)))
    return a,b
def addop():
    a,b=readvalues("addtion")
    print("sum({},{})={}".format(a,b,a+b))
def subop():
    a,b=readvalues("substarction")
    print("sub({},{})={}".format(a,b,a-b))
def mulop():
    a,b=readvalues("multiplication")
    print("mul({},{})={}".format(a,b,a*b))
def divop():
    a,b=readvalues("division")
    print("div({},{})={}".format(a,b,a/b))
def fdivop():
    a,b=readvalues("division")
    print("div({},{})={}".format(a,b,a//b))
def mdivop():
    a,b=readvalues("modulo division")
    print("mdiv({},{})={}".format(a,b,a%b))
def expop():
    a,b=int(input("enter base:")),int(input("enter a power"))
    print("sum({},{})={}".format(a,b,a**b))



