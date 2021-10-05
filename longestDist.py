import matplotlib.pyplot as plt
from methods import Drag_type, SYS, Phase, polar_to_cartesian
import numpy as np

if __name__ == "__main__":
    v = 700
    fig, ax = plt.subplots(1, 1)
    crashes = []
    thetas = np.linspace(0,90,300)
    for drag_type in [Drag_type.NODRAG, Drag_type.UNIFORM,
                        Drag_type.ISOTHERMAL, Drag_type.ADIABATIC]:
        single_crash = []
        for theta in thetas:
            theta *= np.pi / 180
            init_phase = Phase(0, 10, *polar_to_cartesian(v, theta))
            sys = SYS(init_phase, 0, drag_type=drag_type)
            sys.propagate_until_crash(y_floor=0, dt=1e-1)
            single_crash.append(sys.crash_distance)
        arg = np.argmax(single_crash)
        print(f"Maximal angle for {drag_type.value.lower()} is {thetas[arg]:.4g}, which gives a range of {single_crash[arg]:.6g}")
