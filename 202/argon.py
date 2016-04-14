# -*- coding: utf-8 -*-
import pprint as pp
import scipy.constants as c
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
font = {'family': 'Droid Sans',
        'weight': 'normal',
        'size': 13}
rc('font', **font)

# аргон
x =[a for a in np.arange(0,4.5,0.5)]# list from 0 to 4 (step 0.5)
x =[11.-a for a in x]
t1=[69.0,64.2,61.8,57.6,55.4,51.1,48.6,45.4,43.0]
t2=[67.0,64.2,59.9,57.0,54.1,50.8,48.8,45.6,43.0]
t =[0.5*(t1[i]+t2[i]) for i in range(0,len(t1))]
t =[5*a for a in t]; # умножаем t на 5

# вывод данных:
# pp.pprint(zip(x,t))

plt.scatter(t, x, color='k', s=25, marker="o")
pl_fit = np.polyfit(t, x, 1)
x1 = [i for i in np.arange(t[0]+5, t[len(t)-1]-5, -0.1)]
y1 = [pl_fit[0]*i+pl_fit[1] for i in x1]

n = len(x)
x = map(lambda a: a*10**(-2), x) # переводим в метры
t = map(lambda a: a*10**(-6), t) # переводим в секунды

fit, err, _,_,_ = np.polyfit(t,x,1,full=True)
v = fit[0]
print "Скорость:", v
print "Погрешность МНК:", err[0]

Sx = np.std(x)/(n*(n-1))**0.5
St = np.mean(t)*0.02
Sv = ( (1/np.mean(t)*Sx)**2 +
	   (np.mean(x)/np.mean(t)**2*St)**2 +
	   err[0]**2)**0.5
print "Погрешность скорости:", Sv;

mu = 39.948*10**(-3)
T = 297

v_t = (5./3.*c.R*T/mu)**0.5
print "Теоретическая скорость:", v_t

gamma = mu*v**2/(c.R*T)
Sg = 2*mu*v/(c.R*T)*Sv
print "γ:", gamma
print "Погрешность γ:", Sg

# аргон
# x=[11.0,10.5,10.0,9.5,9,8.5,8.0,7.5]
# t=[5*67,5*64.2,5*59.9,5*57,5*54.1,5*50.8,5*48.8,5*45.6]

# CO2
# x=[11.0,10.5,10.0,9.5,9.0,8.5,8.0,7.5]
# t=[5*80.8,5*78,5*72.8,5*68.8,5*65.4,5*61.8,5*58.5,5*54.7]


plt.plot(x1, y1, color='k')
plt.xlabel(u'Время $t$ распространения сигнала между головками, мкс')
plt.ylabel(u'Расстояние между головками $X$, см')
plt.title(u'График зависимости $X(t)$ для Ar')
plt.grid(color='k', linestyle='-')
# plt.errorbar(t, x, yerr=0.5, color='k', fmt='o')
plt.show()