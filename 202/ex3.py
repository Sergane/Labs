# -*- coding: utf-8 -*-
import numpy as np
import scipy.constants as c

from sympy.solvers import nsolve
from sympy import Symbol, exp

# СО2
x =[a for a in np.arange(0,4.5,0.5)]# list from -4 to 4 (step 0.5)
x =[11.-a for a in x]
t1=[80.2,76.0,73.1,69.3,65.4,62.0,58.4,54.8,51.5]
t2=[80.8,78.0,72.8,68.8,65.4,61.8,58.5,54.7,51.5]
t =[0.5*(t1[i]+t2[i]) for i in range(0,len(t1))]
t =[5*a for a in t]; # умножаем t на 5

n = len(x)
x = map(lambda a: a*10**(-2), x) # переводим в метры
t = map(lambda a: a*10**(-6), t) # переводим в секунды

fit, err, _,_,_ = np.polyfit(t,x,1,full=True)
v = fit[0]

Sx = np.std(x)/(n*(n-1))**0.5
St = np.mean(t)*0.02
Sv = ( (1/np.mean(t)*Sx)**2 +
	   (np.mean(x)/np.mean(t)**2*St)**2 +
	   err[0]**2)**0.5

mu = 44.01*10**(-3)
T = 297
gamma = mu*v**2/(c.R*T)
Sg = 2*mu*v/(c.R*T)*Sv

Ck = (7.0-5.0*gamma)/(2*(gamma-1))*c.R
Sck = c.R/(gamma-1)**2*Sg
print "Cк:", Ck
print "Погрешность Cк:", Sck

a = (7.0-5.0*gamma)/(2*(gamma-1))
# Sa = Sg/(gamma-1)**2
print "a:", a
print "a/2:", a/2

y = Symbol('y')
# последнее число это приблизительный хk
# лучше всего посмотреть на картинке приблизительный х,
# которому соответствует Y=a/2
xk = nsolve(2*y**2*exp(-y)/(1-exp(-y))**2-a, 4.5)
print "xk:", xk
Sxk = 0.05

nu = xk*c.k*T/c.h
Snu = c.k*T/c.h*Sxk
print "Частота:", nu
print "Погрешность частоты:", Snu

Th = c.h*nu/c.k
Sth = T*Sxk
print "Характеристическая темп.:", Th
print "Погрешность хар-кой темп.:", Sth