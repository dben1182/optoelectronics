#%%
import numpy as np
import scipy.constants as scp


def getFr(tau, tau_ph, I_ratio):

    return (1/(2*np.pi*np.sqrt(tau*tau_ph)))*np.sqrt(I_ratio - 1)

#radiative lifetime
tau_r = 2e-9
#nonradiative lifetime
tau_nr = 50e-9
#total attenuation coefficient
alpha_t = 6000
#refractive index
n = 3.6
#gets the photon cavity lifetime
tau_ph = n/(scp.c*alpha_t)

#gets tau, the effective carrier recombination time
tau = 1/(1/tau_r + 1/tau_nr)


#we need to find the relaxation oscillation frequency

#for I1 = 2*Ith
I_ratio_2 = 2
fr_2 = getFr(tau=tau, tau_ph=tau_ph, I_ratio=I_ratio_2)
print("Fr 2: ", f'{fr_2:e}')

#for I1 = 3*Ith
I_ratio_3 = 3
fr_3 = getFr(tau=tau, tau_ph=tau_ph, I_ratio=I_ratio_3)
print("Fr 3: ", f"{fr_3:e}")


#gets the delay time to go from 0.9 Ith to 2 Ith

td_1 = tau*np.log((2)/(2-(1-0.9)))
print("td 1: ", f"{td_1:e}")


td_2 = tau*np.log((2)/(2-(1-0)))
print("td 2: ", f"{td_2:e}")


testPoint = 0
# %%
