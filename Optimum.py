from __future__ import print_function
import sys
import time
from ortools.constraint_solver import pywrapcp
cb=20
cd=30
bmax=50
def solution_op(pres, price, load, n, bin):
	solver=pywrapcp.Solver("Microgrid")
	bg = [solver.IntVar(0, cb, "bg_%i" % I) for I in range(n)]
	pb = [solver.IntVar(-cd, cb, "pb_%i" % I) for I in range(n)]
	lres = [solver.IntVar(0, min(load[I], pres[I]), "lres_%i" % I) for I in range(n)]
	bres = [solver.IntVar(0, min(cb, pres[I]), "bres_%i" % I) for I in range(n)]
	de = [solver.BoolVar("de_%i" % I) for I in range(n)]
	for i in range(n):
		solver.Add(lres[i] + bres[i] <= pres[i])
    	solver.Add(de[i]*pb[i] <= 0)

	bs = bin
	solver.Add(-de[0] * pb[0] <= bs)
	for i in range(1,n):
		bs = bs + pb[i-1]
		solver.Add(bs >= 0)
		solver.Add(bs <= bmax)
		solver.Add(-de[i] * pb[i] <= bs)
	cost = 0
	for i in range(n):
		solver.Add(bres[i] + bg[i] == pb[i] - pb[i] * de[i])
		solver.Add(bres[i] + bg[i] <= cb)
		solver.Add(-de[i] * pb[i] + lres[i] <= load[i])
		solver.Add(-de[i] * pb[i] <= load[i])
		cost += load[i]*price[i]
	print(cost)
	for i in range(n):
		cost += -lres[i]*price[i] + pb[i]*price[i] - bres[i]*price[i]
 	var = pb + de + bg + bres + lres
	print(var)
	obj = solver.Minimize(cost, 1)
	db = solver.Phase(var, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
	collector = solver.LastSolutionCollector()
	collector.Add(var)
 	search_log = solver.SearchLog(1000000, cost)
	#Time_Limit = solver.TimeLimit(n*60*1000);
	time1=time.clock()
	solver.Solve(db, [search_log, obj, collector])
	time2=time.clock()
	results=[]
	results.append(time2-time1)
	print(obj)
	with open("./RTT_6/temp.txt","w") as f:
		f.write(str(obj)+"\n")
		for x in range(n):
			f.write(str(collector.Value(0,pb[x]))+" ")
			f.write(str(collector.Value(0,de[x]))+" ")
			f.write(str(collector.Value(0,bg[x]))+" ")
			f.write(str(collector.Value(0,bres[x]))+" ")
			f.write(str(collector.Value(0,lres[x]))+"\n")
    