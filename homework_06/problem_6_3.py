import numpy as np
import scipy.constants as scp

n = 3.6
length = 200e-6
loss = 800
eta = 0.8

bandgap_GaAs_eV = 1.424
eV_to_Joules = 1.60218e-19
bandgap = bandgap_GaAs_eV*eV_to_Joules

#gets the Reflection coefficient
Ref = ((1.0-n)**2)/((1.0+n)**2)

#gets the efficiency per volt
efficiency = eta*(bandgap/scp.elementary_charge)*(np.log(1/Ref)/(loss*length + np.log(1/Ref)))



testPoint = 0
