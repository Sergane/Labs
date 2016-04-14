# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [1466.3, 1999.5, 2666., 4132.3, 5465.3]
T = [294.5, 298.2, 303., 308.1, 313.]

ln_p = [m.log(a) for a in p]
one_frac_T = [1/t for t in T]

fit = np.polyfit(one_frac_T, ln_p, 1)
K, b = fit;
print "y = "+str(K)+"*x + "+str(b)
Q = 8.3144598*abs(K)
print "Q =", Q
print "a =", 18*10**(-6)*(Q - p[0])

x1 = [x for x in np.arange(one_frac_T[len(T)-1]-0.00001, one_frac_T[0]+0.00001, 0.00001)]
y1 = [K*x+b for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(one_frac_T, ln_p, color='k', s=25, marker="o")

plt.xlabel(u'1/T, 1/К')
plt.ylabel(u'ln(p)')
plt.title(u'График зависимости ln(p) от 1/T')
plt.grid(color='k', linestyle='-')
plt.show()