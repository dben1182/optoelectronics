import numpy as np
import scipy.constants as scp


lamb_list = [850e-9, 1310e-9, 1550e-9]
T = 300.0

spectralWidths = [(lamb_0**2)*(3*scp.Boltzmann*T)/(scp.Planck*scp.c) for lamb_0 in lamb_list]

testPoint = 0
