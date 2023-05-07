n=int(input("Enter How many Random Mul tables u want generate:")) # n=4
if(n<=0):
	print("{} is invalid input".format(n))
else:
	#create an empty list for storing different Numerical Integer values
	lst=list()
	for i in range(1,n+1):
		val=int(input("Enter {} Value :".format(i)))
		lst.append(val)
	else:
		print("="*50)
		print("Given List={}".format(lst)) # [15, 18, -3, 0, 17, 19, 24, 25, -4, 45]
		print("="*50)
		for num in lst: #outer for loop---supply the numbers
			if(num<=0):pass
				#print("{} is invalid Input--No Mul table".format(num))
			else:
				print("="*50)
				print("\tMul Table for:{}".format(num))
				print("="*50)
				for i in range(1,11): # Inner Loop--generates mul table for random numbers
					print("\t{} x {} = {}".format(num,i,num*i))
				else:
					print("="*50)