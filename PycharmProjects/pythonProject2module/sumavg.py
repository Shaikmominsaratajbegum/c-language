n=int(input("Enter How many numbers sum and avg u want to Find:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("Content of list=",lst)
        #logic for finding sum and avg
        s=0
        for val in lst:
            s+=val
        else:
            print("Sum=",s)
            print("Avg={}".format(s/len(lst)))
