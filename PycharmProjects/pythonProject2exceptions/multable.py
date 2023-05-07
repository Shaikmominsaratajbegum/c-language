from mulexception import negnumError,zeroError
def Table(n):
    if(n<0):
        raise negnumError
    elif(n==0):
        raise zeroError
    elif(n>0):
        print("multiplication table")
        for i in range(1,11):
            print("\t{}X{}={}".format(n,i,n*i))

