import numpy as np
import scipy.constants as spc

P_in = 10e-3
lam = 0.8e-6
eta = 1.0

I0 = 10e-9
T = 300

#gets the photocurrent in reverse bias mode:
Iph = P_in * eta * (spc.elementary_charge*lam)/(spc.Planck*spc.c)

Voc = (eta*spc.Boltzmann*T/(spc.elementary_charge))*np.log(Iph/I0 + 1)

testPoint = 0
