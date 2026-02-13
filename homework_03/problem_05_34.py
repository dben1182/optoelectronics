import numpy as np
import scipy as sp
import scipy.constants as sp_c

eta = 1.0
T = 300.0

#sets the intensity of the light initially
intensity_1 = 250
Isc_1 = -50e-3
Voc_1 = 0.55


intensity_2 = 2.0*intensity_1
Isc_2 = (intensity_2/intensity_1)*Isc_1

Voc_2 = Voc_1 + (eta*sp_c.Boltzmann*T/(sp_c.elementary_charge))*np.log(intensity_2/intensity_1)


testPoint = 0
