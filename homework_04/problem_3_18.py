import numpy as np
import scipy.constants as scp
from scipy.optimize import curve_fit

C_to_K = 273.15
joules_to_eV = 6.242e18

T_celsius = [-40, 25, 85]
T_kelvin = [tempT + C_to_K for tempT in T_celsius]

lamb_0 = [804e-9, 822e-9, 837e-9]

#gets the Eg list (emperical)
Eg_list_joules = [(scp.Planck*scp.c/lam) - 0.5*scp.Boltzmann*T_temp for lam, T_temp in zip(lamb_0, T_kelvin)]

Eg_list_eV = [Eg_temp*joules_to_eV for Eg_temp in Eg_list_joules]

def varshni(T, Eg0, A, B):
    return Eg0 - A*T**2/(B+T)

params, _ = curve_fit(varshni, T_kelvin, Eg_list_eV)

Eg0, A, B = params

Eg_test = [Eg0 - A*(T_temp**2)/(B + T_temp) for T_temp in T_kelvin]

testPoint = 0
