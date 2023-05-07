while(True):
    print("="*50)
    print("arithmetic operation")
    print("\t1.addition")
    print("\t2.substraction")
    print("\t3.multiplication")
    print("\t4.division")
    print("\t5.modulo div")
    print("\t6.exponentiation")
    print("\t7.exit()")
    ch=int(input("enter u r choice"))
    match(ch):
           case 1:
                   print("enter two values for addition")
                   a,b=int(input()),int(input())
                   print("sum({},{})={}".format(a,b,a+b))
           case 2:
                   print("enter two values for substraction")
                   a, b = int(input()), int(input())
                   print("sub({},{})={}".format(a, b, a - b))
           case 3:
                   print("enter two values for multiplication")
                   a, b = int(input()), int(input())
                   print("mul({},{})={}".format(a, b, a * b))
           case 4:
                   print("enter two values for division")
                   a, b = int(input()), int(input())
                   print("div({},{})={}".format(a, b, a / b))
           case 5:
                   print("enter two values for modulo division")
                   a, b = int(input()), int(input())
                   print("mod div({},{})={}".format(a, b, a % b))
           case 6:
                a=int(input("enter base"))
                b=int(input("enter power:"))
                print("({},{})={}".format(a, b, a ** b))
           case 7:
                 print("tq for using this program")
           case _:
                print("u r selection is wrong")

