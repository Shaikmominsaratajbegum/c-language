line=input("Enter a Line of Text:")
print("-"*50)
print("Given line  : {}".format(line)) # HYD IS THE CAPITAL OF TS
print("-"*50)
words=line.split()
print("Given words={}".format(words)) # ['HYD', 'IS', 'THE', 'CAPITAL', 'OF', 'TS']
print("-"*50)
for word in words: # Outer loop supply Words
	noc=0
	for ch in word: # Inner loop counts number of chars in a word
		noc+=1
	else:
		print("\t{}--->{}".format(word,noc))
else:
	print("-"*50)
