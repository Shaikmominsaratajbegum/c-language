word=input("enter a word:")
if(word==word[::-1]):
    print("it is palindrom")
if(word!=word[::-1]):
    print("it is not palindrome")