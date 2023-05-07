try:
    kvr=open("sartaj","w")
    print("file opened in read mode")
    print("type of kvr=",type(kvr))
    print("file is closed:",kvr.closed)
except FileNotFoundError:
    print("file does not exist")
finally:
    print("i am from finally block")
    kvr.close()
    print("is file closed:",kvr.closed)

