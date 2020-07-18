import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import kal_python as kal


show_animation = True
tx = []
ty = []

sinwave = kal.wave(0,1,1,"SIN")


for i in range(100):
    t = i/10
    tx.append(t)
    # ty.append(np.sin(2.0*np.pi*t/10 ))
    ty.append(sinwave.update(t))

    if show_animation:  # pragma: no cover
        plt.cla()
        # for stopping simulation with the esc key.
        plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
        plt.plot(tx, ty,"-k")
        plt.xlim(0.0, 10.0)
        plt.ylim(-1, 1)
        # plt.title("v[km/h]:" + str(c_speed * 3.6)[0:4])
        plt.grid(True)
        plt.pause(0.0001)

print("Finish")
if show_animation:  # pragma: no cover
    plt.grid(True)
    plt.pause(0.0001)
    plt.show()
