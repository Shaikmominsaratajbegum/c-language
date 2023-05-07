tpl=(10,20,5,-6,2,14,15)
d=dict([(val,val**2) for val in tpl ])
print("-"*50)
print("Given Number\tSquare")
print("-"*50)
for n,sn in d.items():
    print("\t{}\t\t\t{}".format(n,sn))
print("-"*50)