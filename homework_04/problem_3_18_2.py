import numpy as np
import scipy.constants as scp
from scipy.optimize import root_scalar


joules_to_eV = 6.242e18
T_C = 25
C_to_K = 273.15
T_k = T_C + C_to_K
joules_to_eV = 6.242e18
lambda_0 = 822e-9


E_g_joules = (scp.c*scp.Planck/lambda_0) - 0.5*scp.Boltzmann*T_k
E_g_eV = E_g_joules*joules_to_eV


def Eg_comp(comp: float):
    return 1.424 + 1.266*comp + 0.266*comp**2 - E_g_eV


solution = root_scalar(Eg_comp, bracket=[0.0,1.0])

sol = solution.root


sol_test = Eg_comp(comp=sol)

testPoint = 0
