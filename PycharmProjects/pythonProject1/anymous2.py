def menu():  # Normal function
    print("=" * 50)
    print("\tArihtmetic Operations")
    print("=" * 50)
    print("\t1. Addition")
    print("\t2. Substraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Modulo Div")
    print("\t6. Exponentiation")
    print("\t7.Square Root")
    print("\t8. Exit")
    print("=" * 50)


#Anonymous Function definition
addop = lambda k, v: k + v
subop = lambda k, v: k - v
mulop = lambda k, v: k * v
divop = lambda k, v: k / v
fdivop = lambda k, v: k // v
modop = lambda k, v: k % v
sqrop = lambda n: n ** 0.5
expop = lambda a, b: a ** b

# main program
while (True):
    menu()
    ch = int(input("Enter Ur Choice:"))
    match (ch):
        case 1:
            print("Enter Two Values for Addition:")
            print("Sum=", addop(float(input()), float(input())))
        case 2:
            print("Enter Two Values for Substraction:")
            print("Sub=", subop(float(input()), float(input())))
        case 3:
            print("Enter Two Values for Multiplication:")
            print("Mul=", mulop(float(input()), float(input())))
        case 4:
            while (True):
                print("-------------------------------")
                print("1. Normal Div")
                print("2. Floor Div:")
                print("3. Exit")
                print("-------------------------------")
                ch1 = int(input("Enter Ur Choice:"))
                match (ch1):
                    case 1:
                        print("Enter Two Values for Normal Division:")
                        print("Div=", divop(float(input()), float(input())))
                    case 2:
                        print("Enter Two Values for Floor Division:")
                        print("Floor Div=", fdivop(float(input()), float(input())))
                    case 3:
                        print("Thx for using Inner menu")
                        break
                    case _:
                        print("Ur Selection of inner Menu is wrong-try again")
        case 5:
            print("Enter Two Values for Modulo Div:")
            print("MOdulo Div=", modop(float(input()), float(input())))

        case 6:
            print("Enter Base\nEnter Power::")
            print("Exp=", expop(float(input()), float(input())))
        case 7:
            print("Enter a Number for Cal Square Root of Given Number:")
            print("Square Root=", sqrop(float(input())))
        case 8:
            print("Thx for using this Program--outer menu")
            break
        case _:
            print("Ur Selection of Operation is Wrong-try again")
