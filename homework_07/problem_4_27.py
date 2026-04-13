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
d_L_dT = 5.6e-6

#sets the bandgap
InGaAs_Eg0_eV = 0.850
InGaAs_Eg0 = InGaAs_Eg0_eV*eV_to_joules
A_eV = 4.906e-4
A = A_eV*eV_to_joules
B = 301
Temp = 298

InGaAs_Eg = InGaAs_Eg0 - A*(Temp**2)/(B + Temp)

#cerates the temperature as a variable
T = sp.symbols('T')
#creates alpha as a constant
alpha_s = sp.symbols('alpha_s')

#creates L as a function of temperature
L = sp.Function('L')(T)
R = sp.Function('R')(T)
#

#definds the gain
g_th = alpha_s + (1 / (2*L))*sp.ln(1/(R**2))
display(g_th)

d_g_dT = sp.diff(g_th, T)
display(d_g_dT)




testPoint = 0
# %%

R_new = 




# %%
