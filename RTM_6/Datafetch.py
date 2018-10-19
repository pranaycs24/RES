with open ("res_6.txt") as f:
	for line in f:
		line=line.strip("\n")
		l=line.split(" ")
		if l[0]=="obj":
			with open("res_6_obj.txt", "a+") as f:
				f.write(str(l[1])+"\n")
