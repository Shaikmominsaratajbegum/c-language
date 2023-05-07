print("="*20)
print("\tC.Circle")
print("\tR.Rectangle")
print("\tS.Square")
print("\tT.triangle")
print("\tE.Exit()")
ch=int(input("enter u r choice"))
match(ch):
    case Circle:
        print("enter a radius:")
        a=3.14*r*r
        print("{} is area".format(a))
    case Rectangle:
        print("enter a length")
        print("enter a width")
        a=l*w
        print("{} is rectangle".format(a))
    case square:
        print("enter a square value:")
        s=n**1/2
        print("{} is square value:".format(s))
    case Triangle:
        print("enter a triangle value:")
        a=h**b/2
        print("{} is square:".format(a))

