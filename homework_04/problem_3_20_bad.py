import numpy as np
import scipy.constants as scp


E_go = 1.519
A = 5.41e-4
B = 204

T_temp = 300


def get_Eg(T: float):

    return E_go - (A*T**2)/(B + T)

def get_nu(T: float):

    Eg_temp = get_Eg(T=T)
    part1 = Eg_temp/scp.Planck
    part2 = (scp.Boltzmann*T)/(2*scp.Planck)

    return Eg_temp/scp.Planck + (scp.Boltzmann*T)/(2*scp.Planck)



Eg_temp = get_Eg(T=T_temp)
nu_temp = get_nu(T=T_temp)


testPoint = 0
