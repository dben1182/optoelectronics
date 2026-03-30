import numpy as np
import scipy.constants as scp


lamb = 10.6e-6
g = 0.5
B = 200

nu = scp.c/lamb
T = 300
M = 7.31e-26


Delta_nu = 2*nu*np.sqrt((2*scp.Boltzmann*np.log(2))/(M*(scp.c**2)))

tau_sp = 10e-3

N_th = g*(8*np.pi*(1**2)*(nu**2)*tau_sp*Delta_nu)/((scp.c)**2)


testPoint = 0

