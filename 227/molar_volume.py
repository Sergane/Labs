# -*- coding: utf-8 -*-
import math as m
import numpy as np

# v[5] = 18.2002
v_table = [18.0324, 18.0528, 18.0782, 18.1075, 18.1415, 18.1773, 18.2178, 18.262, 18.3088]
t_table = [i for i in range(20, 65, 5)]
T_table = [i+273 for i in t_table]

fit, err, _, _, _ = np.polyfit(T_table, v_table, 2, full=True)
a, b, c= fit
print err

x1 = [x for x in np.arange(T_table[0]-2, T_table[len(T_table)-1]+2, 0.001)]
y1 = [a*x**2+b*x+c for x in x1]

T = [294.5, 298.2, 303., 308.1, 313.9, 318.]
V = [a*x**2+b*x+c for x in T]
print V