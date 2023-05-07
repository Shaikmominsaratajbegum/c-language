biggest=lambda a,b,c: a if a>b and a>c else b if b>a  and b>c else  c if c>a and c>b else "both are euual"
smallest=lambda a,b,c: a if a<b and a<c else b if b<a  and b<c else  c if c<a and c<b else "both are euual"
#main progrm
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value"))
res1=biggest(a,b,c)
res2=smallest(a,b,c)
print(res1)
print(res2)