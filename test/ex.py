import math as m
p = [m.factorial(12)/(m.factorial(x)*m.factorial(12-x))*0.2**x*0.8**(12-x) for x in range(0, 13)]
#print max(p)
#print p.index(max(p))
for i in p:
    print p.index(i), i
