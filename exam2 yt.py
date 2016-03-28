__author__ = 'austin'

import math
import matplotlib.pyplot as plt

dt = 0.01
k = 0.1
b_min = 95
b_max = 136
ylim = 20
xlim = 200

for b in [i * 0.1 for i in range(b_min, b_max)]:

    x = 0.0
    y = 0.0
    y_lst = []
    t_lst = []

    for t in [j * 0.01 for j in range(0, 100000)]:

        y_lst.append(y)
        t_lst.append(t)

        x += (y * dt)
        y += ((- (k * y) - math.sin(x) + (b * math.cos(t))) * dt)
        t += dt

        # print "B: %f\n\tt: %f\n\tx: %f\n\ty: %f\n\tcount: %f" % (b, t, x, y, count)

    plt.figure()
    plt.ylim(-ylim, ylim)
    plt.xlim(-5, xlim)
    plt.gca().set_autoscale_on(False)
    plt.title("b = " + str(b))
    plt.xlabel("t")
    plt.ylabel("y")
    plt.plot(t_lst, y_lst)

plt.show()
