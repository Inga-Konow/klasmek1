#Constants and parameters:

v_0 = 700 #firing velocity in m/s
theta = 45 #firing angle in degrees

a = 6.5e-3 #constant in adiabatic approximation?
y_0 = 1e4 #k_B*T/mg
alfa = 2.5 #constant for air?
drag_coefficient = 4e-5 #per air particle mass, in m^-1#!/usr/bin/python
#Sistnevnte er en bash-kommando for aa kjore resten av filen i python
	#om filen kjores direkte fra kommandolinjen
from typing import Callable, Tuple, NamedTuple

def RK4(f: Callable[[any], float], y:any, t:float, dt:float) -> Tuple[any, float]:
	k_1 = f(y, t)
	k_2 = f(y+k_1*dt/2, t+dt/2)
	k_3 = f(y+k_2*dt/2, t+dt/2)
	k_4 = f(y+k_3*dt, t+dt)
	y_next = y + 1/6*(k_1+2*k_2+2*k_3+k_4)*dt
	return y_next, t+dt
	

class phase(NamedTuple):
	x: float
	y: float
	v_x: float
	v_y: float
	def __add__(self, rhs:phase)
		return (l+r for l,r in zip(self, rhs)
	def __radd__(self, lhs:phase):
		return self + lhs
	def __mul__(self, rhs:float):
		return (elem*rhs for elem in self)
	def __rmul__(self, lhs:float):
		return self*lhs


g=9.81
def f(ph:phase, t:float):
	return(ph.v_x, ph.v_y, 0, -g)

import matplotlib.pyplot as plt	
import numpy as np

 __name__ == "__main__":
	dt = 1e-2
	ys = [phase(0,10,4,10)]
	ts = [0]
	while t<2.0:
		y_next, t_next=RK4(f, y, t, dt)
		ys.append(y_next)
		ts.append(t_next)
	yvals = np.array(ys)
	ts = np.array(ts)
	print(yvals[:,1])

