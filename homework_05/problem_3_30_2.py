import numpy as np
import scipy.constants as scp
from machinevisiontoolbox import rluminos

P_0 = 320e-3
lamb = 656e-9
I = 400e-3
V = 215
nu = scp.c/lamb


PCE = P_0/(I*V)
eta_EQE = ((P_0)/(scp.Planck*nu))/((I)/scp.elementary_charge)


V_lamb = rluminos(lamb)
lumens_per_watt = 683
efficacy = V_lamb*lumens_per_watt


testPoint = 0
