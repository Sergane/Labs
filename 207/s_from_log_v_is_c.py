# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math as m

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [964.5,966.7,970.3,972.8,975.7,978.9,982.7,986.4]
T = [313.02,314.04,315.17,316,316.95,318.05,319.11,320]
s = [0.00010136781807856063, 0.00019700260147301915, 0.0002690423847815182, 0.0003507278728928801, 0.00044718976992692817, 0.0005299402763089997, 0.000592230110090298]
x = []
# x = [m.log(T[i]/T[0]) for i in range(1,8)]
for i in range(1,8):
	x.append(m.log(T[i]/T[0]))

fit, err, _, _, _ = np.polyfit(x, s, 1, full=True)
K, b = fit
print K
print err

x1 = [i for i in np.arange(0.002, 0.024, 0.001)]
y1 = [i for i in x1]
for i in range(0,len(y1)):
	y1[i] *= K
	y1[i] += b

# print x1
# print y1

plt.plot(x1, y1, color='k')
plt.scatter(x, s, color='k', s=25, marker="o")

plt.xlabel(u'ln(Ti/T0)')
plt.ylabel(u'Si, Дж/К')
plt.title(u'График зависимости Si oт ln(Ti/T0)\nпри постоянном объеме')
plt.grid(color='k', linestyle='-')
plt.show()