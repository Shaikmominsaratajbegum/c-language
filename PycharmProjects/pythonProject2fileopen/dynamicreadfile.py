def filedataread():
    filename=input("enter any file name:")
    try:
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("content of file:",fp.name)
            print(filedata)
    except FileNotFoundError:
        print("file does not exits")
filedataread()