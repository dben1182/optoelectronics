import numpy as np
import scipy.constants as scp


wavelength = 1.50e-6
Temp = 300

joulesToeV = 6.242e+18

n1 = 3.57
n2 = 3.17

bandgap = scp.Planck*scp.c/wavelength - 0.5*scp.Boltzmann*Temp
bandgap_eV = bandgap*joulesToeV

y_roots = np.roots([0.14, 0.46, 0.75-bandgap_eV])


y_temp = y_roots[1]

y_neg = 1-y_temp

x_temp = (1-y_temp)/2.13

x_neg = 1-x_temp

V_num = np.pi/2

d = V_num*wavelength/(np.pi*np.sqrt(n1**2 + n2**2))

testPoint = 0