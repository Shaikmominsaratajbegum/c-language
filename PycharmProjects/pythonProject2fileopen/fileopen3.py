with open("kvr2.data","x+") as fp:
    print("file created and opened in write mode")
    print("type of kvr=", type(fp))
    print("file name",fp.name)
    print("file name", fp.mode)
    print("file readable", fp.readable())
    print("file writable ", fp.writable())
    print("file  closed", fp.closed)
print("file closed", fp.closed)