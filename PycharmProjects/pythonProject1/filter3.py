
print("Enter List of Values separated by space:")
lst=[ int(val) for val in input().split()]
poslist=list(filter(lambda k: k>0,lst))
neglist=tuple(filter(lambda k: k<0,lst))
print("Given list of values:{}".format(lst))
print("Possitive Values:{}".format(poslist))
print("Negative Values:{}".format(neglist))
