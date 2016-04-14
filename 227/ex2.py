# -*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

T = [294.5, 298.2, 303, 308.1, 313.9, 318]
t1 = [27.35, 25.15, 23.3, 22.01, 21.28, 20.2]
t2 = [30.55, 28.1, 26.57, 23.90, 23.1, 21.95]
t = [(t1[i]+t2[i])/2 for i in range(0, len(t1))]

B = 8*10**(-5)

eta = [B*i for i in t]
# print eta

fit = np.polyfit(T, eta, 2)
a, b, c = fit

x1 = [x for x in np.arange(T[0]-1, T[len(T)-1]+1, 1)]
y1 = [a*x**2+b*x+c for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(T, eta, color='k', s=25, marker="o")

plt.xlabel(u'температура T, К')
plt.ylabel(u'вязкость воды η, Па*с')
plt.title(u'График зависимости вязкости воды η\nот температуры')
plt.grid(color='k', linestyle='-')
plt.show()
