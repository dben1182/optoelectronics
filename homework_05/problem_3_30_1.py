import numpy as np
import scipy.constants as scp
from machinevisiontoolbox import rluminos


lamb_0 = 538e-9
nu = scp.c/lamb_0
I = 350e-3
V = 3.4
#in lumens
luminous_flux = 92

V_lamb = rluminos(lamb_0)
lumens_per_watt = 683
efficacy = V_lamb*lumens_per_watt

P_0 = luminous_flux / (V_lamb*lumens_per_watt)

PCE = P_0 / (I*V)

eta_EQE = ((P_0)/(scp.Planck*nu))/(I/scp.elementary_charge)

testPoint = 0
