# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [1099.3,1082.7, 1056.4,1043.9,1032.1,1019.4,1009.3,996.2,982.5,973.8]
v = [35.5, 36.0, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5]

# p = [977,988.1,999.2,1006.6,1020.2,1031.9,1040.7,1048.6,1063.8,1075.2,1089.7,1100.2]
# v = [44,43.5,43,42.5,42,41.5,41,40.5,40,39.5,39,38.5]

# plt.plot(v, p, label='P(V) line', color='k')
plt.scatter(v, p, label='P(V) dots', color='k', s=25, marker="o")

plt.xlabel(u'Объем V, мл')
plt.ylabel(u'Давление P, гПа')
plt.title(u'График зависимости P(V)\nпри изотермическом расширении')
plt.grid(color='k', linestyle='-')
# plt.legend()
plt.show()
