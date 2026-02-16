import numpy as np
import scipy.constants as sp_c
import matplotlib.pyplot as plt

#plots I vs V for polycrystalline Si solar cell
eta = 2.0
I_0 = 3e-4
I_ph = 5e-3
T = 300

#creates the array for values of R_p
Rp_list = [np.inf, 1000, 100]


#creates a V linspace
V_array = np.linspace(0.0, 0.5, num=1000)
V_list = V_array.tolist()

I_lists = []

for Rp in Rp_list:

    I_temp_list = []

    for V in V_list:

        #gets the total current into the system I
        I_total = -I_ph + I_0*np.exp((sp_c.elementary_charge*V)/(eta*sp_c.Boltzmann*T)) - I_0 + V/Rp
        I_temp_list.append(I_total)

    I_lists.append(I_temp_list)


plt.figure(0)
for I_tempList, Rp_value in zip(I_lists, Rp_list):
    plt.plot(V_list, I_tempList, label=f"Rp = {Rp_value}")
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.legend()
plt.show()



testPoint = 0
