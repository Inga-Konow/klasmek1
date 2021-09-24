from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np

#Constants and parameters:

v_0 = 700  # firing velocity in m/s
theta = 45  # firing angle in degrees

a = 6.5e-3  # constant in adiabatic approximation?
y_0 = 1e4  # k_B*T/mg
alfa = 2.5  # constant for air?
drag_coefficient = 4e-5  # per air particle mass, in m^-1#!/usr/bin/python
g=9.81

# Sistnevnte er en bash-kommando for aa kjore resten av filen i python
# om filen kjores direkte fra kommandolinjen
from typing import Callable, Tuple, NamedTuple


def RK4(f: Callable[[any,float], float], y: any, t: float, dt: float) -> Tuple[any, float]:
	k_1 = f(y, t)
	k_2 = f(y+k_1*dt/2, t+dt/2)
	k_3 = f(y+k_2*dt/2, t+dt/2)
	k_4 = f(y+k_3*dt, t+dt)
	y_next = y + 1/6*(k_1+2*k_2+2*k_3+k_4)*dt
	return y_next, t+dt


def Euler(f: Callable[[any, float], float], y:any, t:float, dt:float) -> Tuple[any, float]:
	k_1 = f(y, t)
	y_next = y + k_1*dt
	return y_next, t+dt


def crossing(ph_1: Phase, ph_2: Phase, y_crossing: float) -> Union[float, bool]:
	if not ((ph_1.y < y_crossing) ^ (ph_2.y < y_crossing)):
		return False
	r = -ph_1.y/ph_2.y
	return (r*ph_2.x + ph_1.x)/(r+1)


	

class Phase(NamedTuple):
	x: float
	y: float
	v_x: float
	v_y: float

	def __add__(self, rhs:phase):
		return Phase(*[l+r for l,r in zip(self, rhs)])

	def __radd__(self, lhs:phase):
		return self + lhs

	def __mul__(self, rhs:float):
		return Phase(*[l*rhs for l in self])

	def __rmul__(self, lhs:float):
		return self*lhs

	def __truediv__(self, rhs:float):
		return self*(1/rhs)


def f(ph: Phase, t: float):
	return Phase(ph.v_x, ph.v_y, 0, -g)

if __name__ == "__main__":
	dt = 1e-2
	phases = [Phase(0, 10, 4, 10)]
	ts = [0]
	while True:
		current_phase = phases[-1]
		t = ts[-1]
		next_phase, t_next = RK4(f, current_phase, t, dt)
		if (x_cross := crossing(current_phase, next_phase, 0)) is False:
			phases.append(next_phase)
			ts.append(t_next)
			continue
		print(f"CROSSED AT {x_cross=}")
		break

	phase_array = np.array(phases)
	ts = np.array(ts)
	plt.figure(0)
	plt.plot(phase_array[:,0], phase_array[:,1], label="y")
	plt.show()