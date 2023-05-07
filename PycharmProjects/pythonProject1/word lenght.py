def getnames():
    print("enter list of names separated by cooma:")
    nameslist=[names for names in input().split()]
    return nameslist
def obatainwordsvowel():
    nameslist=getnames()
    print("given names")
    for names in nameslist:
        print("\t{}".format(names))
    vwords=[name for name in nameslist if (len(name) in [3,4,5] and ('a' in name.lower() or 'e' in name.lower() or 'i' in name.lower() or 'o' in name.lower() or 'u' in name.lower() ) ]
    print("resultant words")
    print(vwords)
obatainwordsvowel()

