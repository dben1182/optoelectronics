import numpy as np
import scipy.constants as scp
from machinevisiontoolbox import rluminos


P_opt = 710e-3
lamb = 455e-9
I = 350e-3
V = 3.2


nu = scp.c/lamb


PCE = P_opt/(I*V)
eta_EQE = ((P_opt)/(scp.Planck*nu))/((I)/scp.elementary_charge)


V_lamb = rluminos(lamb)
lumens_per_watt = 683
efficacy = V_lamb*lumens_per_watt


testPoint = 0
