n=int(input("enter how many mul tables u want:"))
if(n<=0):
    print("invalid input{}".format(n+1))
else:
    for num in range(1,n):
        print("mul table for{}".format(num))
        for i in range(1,11):
            print("\t{}x{}={}".format(num,i,num*i))