def getnames():
    print("enter list of names separated by space:")
    nameslist=[names for names in input().split()]
    return nameslist
def maxlengthwords():
    nameslist=getnames()
    palwords={name:len(name) for name in nameslist if name==name[::-1] }
    print(palwords)
    ml=max(palwords.values())
    maxpalword=[word for word,length in palwords.items() if length>=ml]
    print("max length palindrome word=",maxpalword)
maxlengthwords()bv11
