import functools
print("enter list of words separated by space:")
word=[val for val in input().split()]
print("given wlrds".format(word))
line=functools.reduce(lambda a,b:a + " "+b,word)
print("resuls=",line)
print("======================")
k=" "
k=k.join(word)
print("resuls=",line)
print("========================")
for w in word:
    v=v+" "+w
else:
    print("resuls=", v)