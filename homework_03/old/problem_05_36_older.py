import numpy as np

#creates the Resistances 
Rs_list = [0, 40, 90]
Iph = 9e-3
I0 = 30e-6
Rp = np.inf


V_array = np.linspace(0.0, 0.5, num=1000)

for Rs in Rs_list:


