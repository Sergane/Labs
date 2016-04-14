# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as c

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

T = [294.5, 298.2, 303., 308.1, 313.9, 318.]
t1 = [27.35, 25.15, 23.3, 22.01, 21.28, 20.2]
t2 = [30.55, 28.1, 26.57, 23.90, 23.1, 21.95]
t = [(t1[i]+t2[i])/2 for i in range(0, len(t1))]

B = 8*10**(-5)

eta = [B*i for i in t]
# print eta

ln_eta = [m.log(a) for a in eta]
one_frac_T = [1/a for a in T]
# print ln_eta
# print one_frac_T

fit, err, _, _, _ = np.polyfit(one_frac_T, ln_eta, 1, full=True)
K, b = fit
print c.k
print K*c.k

x1 = [x for x in np.arange(one_frac_T[len(T)-1]-0.00001, one_frac_T[0]+0.00001, 0.00001)]
y1 = [K*x+b for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(one_frac_T, ln_eta, color='k', s=25, marker="o")

plt.xlabel(u'1/T, 1/К')
plt.ylabel(u'ln (η)')
plt.title(u'График зависимости ln(η) от 1/T')
plt.grid(color='k', linestyle='-')
plt.show()
