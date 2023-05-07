print("Enter Number of Numbers to find sum and avg (press @ to stop the input):")
lst=list() # create an empty list
while(True):
    val=input()
    if(val=="@"):
        break
    else:
        lst.append(int(val))
print("--------------------------")
print("Content of list={}".format(lst))
print("--------------------------")
#logic for finding sum and avg
s=0
for val in lst:
    s+=val
else:
    print("Sum={}".format(s))
    print("Avg={}".format(s/len(lst)))
