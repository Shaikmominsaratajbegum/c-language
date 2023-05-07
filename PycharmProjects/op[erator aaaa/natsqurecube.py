n=int(input("enter how many natural numbers  square and cube numbers u want:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    s=0
    ss=0
    cs=0
    print("\tnatnums\tsquare\tcube".format(s))
    for i in range(1,n+1):
        print("\t{}\t{}\t{}".format(i,i**2,i**3))
        s=s+1
        ss=ss+i**2
        cs=ss+i**3
    else:
        print("==="*50)
        print("\t{}\t{}\t".format(s,ss,cs))
