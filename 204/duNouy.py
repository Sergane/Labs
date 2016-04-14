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

print "F:"
for i in F:
	print i

k = 0.911
D = 65*10**(-3)

sigma = [f/(2*k*c.pi*D) for f in F]
print "σ:"
for i in sigma:
	print i

d_1 = 0.5*10**(-3)/(2*k*c.pi*D)
print "d1 =", d_1

l = len(sigma)
av_sigma = sum(sigma)/l
print "<σ> =", av_sigma

mis = [(av_sigma-i)**2 for i in sigma]
d_2 = ( sum(mis)/(l*(l-1)) )**0.5
print "d2 =", d_2

delta = (d_1**2+d_2**2)**0.5
print "Δσ =", delta

fit, err, _, _, _ = np.polyfit(T, sigma, 1, full=True)
K, b = fit
print "K =", K
print "err =", err[0]

x1 = [i for i in np.arange(T[T.index(min(T))]-1, T[T.index(max(T))]+2, 0.1)]
y1 = [K*x+b for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(T, sigma, color='k', s=25, marker="o")
plt.xlabel(u'Температура воды T, К')
plt.ylabel(u'Коэффициент поверхностного\n натяжения σ, Н/м')
plt.title(u'График зависимости σ(Т)')
plt.grid(color='k', linestyle='-')
plt.errorbar(T, sigma, xerr=2, yerr=delta, color='k', fmt='o')
plt.show()