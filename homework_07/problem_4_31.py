import numpy as np
import scipy.constants as scp

wavelength = 630e-9
frequency = scp.c/wavelength

Temperature_C = 25.0
Temperature = Temperature_C + 273.15
I_th = 45e-3
V_operating = 2.3

I_output = 95e-3
P_output = 30e-3

eta_eqe = (P_output/(scp.Planck*frequency))/(I_output/scp.elementary_charge)

Bandgap = scp.Planck*frequency

eta_edqe = (scp.elementary_charge/Bandgap)*(P_output/(I_output - I_th))

#gets the power conversion efficiency
eta_pce = eta_eqe*(Bandgap/(scp.elementary_charge*V_operating))
eta_pce_2 = P_output/(I_output*V_operating)

eta_slope = P_output/(I_output - I_th)


P_output_2 = 20e-3
I_output_2 = (scp.elementary_charge*P_output_2)/(Bandgap*eta_eqe)

I_th_2 = 70e-3
Temperature_2 = 50 + 273.15

#gets T_0
T_0 = (Temperature - Temperature_2)/(np.log(I_th) - np.log(I_th_2))

A = np.exp(np.log(I_th) - Temperature/T_0)


T_in = 0+273.15

I_th_3 = A*np.exp(T_in/T_0)


testPoint = 0