p=float(input("enter a principle amount:"))
t=float(input("enter a time:"))
r=float(input("enter a rate:"))
si=p*t*r/100
totamt=si+p
print("principle amount={}".format(p))
print("time={}".format(t))
print("rate={}".format(r))
print("="*50)
print("simple interest on amount:{}".format(si))
print("total amount to pay:{}".format(totamt))
