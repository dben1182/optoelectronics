#%%
import numpy as np
import scipy.constants as scp

wavelength = 630e-9
L = 1e-3
n=3.60

#gets the mode number
m = int((2*L*n)/(wavelength))

wavelength_mod = (2*L*n)/m

delta_lambda = ((2*L)/(m))*10**(-7)

frequency = scp.c/wavelength
print("frequency: ", f"{frequency:e}")

testPoint = 0

