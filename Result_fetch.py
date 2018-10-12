res=[]
with open ("RTT_6/temp1.txt") as f:
	for line in f:
		line=line.strip("\n")
		l= line.split(" ")
		res.append(l[1])
with open("RTT_6/res.txt", 'w') as f:
	for x in res:
		f.write(str(x)+"\n")