word=input("enter a word:")
if(word.isalpha()):
    print("{} is a word".format(word))
    if("a" in word or "e" in word or "i" in word or "o" in word or "u" in word ):
        print("{} is vowel".format(word))
    else:
        print("{} is consonant".format(word))
else:
    print("{} it is not a word".format(word))