lst=[10,20 ,30,-40,50,60,-70,-20]
plst={val for val in lst if val>0}
nlst={v for v in lst if v<0}
print("list of +ve values:{} and type={}".format(plst,type(plst)))
print("list of -ve values:{} and type={}".format(nlst,type(nlst)))
