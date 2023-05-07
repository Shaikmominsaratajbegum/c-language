def  addop(a,b):
	c=a+b
	return c
#--------------------------------------------------------
sumop=lambda a,b:a+b # Anonymous function Definition

#main program
x=float(input("Enter First value:"))
y=float(input("Enter Second value:"))
res=addop(x,y) # Normal function call
print("type of addop=",type(addop))
print("sum by using Normal Functions=",res)
print("----------------------------------------------------")
result=sumop(x,y) # Anonymous function  call
print("type of sumop=",type(sumop))
print("sum by using Anonymous Functions=",result)
