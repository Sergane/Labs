# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np

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

one_frac_eta = [1/a for a in eta]

# from molar_volume.py :
v = [18.03779760606059, 18.054316795844144, 18.078780779220772, 18.108527944415581, 18.147058775584416, 18.177314155844158]

fit = np.polyfit(v, one_frac_eta, 1)
a, b = fit
print "d =", -b/a
mu = 18.01528
print "b =", -b/a*mu

x1 = [x for x in np.arange(v[0]-0.015, v[len(v)-1]+0.01, 0.0001)]
y1 = [a*x+b for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(v, one_frac_eta, color='k', s=25, marker="o")
plt.xlabel(u'молярный объем V,  $м^3моль^{-1}$')
plt.ylabel(u'1/η,  $Па^{-1}с^{-1}$')
plt.title(u'График зависимости 1/η\nот молярного объема V')
plt.grid(color='k', linestyle='-')
plt.show()