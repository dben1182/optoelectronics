import numpy as np
import scipy.constants as scp
from scipy.optimize import root_scalar


JoulesToEv = 6.242e+18

T = 300

lamb_0 = 1.30e-6

E_g_joules = (scp.c*scp.Planck)/lamb_0 - 0.5*scp.Boltzmann*T
E_g_eV = JoulesToEv*E_g_joules

def Eg_equation(y: float):

    return 0.75 + 0.46*y + 0.14*(y**2) - E_g_eV

sol = root_scalar(Eg_equation, bracket=[0.0,1.0])

y_0 = sol.root

neg_y0 = 1.0-y_0

x_0 = (1-y_0)/2.13

neg_x0 = 1.0-x_0

testPoint = 0

