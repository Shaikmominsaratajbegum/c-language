print("enter list of valued separated by space:")
vals=input()
print(vals,type(vals))
lst=vals.split()
print(lst,type(lst))
finallist=[int(val) for val in lst]
print("final list of values={}".format(finallist))