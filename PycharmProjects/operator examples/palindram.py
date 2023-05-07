val=input("enter a word / value:")
res="Palindrome" if val.lower()==val[::-1].lower() else "not palindrome"
print("{} is {}".format(val,res))