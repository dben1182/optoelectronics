import numpy as np
import scipy.constants as scp


wavelength = 1.60e-6
Temp = 300

joulesToeV = 6.242e+18

d = 30e-9

m_eh = 0.05*scp.electron_mass

eps_1 = (scp.Planck**2)*(1**2)/(8*m_eh*(d**2))

Eg = (scp.Planck*scp.c/wavelength) - 2*eps_1
Eg_ev = Eg*joulesToeV


y_roots = np.roots([0.14, 0.46, 0.75-Eg_ev])


y_temp = y_roots[1]

y_neg = 1-y_temp

x_temp = (1-y_temp)/2.13

x_neg = 1-x_temp



testPoint = 0