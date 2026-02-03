import numpy as np

#saves the indices of refraction
n_list = [1.4634, 1.4587, 1.4567]
#and the lambdas
lamb_list = [486.1e-9, 589.2e-9, 656.3e-9]

seperation = 1.0

alpha = np.radians(60)
theta_i = np.radians(45)

delta_2_list = []
position_list = []

for n in n_list:

    theta_t = np.arcsin(np.sin(theta_i)/n)

    beta = np.radians(180) - alpha
    
    theta_i_prime = np.radians(180) - beta - theta_t

    theta_t_prime = np.arcsin(n*np.sin(theta_i_prime))

    delta_2 = theta_t_prime - theta_i_prime

    delta_2_list.append(delta_2)

    position = seperation*np.tan(delta_2)
    position_list.append(position)

difference_1 = position_list[1] - position_list[0]
difference_2 = position_list[2] - position_list[1]

testPoint = 0
