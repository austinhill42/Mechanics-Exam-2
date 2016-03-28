__author__ = 'austin'

import math
import matplotlib.pyplot as plt

dt = 0.01
k = 1
b_min = 95
b_max = 136
b = 0.7
ylim = 10
xlim = 15

for b in [i * 0.1 for i in range(b_min, b_max)]:

    x = 0.0
    y = 0.0
    x_lst = []
    y_lst = []


    for t in [j * 0.01 for j in range(0, 10000)]:

        x_lst.append(x)
        y_lst.append(y)

        x += (y * dt)
        y += ((- (k * y) - math.sin(x) + (b * math.cos(t))) * dt)
        t += dt

        # print "B: %f\n\tt: %f\n\tx: %f\n\ty: %f\n\tcount: %f" % (b, t, x, y, count)

    plt.figure()
    plt.ylim(-ylim, ylim)
    plt.xlim(-xlim, xlim)
    plt.gca().set_autoscale_on(False)
    plt.title("b = " + str(b))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_lst, y_lst)

plt.show()
