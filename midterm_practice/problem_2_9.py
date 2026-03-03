import numpy as np

n1 = 1.4446
n2 = 1.4440


#creates a linspace of theta
theta = np.linspace(0.0, np.pi/2.0, 100)
theta_list = theta.tolist()

interior_list = []
phi_list = []

for theta_temp in theta_list:
    interior = (np.sin(theta_temp))**2 - (n2/n1)**2
    numerator = ((np.sin(theta_temp))**2 - (n2/n1)**2)**(1/2)
    denominator = np.cos(theta_temp)

    right_side = numerator / denominator
    interior_list.append(interior)

    phi_temp = 2.0*np.arctan(right_side)
    phi_list.append(phi_temp)




testPoint = 0
