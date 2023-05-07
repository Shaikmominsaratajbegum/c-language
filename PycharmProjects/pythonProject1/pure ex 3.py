def disp(sno,sname,*val):
    print("student number:{}".format(sno))
    print("student name:{}".format(sname))
    print("number of  values:{}".format(len(val)))
    s=0
    for val in val:
        print(val,end=" ")
        s=s+val
    print("sum={}".format(s))
disp(100,"rossum",10,20,30,40,50,60) # Function Call-1
disp(200,"sar",10,20,30,40,50) # Function Call-2
disp(300,"beg",10,20,30,40) # Function Call-3
disp(400,"rsda",10,20,30) # Function Call-4
disp(500,"daa",10,20) # Function Call-5
disp(600,"maru",10) # Function Call-6

