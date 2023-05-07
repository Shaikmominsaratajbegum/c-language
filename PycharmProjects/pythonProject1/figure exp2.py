def menu():
    print("\t1.area of circle")
    print("\t2.area of triangle")
    print("\t3.area of reactangle")
    print("\t4.area of square")
arce=lambda r: 3.14*r*r
arte=lambda h,b : 1/2*h**b
arre=lambda l,b:l*b
arsqe=lambda a:a**2
# main program
while(True):
    menu()
    ch=int(input("enter u r choice:"))
    match(ch):
        case 1:
            print("enter radious of circle:")
            print("arce=",arce(float(input())))
        case 2:
            print("enter hight of circle\n enter base of circle::")
            print("arte=", arte(float(input()),float(input())))
        case 3:
            print("enter length of circle\n enter breadth of circle::")
            print("arre", arre(float(input()), float(input())))
        case 4:
            print("enter area of circle:")
            print("arsqe=",arsqe(float(input())))