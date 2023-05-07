print("enter a list of elemrnts separated by cooma:")
lst=[int(val) for val in input().split(",") if int(val)>0]
print("list of values:{}".format(lst))