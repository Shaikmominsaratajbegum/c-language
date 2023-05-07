print("Enter List of Values separated by space:")
words=[ val  for val in input().split()]
vw=list(filter(lambda word:'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower(), words))
print("vowel words={}".format(vw))