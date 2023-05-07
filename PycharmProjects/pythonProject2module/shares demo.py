import shares
import time
import importlib
def disp(d):
    print("\tshares names\tvalue")
    for sn,sv in d.items():
        print("\t{}\t\t:{}".format(sn,sv))
    else:
        print("===="*40)
d=shares.sharesinfo()
disp(d)
time.sleep(15)
importlib.reload(shares)
d=shares.sharesinfo()
disp(d)