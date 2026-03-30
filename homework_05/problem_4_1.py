import numpy as np
import scipy.constants as scp

k = 2
L = 0.5
g = k/L
G = np.exp(g*L)

eV_to_J = 1.602e-19

P_eV = 3.0

P_joules = P_eV*eV_to_J 
#gets the frequency and wavelenth
nu = P_joules/scp.Planck
lamb = scp.c/nu

#in centimeters
diameter = 0.7
radius = diameter/2.0
length = 5.0

Volume = np.pi*(radius**2)*length

tau_sp = 3e-3


cm_per_meter = 100

#ion concentration
N_0 = 1e20

P_min = Volume*(N_0/2.0)*P_joules/tau_sp


testPoint = 0
