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
