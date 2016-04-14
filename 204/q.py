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

plt.scatter(T, q, color='k', s=25, marker="o")
plt.xlabel(u'Температура воды T, К')
plt.ylabel(u'Теплота образования ед. поверхности q, $\\frac{Дж}{м^2К}$')
plt.title(u'График зависимости q(Т)')
plt.grid(color='k', linestyle='-')
plt.errorbar(T, q, xerr=2, yerr=q_err, color='k', fmt='o')
plt.show()