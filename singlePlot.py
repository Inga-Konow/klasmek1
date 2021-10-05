import matplotlib.pyplot as plt
from methods import Drag_type, SYS, Phase, polar_to_cartesian
import numpy as np




if __name__=="__main__":
    v = 700
    fig, ax = plt.subplots(1,1)
    initial_phase = Phase(0, 0, *polar_to_cartesian(v, np.pi/4))
    launch = SYS(initial_phase, drag_type=Drag_type.NODRAG)
    launch.propagate_until_crash(y_floor=0, dt=1e-3)
    phases = launch.phases
    xs, ys, vxs, vys = np.array(phases).T
    ax.plot(xs, ys, label="No drag")
    ax.legend()
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    plt.show()
    print(f"The projectile range is {launch.crash_distance}")


