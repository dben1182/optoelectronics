import numpy as np
import scipy.constants as scp


#refractive index
n = 3.7
length = 300e-6
alpha_cm = 20

cm_to_m = 0.01
alpha_s = alpha_cm*cm_to_m


R = 1.0

alpha_t = alpha_s + (1/(2*length))*np.log(1/(R*R))

tau_ph = n/(scp.c*alpha_t)

testPoint = 0
