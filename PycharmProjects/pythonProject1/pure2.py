def disp(*kvr):
    print("number of  values:{}".format(len(kvr)))
    for val in kvr:
        print(val,end=" ")
    print()
disp(10,20,30,40,50,60) # Function Call-1
disp(10,20,30,40,50) # Function Call-2
disp(10,20,30,40) # Function Call-3
disp(10,20,30) # Function Call-4
disp(10,20) # Function Call-5
disp(10) # Function Call-6

