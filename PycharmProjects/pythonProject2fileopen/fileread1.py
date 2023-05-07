try:
    with open("sci.info") as sp:
        filedata=sp.readlines()
        print("===============================")
        for fd in filedata:
            print(fd,end="")
        print(("=============================="))
except FileNotFoundError:
    print("file does not exits")