x=[10,"python",20,"c",30,"c++"]
fp=open("sci.info","a")
fp.writelines(str(x))
fp.writelines("\n")
print("data written to file")