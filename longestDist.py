import matplotlib.pyplot as plt
from methods import Drag_type, SYS, Phase, polar_to_cartesian
import numpy as np




if __name__ == "__main__":
    v = 700
    fig, ax = plt.subplots(1, 1)
    crashes = []
    thetas = np.linspace(0,90,300)
    for theta in thetas:
        theta *= np.pi / 180
        init_phase = Phase(0, 10, *polar_to_cartesian(v, theta))
        single_crash = []
        for drag_type in [Drag_type.NODRAG, Drag_type.UNIFORM,
                          Drag_type.ISOTHERMAL, Drag_type.ADIABATIC]:

            sys = SYS(init_phase, 0, drag_type=drag_type)
            sys.propagate_until_crash(y_floor=0, dt=1e-1)

            single_crash.append(sys.crash_distance)
        crashes.append(single_crash)
    crashes = np.array(crashes)
    ax.plot(thetas, crashes[:,0], label="Nodrag")
    ax.plot(thetas, crashes[:,1], label="Uniform drag")
    ax.plot(thetas, crashes[:,2], label="Isothermal drag")
    ax.plot(thetas, crashes[:,3], label="Adiabatic drag")
    for i in range(4):
        arg = np.argmax(crashes[:,i])
        print(f"{thetas[arg]=}, {crashes[arg,i]}")
    #ax.set_aspect("equal")
    plt.legend()
    plt.show()