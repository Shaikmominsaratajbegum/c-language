import functools
print("enter list of number separated by space:")
lst=[int(val) for val in input().split()]
s=set(lst)
if(len(s)==1):
    print("max({})={}".format(lst,"all values are equal"))
    print("min({})={}".format(lst,"all values are equal"))
else:
    maxv=functools.reduce(lambda k,v:k if k>v else v,lst)
    minv=functools.reduce(lambda x,y:x if x<y else y,lst)
    print("max({})={}".format(lst,maxv))
    print("min({})={}".format(lst,minv))

