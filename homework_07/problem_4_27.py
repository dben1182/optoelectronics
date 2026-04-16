#%%
import numpy as np
import scipy.constants as scp
import sympy as sp
from IPython.display import display

eV_to_joules = 1.60218e-19
lamb = 1550e-9
#the length of the fabry perot cavity
LD_cavityLength = 250e-6
#the index of refraction of the ingas
n_InGaAsP = 3.60
#the index of refraction of the air
n_air = 1.0
#the derivative of the index of refraction with respect to temperature
dn_dT = 2e-4

#the therman expansion coefficient
#that is the derivative of length with respect to a change in temperature
alpha_t = 5.6e-6
dL_dT = alpha_t*LD_cavityLength

#sets the bandgap
InGaAs_Eg0_eV = 0.850
InGaAs_Eg0 = InGaAs_Eg0_eV*eV_to_joules
InGaAs_A_eV = 4.906e-4
InGaAs_A = InGaAs_A_eV*eV_to_joules
InGaAs_B = 301
Temp = 298

InGaAs_Eg = InGaAs_Eg0 - InGaAs_A*(Temp**2)/(InGaAs_B + Temp)

#cerates the temperature as a variable
T = sp.symbols('T')
#creates alpha as a constant
alpha_s = sp.symbols('alpha_s')

#creates L as a function of temperature
L = sp.Function('L')(T)
R = sp.Function('R')(T)
#

#definds the gain
g_th = alpha_s - (1 / L)*sp.ln(R)
display("g th")
display(g_th)


d_g_dT = sp.diff(g_th, T)
display("g th diff")
display(d_g_dT)



n1 = sp.Function('n_1')(T)

n2 = sp.symbols('n_2')

R = ((n1 - 1)/(n1 + 1))**2


display(R)

dR_dn1 = sp.simplify(sp.diff(R, T))
display(dR_dn1)

#wavelength section of this problem


A, B, E_g0 = sp.symbols('A B E_{g0}')
h, c = sp.symbols('h c')
E_g = E_g0 - (A*T**2)/(B + T)

Wavelength_sym = h*c/(E_g)
display(Wavelength_sym)

d_Wavelength_dT = sp.simplify(sp.diff(Wavelength_sym, T))
display("d lambda dT")
display(d_Wavelength_dT)


d_Eg_dT = sp.diff(E_g, T)
display("d Eg dT")
display(d_Eg_dT)


#numerical section

#gets the numerical reflection coefficient
num_R = ((n_InGaAsP - 1)/(n_InGaAsP + 1))**2
#gets the derivative of R with respect to T at the current temperature
num_dR_dT = (4*(n_InGaAsP - 1)*dn_dT)/((n_InGaAsP + 1)**3)
num_dg_dT = -(num_dR_dT/(LD_cavityLength*num_R)) - ((np.log(1/(num_R**2)))*dL_dT/(2*(LD_cavityLength**2)))


#gets the output wavelength
num_Eg = InGaAs_Eg0 - (InGaAs_A*(Temp**2))/(InGaAs_B + Temp)
num_wavelength = scp.c*scp.Planck/num_Eg



#gets the derivative of EG with respect to temperature
num_dEg_dT = ((InGaAs_A*(Temp**2)/((InGaAs_B + Temp)**2))) - (2*InGaAs_A*InGaAs_B)/(InGaAs_B + Temp)

num_dLambda_dT = (-scp.Planck*scp.c/(num_Eg**2))*num_dEg_dT

#gets the derivative of the wavelength output with respect to the change in temperature

'''
dLamb_dT_top = (scp.c*scp.Planck*InGaAs_A*Temp*(2*InGaAs_B + Temp))
dLamb_dT_bottom = (A*Temp**2 - InGaAs_Eg0*(InGaAs_B + Temp))**2
num_dLamb_dT = dLamb_dT_top/dLamb_dT_bottom
#'''


testPoint = 0
# %%
