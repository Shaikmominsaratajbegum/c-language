def dispvalues(**sar):
    for k,v in sar.items():
        print("\t{}={}".format(k,v))
        print()
dispvalues(tno=1,tname="KV",sub1="Python",sub2="Java") # Function call-1
dispvalues(eno=1000,ename="Rossum",dsg="SE") # Function Call-2
dispvalues(a=10,b=20,c=30) # Function Call-3
dispvalues(sno=100,sname="Raj",hobby1="Eating",hobby2="Sleep",hobby3="Chatting",hobby4="Insta Reels")
