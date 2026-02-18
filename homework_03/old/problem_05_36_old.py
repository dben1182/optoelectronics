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
#sets the sum solution (to zero)
currentSolutionSum = 0.0

V_list = []
I_list = []

plt.figure(0)

for Rs in Rs_list:
    
    #creates the current sum equation
    def currentEquation(V):
        sum = V/Rs - Iph + I0*(np.exp((spc.elementary_charge*V)/(eta*spc.Boltzmann*T)) - 1.0)
        return sum


    #gets the V for the solution
    V_solution = fsolve(currentEquation, currentSolutionSum)[0]


    V_list.append(V_solution)

    if V_solution == 0.0:
        I_output = Iph

    else:
        I_output = V_solution/Rs
    I_list.append(I_output)

    plt.scatter(V_solution, I_output, label=f"Rs: {Rs}")

plt.legend()
plt.show()

testPoint = 0
    
    
