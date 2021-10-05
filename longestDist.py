import matplotlib.pyplot as plt
from methods import Drag_type, SYS, Phase, polar_to_cartesian
import numpy as np

if __name__ == "__main__":
    v = 700
    fig, ax = plt.subplots(1, 1)
    crashes = []
    thetas = np.linspace(0, 90, 100)
    for drag_type in [Drag_type.NODRAG, Drag_type.UNIFORM,
                        Drag_type.ISOTHERMAL, Drag_type.ADIABATIC]:
        single_crash = []
        for theta in thetas:
            theta *= np.pi / 180
            init_phase = Phase(0, 0, *polar_to_cartesian(v, theta))
            sys = SYS(init_phase, 0, drag_type=drag_type)
            sys.propagate_until_crash(y_floor=0, dt=1e-1)
            single_crash.append(sys.crash_distance)
        arg = np.argmax(single_crash)
        max_theta = thetas[arg]

        thetas = np.linspace(thetas[arg-1], thetas[arg+1], 100)
        print(thetas[arg])
        single_crash = []
        for theta in thetas:
            theta *= np.pi / 180
            init_phase = Phase(0, 0, *polar_to_cartesian(v, theta))
            sys = SYS(init_phase, 0, drag_type=drag_type)
            sys.propagate_until_crash(y_floor=0, dt=1e-1)
            single_crash.append(sys.crash_distance)
        arg = np.argmax(single_crash)
        print(f"Maximal angle for {drag_type.value.lower()} is {thetas[arg]:.5f}, which gives a range of {single_crash[arg]:.6g}")
        max_theta = thetas[arg] * np.pi/180

        best_phase = Phase(0, 0, *polar_to_cartesian(v, max_theta))

        max_sys = SYS(best_phase, 0, drag_type=drag_type)
        max_sys.propagate_until_crash(y_floor=0, dt=1e-1)
        xs, ys, vxs, vys = np.array(max_sys.phases).T
        ax.plot(xs, ys, label=drag_type.value)
    ax.set_xlabel(r"$x[m]$")
    ax.set_ylabel(r"$y[m]$")
    plt.show()


