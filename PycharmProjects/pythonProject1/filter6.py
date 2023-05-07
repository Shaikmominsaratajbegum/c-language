print("enter a list of words separated by space:")
lst=[val for val in input().split()]
print("given list of words:{}".format(lst))
palwords=list(filter(lambda word:word[::].upper()==word[::-1].upper(),lst))
print("list of palindrome words={}".format(palwords))
