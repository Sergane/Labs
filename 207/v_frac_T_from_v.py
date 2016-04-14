# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [974.5,974.6,974.5,974.7,974.4,974.5,974.6]
T = [295.98,298.46,301.44,304.25,307.49,310.17,313.02]
v = [40.5,41,41.5,42,42.5,43,43.5]

y = []
for i in range(0, len(p)):
	y.append(v[i]/T[i])

plt.scatter(v, y, color='k', s=25, marker="o")

plt.xlabel(u'Объем V, мл')
plt.ylabel(u'V/T, мл/К')
plt.title(u'График зависимости V/T(V)')
plt.grid(color='k', linestyle='-')
plt.show()
