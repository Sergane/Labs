import scipy.constants as c

r = 10**(-3)
l = 23*0.1
p = [70, 53, 41, 62]
p = [P*9.907 for P in p]
I = [2.03, 1.84, 1.41, 1.96]
I = [i*10**(-6) for i in I]

eta = [c.pi*r**4*p[i]/(8*l*I[i]) for i in range(0, len(p))]
for e in eta:
	print e