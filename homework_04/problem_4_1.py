import numpy as np
import scipy.constants as scp
from scipy.optimize import root_scalar


JoulesToEv = 6.242e+18

T = 300

lamb_0 = 1.55e-6

E_g_joules = (scp.c*scp.Planck)/lamb_0 - 0.5*scp.Boltzmann*T
E_g_eV = JoulesToEv*E_g_joules


def Eg_y(y: float):

    return 1.36 - 0.72*y + 0.12*y**2 - 0.787


sol = root_scalar(Eg_y, bracket=[0.0,1.0])

Arsenide_ratio = sol.root

Phosphorus_ratio = 1.0 - Arsenide_ratio

Gallium_ratio = Arsenide_ratio/2.16

Indium_ratio = 1.0 - Gallium_ratio

testPoint = 0
