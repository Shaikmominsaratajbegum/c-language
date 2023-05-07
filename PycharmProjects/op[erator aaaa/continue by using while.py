s="python"
i=0
while(i<len(s)):
    print("{}".format(s[i]))
    i=i+1
print("=============")
#output:pyth
i=0
while(i<len(s)):
    if(s[i]=="h"):
        i=i+1
        continue
    else:
        print("\t{}".format(s[i]))
        i=i+1
else:
    print("e.se block of stmts")
print("other block of stmts")