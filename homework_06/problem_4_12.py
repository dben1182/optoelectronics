import numpy as np
import scipy.constants as scp

lamb = 488e-9
delta_nu = 5e9


nu = scp.c/lamb

rho = 8*np.pi*scp.Planck*(nu**3)/(scp.c**3)

N_ph = rho*(delta_nu)/(scp.Planck*nu)

testPoint = 0
