import numpy as np
import scipy.constants as scp

E_go = 1.519
A = 5.41e-4
B = 204

#number of joules per eV (A Joule is WAY larger than an electron Volt)
Joules_per_eV = 1.602e-19

C_to_K = 273.15

T_temp = 300

#returns the energy in Joules
def get_Eg(T: float):

    Eg_eV = E_go - (A*T**2)/(B + T)

    Eg_Joule = Eg_eV*Joules_per_eV

    return Eg_Joule

#returns the change in energy in Joules
def get_dEg_dT(T: float):

    dEg_dT_eV = -(A*T*(T + 2*B))/((B+T)**2)

    dEg_dT_Joules = Joules_per_eV*dEg_dT_eV
    return dEg_dT_Joules

def get_lamb(T: float):

    Eg = get_Eg(T=T)

    return scp.c*scp.Planck/(Eg + 0.5*scp.Boltzmann*T)

def get_d_lamb_dT(T: float):

    #gets the energy bandgap
    Eg_temp = get_Eg(T=T)
    #gets the change of energy with respect to change in temperature
    d_Eg_dT_temp = get_dEg_dT(T=T)

    return -scp.c*scp.Planck*(d_Eg_dT_temp + 0.5*scp.Boltzmann)/((Eg_temp + 0.5*scp.Boltzmann*T)**2)

def v_to_lambda(nu: float):

    lam = scp.c/nu
    return lam

#gets the change in lambda
T_setPoint = 300
delta_lambda = get_d_lamb_dT(T=T_setPoint)
delta_lambda_nm = delta_lambda*1e9

T_list_C = [27, -30]
T_list_K = [tempT + C_to_K for tempT in T_list_C]

lamb_list = [get_lamb(T=tempT) for tempT in T_list_K]

lamb_list_nm = [lamb_temp*1e9 for lamb_temp in lamb_list]

testPoint = 0
