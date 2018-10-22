from Data import *
import operator

def bstate(pb,bin,index):
    for i in range(index+1):
        bin+=pb[i]
    return bin

def min_price(pri,index,l_index,count):
    iter=0
    for x in pri:
    	key=x[0]
        if index <= key <= l_index:
        	if iter==count:
        		return key
        	iter+=1
    return -1
            

def max_price(pri,index,count):
	iteration=0
	for x in pri:
		key=x[0]
		if key >= index:
			if iteration==count:
				return key
			iteration+=1
	return -1

def getKey(item):
    return item[1]

def RTT_Heu(index, n, bin, pres, ares, load, price):
	lres,bres,bg,pb=[],[],[],[]
	#obj=res_data(lres, bres, bg, pb)
	obj=res_one_to(lres, bres, bg, pb,82)
	#print('0 '+str(obj))
	#print (obj)print(bg)
	for i in xrange(n):
		pr=lres[i]+bres[i]
		if pr>ares[i]:
			print ("intex "+str(i))
			rem=pr-ares[i]
			print bres
			ob=search(pb, price, bg, lres, bres, ares[i], rem, i, bin, n )
			obj+=ob
			print ('1 '+str(obj))
		elif pr<ares[i]:
			print ("intex >"+str(i))
			print bres
			rem_load=load[i]-lres[i]+min(0,pb[i])
			print ("rem "+str(i)+" "+str(rem_load))
			extra=ares[i]-pr
			#print(str(i)+" "+str(extra))
			if bg[i]>0:
				#print(extra)
				ex_bg=min(bg[i],extra)
				bg[i]-=ex_bg
				bres[i]+=ex_bg
				obj-=(ex_bg)*price[i]
				extra-=ex_bg
				#print(str(extra)+" "+str(i))
				print("2 "+str(obj))
				#print(obj)
			if extra>0:
				ch_amt=20-max(0,pb[i])

				#print ('ch_amt '+str(ch_amt))
				ld_f=min(max(0,extra-ch_amt), rem_load)
				obj-=ld_f*price[i]
				print('3 '+str(obj))
				print(str(i)+" "+str(extra))
				load[i]-=ld_f
				extra-=ld_f
				if extra>0:
					
					ob=alloc(price, bg, load, pb, bres, lres, i, n, extra)
					obj-=ob
					print("4 "+str(obj))
	return obj
def alloc(price, bg, load, pb, bres, lres, i, n, extra):
	pri=[(ix,pr) for ix,pr in zip(range(n),price)]
	pri=dict(pri)
	pric=sorted(pri.items(),key=operator.itemgetter(1),reverse=True)
	check=i
	obj=0
	while check<n and extra>0:
		key=max_price(pric, i, check-i) #check-i is a count
		#print("price "+str(price[key]))
		rem_load=load[key]-lres[key]+min(0,pb[key])
		#print("rem_load "+str(rem_load))
		if key==i:
			rem=min(rem_load,extra)
			obj+=rem*price[i]
			lres[i]+=rem
			extra-=rem
		else:
			rem=min([rem_load, extra, pb[key]+30])
			#print(rem)
			obj+=rem*price[key]
			bres[i]+=rem
			pb[i]+=rem
			if pb[key]>0:
				if pb[key]-rem<0:
					bg[key]=0
					lres[key]+=bres[key]
					bres[key]=0
				else:
					rem_c=rem
					lres[key]+=min(pb[key], rem, bres[key])
					temp=min(bres[key], rem_c)
					#print 'temp'+str(temp)
					bres[key]-=temp
					#print bres[key]
					rem_c-=temp
					temp=min(rem_c, bg[key])
					bg[key]-=temp
				#bres[key]=max(0, bres[key]-rem)

			pb[key]-=rem
			#print pb
			extra-=rem
		check+=1
		if extra==0:
			return obj
	if extra>0:
		pb[i]=min(20, pb[i]+extra)
	return obj

def search(pb, price, bg, lres, bres, ares_v, rem, i, bin, n ):
	obj=0
	pri=[(ir,pr) for ir,pr in zip(range(n),price)]
	pri=dict(pri)
	pri=sorted(pri.items(),key=operator.itemgetter(1))
	if bg[i]>0:
		return rem*price[i]
	elif bg[i]==0:
		if ares_v<lres[i]:
			rem_load=lres[i]-ares_v
			lres[i]=ares_v
			pb[i]-=bres[i]
			bres[i]=0
			bs=bstate(pb, bin, i)
			print "bs "+str(bs)
			if bs>0:
				print pb
				serve=min([rem_load, bs, pb[i]+30])
				rem_load-=serve
				obj+=rem_load*price[i]
				pb[i]-=serve
				print( str(i)+" "+str(pb[i])+" "+str(bs))
				rem-=rem_load
			else:
				obj+=rem_load*price[i]
				rem-=rem_load
		elif ares_v>=lres[i]:
			pb[i]=ares_v-lres[i]
			bres[i]=ares_v-lres[i]
		while -rem<0:
			index=i+1
			#print(pb)
			bs=bstate(pb, bin, i)
			#print(" bs "+str(bs))
			while bs>=0 and index<n:
				bs+=pb[index]
				index+=1
			if bs>=0 and index==n:
				return obj
			index=min(index-1,n-1)
			jin=0
			while bs<0:
				min_in=min_price(pri, i, index, jin)
				#print("min_in:: "+str(min_in)+" "+str(index))
				
				jin+=1
				charge=min(20-pb[min_in],-bs)
				#print "charge "+str(charge)
				if pb[min_in]+charge>0:
					if pb[min_in]>=0:
						bg[min_in]+=charge
					else:
						chr=pb[min_in]+charge
						bg[min_in]=chr

					#bres[min_in]=max(bres[min_in]-chr,0)
					
				pb[min_in]+=charge
				bs+=charge
				rem-=charge
				obj+=charge*price[min_in]
	return obj




