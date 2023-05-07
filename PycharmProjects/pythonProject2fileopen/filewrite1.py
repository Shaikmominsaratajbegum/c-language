sno=600
sname="kvr"
smarks=11.22
with open("student data","a") as sd:
    sd.write(str(sno))
    sd.write(sname)
    sd.write(str(smarks))
    sd.write("\n")
    print("data written to the file")
