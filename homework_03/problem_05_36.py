import numpy as np
import scipy.constants as spc
import matplotlib.pyplot as plt
from scipy.optimize import fsolve




I0 = 25e-9
eta = 1.5
Iph = 10e-3
T = 300



def currentSum(Vd, Vin, Rs):

    #gets the diode current
    I_d = diodeCurrent(Vd=Vd)
    I_input = inputCurrent(Vin=Vin, Vd=Vd, Rs=Rs)
    sum = -Iph + I_d - I_input
    return sum

def inputCurrent(Vin, Vd, Rs):
    return (Vin - Vd)/Rs

def diodeCurrent(Vd):
    current_d = I0*(np.exp((spc.elementary_charge*Vd)/(eta*spc.Boltzmann*T)) - 1.0)
    return current_d


Rs_list = [0, 30, 100]

#creates a Linspace on the Load Resistances 
V_array = np.linspace(0.0, 3.0, 500)
V_list = V_array.tolist()

I_total_list = []

plt.figure()

for Rs in Rs_list:

    I_temp_list = []

    for V_test in V_list:

        #find the numerical solution for V diode
        V_diode = fsolve(currentSum, x0=0.0, args=(V_test, Rs))[0]

        #gets the input current given the diode voltage and the test voltage
        I_input = inputCurrent(Vin=V_test,
                               Vd=V_diode,
                               Rs=Rs)
        I_temp_list.append(I_input)

    plt.plot(V_list, I_temp_list, label=f'Rs: {Rs}')

plt.legend()
plt.show()

