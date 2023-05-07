digitdict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
d=int(input("enter a any digit:"))
res=digitdict[d] if digitdict.get(d)!=None else "number"
print("{} is {}".format(d,res))