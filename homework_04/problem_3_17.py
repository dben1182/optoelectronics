import numpy as np
import matplotlib.pyplot as plt

#for heterojunction N+p
A_V = [0.206, 0.244, 0.290, 0.322, 0.362, 0.412, 0.453, 0.485, 0.537, 0.576, 0.612, 0.662, 0.708]
A_I = [1.03e-9, 2.07e-9, 5.20e-9, 10.3e-9, 20.7e-9, 52.8e-9, 105.0e-9, 192.0e-9, 515.0e-9, 1.02e-6, 2.03e-6, 4.89e-6, 10.1e-6]

#for heterojunction P+n
B_V = [0.310, 0.364, 0.402, 0.433, 0.485, 0.521, 0.561, 0.608, 0.682, 0.726, 0.764, 0.807, 0.859, 0.885]
B_I = [2.01e-9, 4.91e-9, 9.79e-9, 19.0e-9, 49.5e-9, 96.1e-9, 194.0e-9, 466.0e-9, 1.96e-6, 5.02e-6, 9.75e-6, 19.5e-6, 50.6e-6, 99.5e-6]


fig, ax1 = plt.subplots(1, 1, sharex=True)

ax1.plot(A_V, A_I, label="Heterojunction N+p")
ax1.plot(B_V, B_I, label="Heterojunction P+n")
ax1.legend()
ax1.grid(True)


plt.show()
