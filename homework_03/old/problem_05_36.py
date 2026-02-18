import numpy as np
import scipy.constants as spc
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


I0 = 25e-9
eta = 1.5
Rp = np.inf
Iph = 10e-3
T = 300.0

Rs_list = [0, 30, 100]
V_max = 5.0

#creates the linspace of v
V_array = np.linspace(0.0, V_max, 500)

V_in_list = V_array.tolist()

currentSumSolution = 0.0

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

plt.figure(0)

I_total_list = []

for Rs in Rs_list:

    testPoint = 0
    I_input_temp_list = []

    for V_in in V_in_list:

        #gets the Vd solution, given the input voltage
        Vd_solution = fsolve(currentSum, x0=currentSumSolution, args=(V_in, Rs))[0]

        #gets the current input (Current throug the cell)
        I_input = inputCurrent(Vin=V_in,Vd=Vd_solution,Rs=Rs)

        I_input_temp_list.append(I_input)


    I_total_list.append(I_input_temp_list)
    plt.plot(V_in_list, I_input_temp_list, label=f"Rs: {Rs}")


plt.xlabel('Voltage')
plt.ylabel('Current')
plt.legend()
plt.show()


testPoint = 0
