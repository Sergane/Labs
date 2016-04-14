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

# воздух
x =[a for a in np.arange(-4,4.5,0.5)]# list from -4 to 4 (step 0.5)
x =[11.-a for a in x]
t1=[86.6,83.1,80.0,76.9,74.0,71.0,67.9,65.2,
	62.0,59.2,56.0,53.6,50.5,47.6,44.8,41.9,39.0]
t2=[86.4,83.0,80.3,76.9,73.8,71.2,68.4,65.5,
	62.4,59.9,56.8,54.1,50.8,47.7,44.9,42.0,39.0]
t =[0.5*(t1[i]+t2[i]) for i in range(0,len(t1))]
t =[5*float(a) for a in t]; # умножаем t на 5

x =[float(a) for a in x]


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
print("Скорость: "+str(v))
print("Погрешность МНК: "+str(err[0]))

Sx = np.std(x)/(n*(n-1))**0.5
St = np.mean(t)*0.02
Sv = ( (1/np.mean(t)*Sx)**2 +
	   (np.mean(x)/np.mean(t)**2*St)**2 +
	   err[0]**2)**0.5
print("Погрешность скорости: "+str(Sv))

mu = 29*10**(-3)
T = 297

v_t = (7./5.*c.R*T/mu)**0.5
print("Теоретическая скорость: "+str(v_t))

gamma = mu*v**2/(c.R*T)
Sg = 2*mu*v/(c.R*T)*Sv
print("γ: "+str(gamma))
print("Погрешность γ: "+str(Sg))

plt.plot(x1, y1, color='k')
plt.xlabel(u'Время $t$ распространения сигнала между головками, мкс')
plt.ylabel(u'Расстояние между головками $X$, см')
plt.title(u'График зависимости $X(t)$ для воздуха')
plt.grid(color='k', linestyle='-')
plt.show()