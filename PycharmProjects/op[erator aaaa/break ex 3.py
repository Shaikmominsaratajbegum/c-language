s="MISSISSIPPI"
for i in range(0,len(s)):
    if(i==4):
        break
    else:
        print("\t{}".format(s[i]))
print("=========================")
cnt=0
for ch in s:
    if(ch=="I"):
        cnt=cnt+1
        if(cnt==2):
            break
        else:
            print(ch)
    else:
        print(ch)
print("=============================")
for ind,ch in enumerate(s):
    if(ind==4):
        break
    else:
        print("{}".format(ch))