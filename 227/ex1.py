# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 14}
rc('font', **font)

p = [1466.3, 1999.5, 2666, 4132.3, 5465.3]
T = [294.5, 298.2, 303, 308.1, 313]

fit = np.polyfit(T, p, 2)
x1 = [x for x in np.arange(T[0]-2, T[len(T)-1]+1, 1)]
y1 = [fit[0]*x**2+fit[1]*x+fit[2] for x in x1]

plt.plot(x1, y1, color='k')
plt.scatter(T, p, color='k', s=25, marker="o")

plt.xlabel(u'Температура насыщенных паров T, К')
plt.ylabel(u'Давление насыщенных паров\nP, Па')
plt.title(u'График зависимости p(T)\nнасыщенных паров')
plt.grid(color='k', linestyle='-')
plt.show()