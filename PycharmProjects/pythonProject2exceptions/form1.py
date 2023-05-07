from ATMoperation import deposite,withdraw,balenq
from ATMmenu import menu
import Atmexception as atm
while(True):
    menu()
    ch=int(input("enter u r choice"))
    match(ch):
            case 1:
                deposite()
            case 2:
                withdraw()
            case 3:
                balenq()
            case 4:
                print("tq for using")
                break
            case _:
                print("u r selection is wrong")


