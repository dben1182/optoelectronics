import numpy as np
import scipy.constants as scp
import matplotlib.pyplot as plt


lamb_list = [565e-9, 583e-9, 600e-9, 635e-9]
lamb_halfWidth_list = [28e-9, 36e-9, 40e-9, 40e-9]
colors = ['green', 'yellow', 'orange', 'red']

m = 3.0
T = 300.0


lamb_halfwidth_calculated = [m*scp.Boltzmann*T/(scp.Planck*scp.c)*lamb**2 for lamb in lamb_list]

plt.figure()
plt.scatter(lamb_list, lamb_halfWidth_list, label='Actual')
plt.scatter(lamb_list, lamb_halfwidth_calculated, label='Calculated')
plt.legend()
plt.grid(True)
plt.show()
