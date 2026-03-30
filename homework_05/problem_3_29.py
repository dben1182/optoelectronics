import numpy as np
import scipy.constants as scp


lamb = 890e-9
#1/cm^3
dopedDensity = 4e-17
Tau_nr = 60e-9
I = 50e-3
V = 1.4
P_opt = 10e-3
B = 1e-16
Na = 2e23


nu = scp.c/lamb

test_c = nu*lamb

#gets the radiative tau
Tau_r = 1/(B*Na)
#gets the internal quantum efficiency
eta_IQE = (Tau_r**(-1))/(Tau_r**(-1) + Tau_nr**(-1))

eta_EQE = ((P_opt)/(scp.Planck*nu))/((I)/(scp.elementary_charge))

PCE = P_opt/(I*V)

eta_EE = P_opt/(scp.Planck*nu*eta_IQE*(I/scp.elementary_charge))

testPoint = 0
