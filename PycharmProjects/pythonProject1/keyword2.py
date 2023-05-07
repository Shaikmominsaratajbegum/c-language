def dispstdioinfo(sno,sname,marks,crs="python",cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))
print("++++++++++++++++++++++++++++++++++++++")
print("\tsno\tsname\tmarks\tcourse\tcountry")
dispstdioinfo(300,"lal",34.88,"java")
dispstdioinfo(sname="sar",sno=67,marks=88)
dispstdioinfo(crs="python",cnt="india",sname="sar",sno=67,marks=88)
dispstdioinfo(300,"lal",34.88,crsp="java",)