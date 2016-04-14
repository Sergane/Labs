# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 13}
rc('font', **font)

# mm:
d1 = 0.13
d2 = 0.7
L1 = 75
L2 = 70
h1 = [36.7, 37.3, 38.4, 51.8, 54.6, 58.3, 61.4]
h2 = [36.8, 37.3, 38.5, 51.8, 54.7, 58.3, 61.5]
h = [(h1[i]+h2[i])/2 for i in range(0, len(h1))]
delta_x = ( (0.05*L2*d1)**2 + (0.005*L2*d2)**2 )**0.5/(d2-d1)**2


N = 13

phi = (d2 - d1)/L2
print "φ =", phi

a = [d2/phi - L1 + 5*i for i in range(0, N+1)]

x = []
x.append(a[N])
x.append(a[N-1])
x.append(a[N-2])
x.append(a[N-9])
x.append(a[N-10])
x.append(a[N-11])
x.append(a[N-12])

one_fr_x = [1/i for i in x]

temp1 = one_fr_x[-1]
temp2 = h1[-1]
one_fr_x.pop()
h.pop()

fit, err, _, _, _ = np.polyfit(one_fr_x, h, 1, full=True)
K, b = fit
print "K =", K
print "ΔK =", err[0]
print "σ =", K*10**(-6)*1000*9.8*phi/2
print "Δσ =", err[0]*10**(-6)*1000*9.8*phi/2

x1 = [i for i in np.arange(one_fr_x[0]-0.0005, one_fr_x[5]+0.0002, 0.0001)]
y1 = [K*i+b for i in x1]

one_fr_x.append(temp1)
h.append(temp2)

plt.plot(x1, y1, color='k')
plt.scatter(one_fr_x, h, color='k', s=25, marker="o")
plt.xlabel(u'$x_i^{-1}$, мм$^{-1}$')
plt.ylabel(u'Высота мениска $h_i$, мм')
plt.title(u'График зависимости высоты мениска $h_i$\nот $x_i^{-1}$')
plt.grid(color='k', linestyle='-')
plt.errorbar(one_fr_x, h, yerr=0.5, color='k', fmt='o')
# plt.xlim([0.01,0.04])
plt.show()