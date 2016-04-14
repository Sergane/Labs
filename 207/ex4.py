# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('ex4.pdf')

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [1099.3,1082.7,1069.8, 1056.4,1043.9,1032.1,1019.4,1009.3,996.2,982.5,973.8]
v = [35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5]
T = [295.81,295.81,295.81,295.81,295.79,295.81,295.85,295.81,295.81,295.81, 295.81]

# p = [977,988.1,999.2,1006.6,1020.2,1031.9,1040.7,1048.6,1063.8,1075.2,1089.7,1100.2]
# v = [44.,43.5,43.,42.5,42.,41.5,41.,40.5,40.,39.5,39,38.5]
# T = [317.62,317.52,317.48,317.48,317.48,317.48,317.42,317.45,317.42,317.45,317.38,317.35]

avT = sum(T)/len(T)

A = []
Ai = []
for i in range(1,len(p)):
	A.append( abs(0.5*(p[i-1]+p[i])*(v[i]-v[i-1])*100/1000000) )
	Ai.append(sum(A))

# s = [x/avT for x in A]
# print s

Si = [x/avT for x in Ai]
print Si

ln_v = [abs(m.log(v[i]/v[0])) for i in range(1, len(v))]
print ln_v

fit, err, _, _, _ = np.polyfit(ln_v, Si, 1, full=True)
K, b = fit
print K
print err

nu = p[0]*100*v[0]/1000000/(8.31*295.81)
print nu

print K/nu

x1 = [i for i in np.arange(0.007, ln_v[len(ln_v)-1]+0.0018, 0.0001)]
y1 = [K*x+b for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(ln_v, Si, color='k')

plt.xlabel(u'ln(Vi/V0)')
plt.ylabel(u'Si, Дж/К')
plt.title(u'График зависимости Si oт ln(Vi/V0)\nпри постоянной температуре')
plt.grid(color='k', linestyle='-')

plt.show()

plt.savefig(pp, format='pdf')
# pp.savefig()
pp.close()