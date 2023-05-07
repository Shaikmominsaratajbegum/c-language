from Atmexception import depositeerror,withdrawerror,Insuffunderror
bal=500.00
def deposite():
    damt=float(input("enter a deposite amount:"))
    if(damt<=0):
        raise depositeerror
    else:
        global bal
        bal=bal+damt
        print("u r acount credited with inr:{}",format(damt))
        print("now u r acount balance after deposite:{}".format(bal))
def withdraw():
    global  bal
    wamt = float(input("enter a deposite amount:"))
    if (wamt <= 0):
        raise withdrawerror
    elif((wamt+500)>bal):
        raise Insuffunderror
    else:
        bal=bal-wamt
        print("u r acount debited with inr:{}".format(wamt))
        print("now u r acount balance after debitated:{}".format(bal))
def balenq():
        print("now u r acount balance eq:{}".format(bal))

