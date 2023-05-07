line=input("enter  a word or line text:")
d={}
for ch in line:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
else:
    print("letter\t\t number of Occrences")
    ln=0
    for let,occ in d.items():
        print("\t{}\t\t{}".format(let,occ))
        ln=ln+occ
