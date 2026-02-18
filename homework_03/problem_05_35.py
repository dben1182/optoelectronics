import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt


#creates a linspace for the 
eta = 2.0
I0 = 3e-7
Iph = 5e-3
T=300

Rp_list = [np.inf, 1000, 100]

#creates a list of test voltages for the input
V_array = np.linspace(0.0, 0.7, 500)
V_list = V_array.tolist()

I_total_list = []
plt.figure(0)

for Rp in Rp_list:

    I_list_current = []
    for V_test in V_list:
        I_diode = I0*(np.exp((scp.elementary_charge*V_test)/(eta*scp.Boltzmann*T)) - 1)
        I_Rp = V_test/Rp
        I_temp = -Iph + I_diode + I_Rp
        I_list_current.append(I_temp)

    plt.plot(V_list, I_list_current, label=f'Rp: {Rp}')


plt.legend()
plt.show()



testPoint = 0
