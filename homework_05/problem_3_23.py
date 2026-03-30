import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt

T = 300.0

#creates the peak emission wavelength list
lamb_list = [650e-9, 810e-9, 820e-9, 890e-9, 950e-9, 1150e-9, 1270e-9, 1500e-9]

#creates the half width list
halfWidth_list = [22e-9, 36e-9, 40e-9, 50e-9, 55e-9, 90e-9, 110e-9, 150e-9]

#gets the approximated delta without m
unscaled = [scp.Boltzmann*T/(scp.Planck*scp.c)*(lamb**2) for lamb in lamb_list]

m_list = [halfWidth_temp/unscaledTemp for halfWidth_temp, unscaledTemp in zip(halfWidth_list, unscaled)]

m_ave = sum(m_list)/len(m_list)

lamb_space = np.linspace(lamb_list[0], lamb_list[-1], num=500)
line = [(lamb_temp**2)*(m_ave*scp.Boltzmann*T)/(scp.Planck*scp.c) for lamb_temp in lamb_space]


#plots the two
plt.figure()
plt.scatter(lamb_list, halfWidth_list)
plt.plot(lamb_space, line, color='orange')
plt.show()


 



testPoint = 0
