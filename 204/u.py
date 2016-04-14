# -*- coding: utf-8 -*-
import scipy.constants as c
import math as m
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 13}
rc('font', **font)

T = [288, 289, 290, 353, 351, 346, 320, 313]
F = [0.064, 0.065, 0.064, 0.06, 0.0605, 0.0605, 0.063, 0.063]
F = [i - 0.034 for i in F]
k = 0.911
D = 65*10**(-3)
sigma = [f/(2*k*c.pi*D) for f in F]

fit, err, _, _, _ = np.polyfit(T, sigma, 1, full=True)
K, b = fit

q = [-t*K for t in T]
q_err = [( (K*2)**2 + (err*T[i])**2 )**0.5 for i in range(0, len(T))]
u = [sigma[i]+q[i] for i in range(0, len(q))]
sgma_err = 0.000167133566568
u_err = [sgma_err + i for i in q_err]

k1, b1 = np.polyfit(T, u, 1)
x1 = [i for i in np.arange(T[T.index(min(T))]-1, T[T.index(max(T))]+2, 0.1)]
y1 = [k1*x+b1 for x in x1]
print "b1 =", b1

plt.plot(x1, y1, color='k')
plt.scatter(T, u, color='k', s=25, marker="o")
plt.xlabel(u'Температура воды T, К')
plt.ylabel(u'Внутренняя энергия ед. поверхности U, $\\frac{Дж}{м^2К}$')
plt.title(u'График зависимости U(Т)')
plt.grid(color='k', linestyle='-')
plt.errorbar(T, u, xerr=2, yerr=u_err, color='k', fmt='o')
plt.show()