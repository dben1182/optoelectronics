import numpy as np
import scipy.constants as scp

diameters = [65.1e-6, 139.5e-6, 365.25e-6]
areas = [np.pi*(dia/2)**2 for dia in diameters]
resistances = [12, 12, 12.5]

relative_permittivity = 3.9
thickness = 5e-7

#gets the capacitances 
capacitances = [relative_permittivity*scp.epsilon_0*area/thickness for area in areas]
cornerFrequencies = [1/(2*np.pi*res*cap) for res, cap in zip(resistances, capacitances)]

testpoint = 0
