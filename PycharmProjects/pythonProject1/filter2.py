def posval(n):
	if n>0:
		return True
	else:
		return False

def negval(n):
	if n<0:
		return True
	else:
		return False

#main program
print("Enter List of Values separated by space:")
lst=[ int(val ) for val in input().split()]
poslist=list(filter(posval,lst))
neglist=tuple(filter(negval,lst))
print("Given list of values:{}".format(lst))
print("Possitive Values:{}".format(poslist))
print("Negative Values:{}".format(neglist))

