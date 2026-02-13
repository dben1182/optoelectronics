import numpy as np
import scipy.constants as sp_c

#sets the temperature at 300 kelvin
T = 300


#500 watts per meter squared
intensity_1 = 500
I_sc_1 = 16e-3
V_oc_1 = 0.5
eta = 1.0

#gets the photocurrent for the second inntensity
intensity_2 = 2.0*intensity_1
I_sc_2 = (intensity_2/intensity_1)*I_sc_1


#gets the different in open circuit voltage Voc2 - Voc1
V_oc_difference = ((eta*sp_c.Boltzmann*T)/sp_c.elementary_charge)*np.log(intensity_2/intensity_1)

#gets the V_oc2
V_oc_2 = V_oc_difference + V_oc_1


testPoint = 0
