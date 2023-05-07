def findtotalmarks(sno,cls,sname,*val,city="kadapa",**submarks):
    for val in val:
        print("\t{}".format(val))
    print("enter a student number:{}".format(sno))
    print("enter a student name:{}".format(sname))
    print("enter a student class:{}".format(cls))
    print("enter a student city:{}".format(city))
    totalmarks=0;
    print("\tsubjects\tmarks")
    for subject,marks in submarks.items():
        print("\t{}\t\t{}".format(subject,marks))
        totalmarks+=marks
    print("===========================")
    print("\ttotal marks={}".format(totalmarks))
findtotalmarks(10,"x","pavan",14,20,30,40,50,telu=60,hindi=50,eng=65,maths=60,sci=70,social=70)
findtotalmarks(20,"xii","sartaj",50,40,70,69,maths=80,chem=40,phy=80)
findtotalmarks(40,"begum","b.tech",50,60,20,10,daa=60,raa=70,os=89)