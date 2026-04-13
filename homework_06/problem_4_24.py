import numpy as np
import scipy.constants as scp

eV_To_Joules = 1.60218e-19

Temperature = 300

#sets the bandgap
Bandgap_eV = 1.424
Bandgap = eV_To_Joules*Bandgap_eV

#sets the intrinsic carrier concentration
n_i_cm = 2e6

cm3_to_m3 = 100**3

n_i = cm3_to_m3*n_i_cm


n = n_i*np.sqrt(np.exp(Bandgap/(scp.Boltzmann*Temperature)))

testPoint = 0
