from Atmexception import depositeerror,withdrawerror,Insuffunderror
from ATMmenu import menu
import Atmexception as atm
while(True):
menu()
try:
ch=int(input("enter u r choice"))
match(ch):
