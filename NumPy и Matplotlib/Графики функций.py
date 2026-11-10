import numpy as np
import matplotlib.pyplot as plt

nmin = 0
nmax = 2 * np.pi
count = 400

x = np.linspace(nmin, nmax, count)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

id_max = np.argmax(y3)
id_min = np.argmin(y3)

xmax = x[id_max]
y3max = y3[id_max]

xmin = x[id_min]
y3min = y3[id_min]

y3x = np.linspace(xmax, xmax, count)
y3_line = np.linspace(-20, y3max, count)

plt.figure(figsize=(12, 5))
plt.ylim(-y3max * 1.1, y3max * 1.1)
plt.plot(x, y1, label='Y1 sin(x)', linewidth=1)
plt.plot(x, y2, label='Y2 cos(x)', linewidth=2)
plt.plot(x, y3, label='Y3 sin(x) + cos(x)', linewidth=3, linestyle='--')

plt.scatter(xmax, y3max, label='Y3 Max', s=30, zorder=4, color='red')
plt.plot(y3x, y3_line, linestyle='--')
plt.legend()

plt.show()
