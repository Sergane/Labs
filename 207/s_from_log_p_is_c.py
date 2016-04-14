# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math as m

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [974.5,974.6,974.5,974.7,974.4,974.5,974.6]
T = [295.98,298.46,301.44,304.25,307.49,310.17,313.02]
v = [40.5,41,41.5,42,42.5,43,43.5]
s = [0.0003570602049715477, 0.0007515220953170746, 0.0011280086343076106, 0.0015351536778089468, 0.0018933705902394182, 0.002261475724156306]
x = []

for i in range(1,len(p)):
	x.append(m.log(T[i]/T[0]))

fit, err, _, _, _ = np.polyfit(x, s, 1, full=True)
K, b = fit
print K
print err

x1 = [i for i in np.arange(0.0065, 0.0575, 0.0005)]
y1 = [i for i in x1]
for i in range(0,len(y1)):
	y1[i] *= K
	y1[i] += b

# print x1
# print y1

plt.plot(x1, y1, color='k')
plt.scatter(x, s, color='k', s=15, marker="o")

plt.xlabel(u'ln(Ti/T0)')
plt.ylabel(u'Si, Дж/К')
plt.title(u'График зависимости Si oт ln(Ti/T0)\nпри постоянном давлении')
plt.grid(color='k', linestyle='-')
plt.show()