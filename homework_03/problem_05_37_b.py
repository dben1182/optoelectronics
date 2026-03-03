import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as scp

K_conversion = 273.15

def getIntensity(alpha: float):

    a = 1.353
    b = 0.7
    c = 0.678

    Intensity = a * (b)**((1.0/(np.sin(alpha)))**c)

    return Intensity

#the parameters for when Intensity is 1 Kw/m^2
Voc_max = 0.45
Isc_max = 400e-3
Intensity_max = 1.0
T_C_max = 27
T_max = T_C_max + K_conversion
Fill_factor_max = 0.73
eta = 1.0

#gets the K
K = -Isc_max / Intensity_max


#gets I0 from the original tests
I0 = Isc_max /(np.exp(scp.elementary_charge*Voc_max/(eta*scp.Boltzmann*T_max)) - 1.0)

phi_deg = 63
phi = np.radians(phi_deg)
alpha = np.pi/2 - phi

T_C_eskimo = -10.0
T_eskimo = T_C_eskimo + K_conversion

#gets the intensity at that alpha
Intensity_eskimo = getIntensity(alpha=alpha)

#gets the short circuit current
Isc_eskimo = (Intensity_eskimo/Intensity_max)*Isc_max

#calculates the Open circuit voltage for eskimo
Voc_eskimo = Voc_max + ((eta*scp.Boltzmann*T_C_eskimo)/(scp.elementary_charge))*np.log(Isc_eskimo/Isc_max)


#creates a linspace for R load
R_load = np.linspace(0.0, 100e3, 1000)



testPoint = 0
