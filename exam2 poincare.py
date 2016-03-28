__author__ = 'austin'

import math
import matplotlib.pyplot as plt

dt = 0.01
k = 0.1
b_min = 95
b_max = 136
ylim = 15
xlim = 25

for b in [i * 0.1 for i in range(b_min, b_max)]:

    x = 0.0
    y = 0.0
    x_lst = []
    y_lst = []
    poin_x_lst = []
    poin_y_lst = []
    count = 0.1

    for t in [j * 0.01 for j in range(0, 100000)]:

        x_lst.append(x)
        y_lst.append(y)

        if count > 3.14:
            poin_x_lst.append(x)
            poin_y_lst.append(y)
            count = 0.0

        x += (y * dt)
        y += ((- (k * y) - math.sin(x) + (b * math.cos(t))) * dt)
        t += dt
        count += 0.01

        # print "B: %f\n\tt: %f\n\tx: %f\n\ty: %f\n\tcount: %f" % (b, t, x, y, count)

    plt.figure()
    plt.ylim(-ylim, ylim)
    plt.xlim(-xlim, xlim)
    plt.gca().set_autoscale_on(False)
    plt.title("b = " + str(b))
    plt.plot(poin_x_lst, poin_y_lst, marker='.', linestyle='')

plt.show()
