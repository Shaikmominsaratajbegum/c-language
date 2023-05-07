s="python"
#output pthn
for ch in s:
    if(ch=="y") or (ch=="o"):
        continue
    print("{}".format(ch))
print("====================")
i=0
while(i<len(s)):
    if (s[i]=="y") | (s[i]=="o"):
        i=i+1
        continue
    print("{}".format(s[i]))
    i=i+1