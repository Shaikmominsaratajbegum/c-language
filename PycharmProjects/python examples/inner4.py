line=input("Enter a Line of Text:")
print("-"*50)
print("Given line  : {}".format(line)) # HYD IS THE CAPITAL OF TS
print("-"*50)
words=line.split()
print("Given words={}".format(words)) # ['HYD', 'IS', 'THE', 'CAPITAL', 'OF', 'TS']
print("-"*50)
#create two empty list objects
vw,cw=[],[]
for word in words: # Outer loop supply Words
	vwres=False
	for ch in word:
		if ch.lower() in ['a','e','i','o','u']:
			vwres=True
			break
	if(vwres):
		vw.append(word)
print("\nVowel Words=",vw)
print("-------------------------------------------------------------")
for word in words: # Outer loop supply Words
	vwres=False
	for ch in word:
		if ch.lower() in ['a','e','i','o','u']:
			vwres=True
			break
	if(not vwres):
		cw.append(word)
print("\nCons Words=",cw)



