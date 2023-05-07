from mulexception import negnumError,zeroError
from multable import Table
try:
    n=int(input("enter a number to generate multiplication table"))
    Table(n)
except ValueError:
    print("Dont enter alphanum strings and symbols")
except negnumError:
    print("dont enter   negnum value for mul table")
except zeroError:
    print("dont enter zero value for mul table")

