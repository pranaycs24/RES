from Data import *
from Optimum import solution_op
from H_RTT import RTT_Heu

def main():
	n=6
	I=0
	open('RTT_6/temp1.txt', 'w').close()
	ase=[11, 17, 19, 21]
	for I in xrange(1,2):
		pass
		pres,ares,price,load=[],[],[],[]
		lres,bres,bg,pb=[],[],[],[]
		data(price,load,pres,ares,I,n)
		#solution_op(pres, price, load, n, 0)
		#obj=res_data(lres, bres, bg, pb)
		#obj=res_opt(lres, bres, bg, pb,17)
		ob=RTT_Heu(0, n, 0, pres, ares, load, price)
		#ob=res_one_to(lres, bres, bg, pb,17)
		print(ob)
		#print(pb)
		#with open("RTT_6/res_6.txt", "a+") as f:
			#f.write(str(ob)+"\n")

if __name__ == '__main__':
    main()