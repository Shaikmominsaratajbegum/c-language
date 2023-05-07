import functools
print("enter list of number separated by space:")
lst=[int(val) for val in input().split()]
res=functools.reduce(lambda a,b:a+b,lst)
print("sum",res)