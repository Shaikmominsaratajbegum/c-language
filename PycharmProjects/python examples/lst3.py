print("enter a list of elemrnts separated by cooma:")
lst=[int(val) for val in input().split(",") if int(val)%2==0 and int(val)>0]
print("list of +ve value even numbers={}".format(lst))
print("enter a list of elemrnts separated by cooma:")
olst=[int(val) for val in input().split(",") if int(val)%2!=0 and int(val)>0]
print("list of +ve value odd numbers={}".format(olst))


