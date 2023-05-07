from aopImplementations import*
from aopmenu import menu as m
import sys
while(True):
    m()
    ch=int(input("\tenter u r choice:"))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            fdivop()
        case 6:
            mdivop()
        case 7:
            expop()
        case 8:
            print("tq for using this program")
            sys.exit()
        case _:
            print(" u r selection is operation is wrong")
