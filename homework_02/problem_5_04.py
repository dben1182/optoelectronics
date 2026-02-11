import numpy as np


#sets the electron charge In Coulomb
q_e = 1.60218e-19
#set's plank's constant
h = 6.6261e-34
#and the speed of light
c = 2.99e8

#creates the parameters for p+n and then pin
l_p = [0.5e-6, 0.5e-6]
L_e = [0.1e-6, 0.1e-6]
W = [1e-6, 30e-6]
L_h = [10e-6, 0.1e-6]
alpha = [1e5, 1e5]
I_ph = [0.42e-6, 0.59e-6]

eta_i = 1.0
lamb = 900e-9
nu = c/lamb
P_0 = 1e-6
T = 1.0

I_ph_plus = ((q_e*eta_i*T*P_0)/(h*nu))*(np.exp(-alpha[0]*(l_p[0] - L_e[0])) - np.exp(-alpha[0]*(l_p[0] + W[0] + L_h[0])))

I_ph_pin = ((q_e*eta_i*T*P_0)/(h*nu))*(np.exp(-alpha[1]*(l_p[1] - L_e[1])) - np.exp(-alpha[1]*(l_p[1] + W[1] + L_h[1])))



testPoint = 0
