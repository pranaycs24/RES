from __future__ import print_function
import sys
def data(price, load, pres, ares, I, N):
    with open("test_case_6/test_%i.txt" % I) as f:
        x = 0
        for line in f:
            if x >= N:
                break
            x += 1
            line = line.strip("\n")
            test = line.split(" ")
            price.append(int(test[0]))
            load.append(int(test[1]))
            pres.append(int(test[2]))
            ares.append(int(test[3]))

def res_data( lres, bres, bg, pb):
	with open("RTT_6/temp.txt") as f:
		x=True
		obj=-1
		for line in f:
			line =line.strip("\n")
			test =line.split(" ")
			if x:
				obj=int(test[-1].strip(")"))
				x=False
			else:
				pb.append(int(test[0]))
				bg.append(int(test[2]))
				bres.append(int(test[3]))
				lres.append(int(test[4]))
		return obj
def res_opt(lres, bres, bg, pb, index):
	with open("RTM_6/res_6.txt") as f:
		x=True
		obj=-1
		for line in f:
			line=line.strip("\n")
			res=line.split(" ")
			if x and res[0]==str(index):
				x=False
			elif res[0]=='obj' and not(x):
				obj=int(res[1])
			elif res[0]=='pb' and not(x):
				pb.append(int(res[1]))
				bg.append(int (res[5]))
				bres.append(int(res[7]))
				lres.append(int(res[9]))
			elif res[0]!='time' and obj!=-1:
				return obj
			#print(res[0])
		return obj
def res_one_to(lres, bres, bg, pb, index):
	with open("Result_pres_6/res_6.txt") as f:
		x=True
		obj=-1
		for line in f:
			line=line.strip("\n")
			res=line.split(" ")
			if x and res[0]==str(index):
				x=False
			elif res[0]=='obj' and not(x):
				obj=int(res[-1].strip(")"))
			elif res[0]=='pb' and not(x):
				pb.append(int(res[1]))
				bg.append(int (res[5]))
				bres.append(int(res[7]))
				lres.append(int(res[9]))
			elif res[0]!='time' and obj!=-1:
				return obj
