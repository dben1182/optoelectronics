import numpy as np
import matplotlib.pyplot as plt


Vr = [30.6, 33.5, 36.6, 39.5, 41.9, 43.4, 44.3, 45.46, 45.92, 46.21]
M = [1.78, 2.16, 2.74, 3.74, 5.34, 7.21, 9.0, 14.2, 19.5, 24.8]

#gets the f
f_list = [(1 - 1/M_temp) for M_temp in M]

#gets the line of best fit here
m, b = np.polyfit(f_list, Vr, 1)


#gets the Vbr list
Vbr = [Vr_temp/((1-1/M_temp)**(1/m)) for Vr_temp, M_temp in zip(Vr, M)]

plt.figure(0)
plt.loglog(f_list, Vr, label="Vr ")
plt.loglog(f_list, Vbr, label="Vbr")
plt.xlabel('1 - 1/M')
plt.ylabel('Vr')
plt.legend()
plt.show()


testPoint = 0
