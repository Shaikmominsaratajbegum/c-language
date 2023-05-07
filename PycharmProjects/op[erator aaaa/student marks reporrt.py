while(True):
    sno=int(input("enter a number between(100-200)"))
    if(sno>=100) and (sno<=200):
        break
    else:
        print("{} os invalid input:".format(sno))
sname=input("enter a name:")
#validate marks in c lang(0-100)
while(True):
    cm=int(input("enter marks in c lang:"))
    if(0<=cm<=100):
        break
    else:
        print("\t{} is invalid marks in c lang:".format(cm))
while(True):
    cppm=int(input("enter marks in cppm:"))
    if(0<=cppm<=100):
        break
    else:
        print("\t{} is inavlid marks in cppm lang".format(cppm))
while(True):
    ym=int(input("enter a marks in python:"))
    if(0<=pym<=100):
        break
    else:
        print("\t{} is invalisd marks in python lang:".format(pym))
totalmarks=cm+cppm+pym
percentage=(totalmarks/300)*100
if(cm<40) or (cppm<40) or (pym<40):
    grade=Fail
else:
    if(totalmarks<=300) and (totalmarks>=250):
        grade="DISTINCTION"
    elif(totalmarks<=249) and (totalmarks<=200):
        grade="first"
    elif(totalmarks<=199) and (totalmarks>=150):
        grade="second"
    elif(totalmarks<=149) and (totalmarks>=120):
        grade="third"
print("=="*50)
print("\tstudent number:{}".format(sno))
print("\tstudent name:{}".format(sname))
print("\tstudent marks in c={}".format(cm))
print("\t student marks in c++={}".format(cppm))
print("\t student marks in python={}".format(pym))
print("="*59)
print("\t student totalmarks:{}".format(totalmarks))
print("\t student percentage of marks{}".format(percentage))
print("\t student grade={}".format(grade))













































