#creates the tables for the two elements: pure silicon oxide and germanium Oxide
import os
import sys
from pathlib import Path
sys.path.insert(0,os.fspath(Path(__file__).parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from tools.dirtyDerivative import dirtyDerivative

#equation definition for index of refraction
def getIndex(A_list: list,
             lamb_list: list,
             lamb: float):

    val_0 = 1.0
    val_1 = (A_list[0]*(lamb**2))/(lamb**2 - lamb_list[0]**2)
    val_2 = (A_list[1]*(lamb**2))/(lamb**2 - lamb_list[1]**2)
    val_3 = (A_list[2]*(lamb**2))/(lamb**2 - lamb_list[2]**2)

    #gets the total value
    n = np.sqrt(val_0 + val_1 + val_2 + val_3)


    return n

Si_A = [0.696749, 0.408218, 0.890815]
Ge_A = [0.711040, 0.451885, 0.704048]

Si_lambda = [0.0690660e-6, 0.115662e-6, 9.900559e-6]
Ge_lambda = [0.0642700e-6, 0.129408e-6, 9.425478e-6]

numSamples = 1000
lamb_min = 0.5e-6
lamb_max = 1.8e-6

spacing = (lamb_max - lamb_min) / numSamples

#gets the linspace for lambda
lamb_list = np.linspace(start=lamb_min, stop=lamb_max, num=numSamples)
lamb_list = lamb_list.tolist()

#creates the instance of the dirty dirtyDerivative
diff_Si = dirtyDerivative(spacing=spacing)
diff_Ge = dirtyDerivative(spacing=spacing)

Si_indices = []
Ge_indices = []

Si_indices_diff = []
Ge_indices_diff = []

Ng_Si_list = []
Ng_Ge_list = []

prev_Si_index = 0.0
prev_Ge_index = 0.0

prev_lamb = 0.0

zero_lamb_Si = 0.0
zero_lamb_Ge = 0.0

for lamb in lamb_list:
    Si_index = getIndex(A_list=Si_A, lamb_list=Si_lambda, lamb=lamb)
    Ge_index = getIndex(A_list=Ge_A, lamb_list=Ge_lambda, lamb=lamb)

    Si_indices.append(Si_index)
    Ge_indices.append(Ge_index)


    Si_index_diff = (Si_index - prev_Si_index)/(lamb - prev_lamb)
    Ge_index_diff = (Ge_index - prev_Ge_index)/(lamb - prev_lamb)

    if abs(Si_index_diff) < 0.0001:
        zero_lamb_Si = lamb

    if abs(Ge_index_diff) < 0.0001:
        zero_lamb_Ge = lamb

    Si_indices_diff.append(Si_index_diff)
    Ge_indices_diff.append(Ge_index_diff)
    

    Ng_Si = Si_index - lamb*Si_index_diff
    Ng_Ge = Ge_index - lamb*Ge_index_diff
    
    Ng_Si_list.append(Ng_Si)
    Ng_Ge_list.append(Ng_Ge)


    prev_Si_index = Si_index
    prev_Ge_index = Ge_index
    prev_lamb = lamb

#gets rid of the starting condition problem
Ng_Si_list[0] = Ng_Si_list[1]
Ng_Ge_list[0] = Ng_Ge_list[1]

plt.figure(0)
plt.plot(lamb_list, Si_indices, label='Si Index')
plt.plot(lamb_list, Ng_Si_list, label='Si Ng')
plt.title("Pure Silicon")
plt.legend()
plt.show()


plt.figure(1)
plt.plot(lamb_list, Ge_indices, label='Ge Index')
plt.plot(lamb_list, Ng_Ge_list, label='Ge Ng')
plt.title("Silicon with Germanium doping")
plt.legend()
plt.show()


testPoint = 0
