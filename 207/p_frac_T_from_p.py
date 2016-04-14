# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [964.5,966.7,970.3,972.8,975.7,978.9,982.7,986.4]
T = [313.02,314.04,315.17,316,316.95,318.05,319.11,320]

y = []
for i in range(0, len(p)):
	y.append(p[i]/T[i])

plt.scatter(p, y, color='k', s=25, marker="o")

plt.xlabel(u'Давление p, гПа')
plt.ylabel(u'p/T, гПа/К')
plt.title(u'График зависимости p/T(p)')
plt.grid(color='k', linestyle='-')
plt.show()
