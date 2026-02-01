import numpy as np
import matplotlib.pyplot as plt

thickness = 20e-6

n1 = 3.0
n2 = 1.50

#gets the velocity through each material
c = 3e8
v1 = c/n1
v2 = c/n2


#create the table
wavelengths = [15e-6, 20e-6, 25e-6, 30e-6, 40e-6, 45e-6, 50e-6, 70e-6, 100e-6, 150e-6, 200e-6]
theta_0_deg = [77.8, 74.52, 71.5, 68.7, 63.9, 61.7, 59.74, 53.2, 46.4, 39.9, 36.45]
theta_1_deg = [65.2, 58.15, 51.6, 45.5, 35.5, 32.02, 30.17]

num_theta_1 = len(theta_1_deg)
wavelengths_section = wavelengths[0:num_theta_1]

theta_0 = np.radians(theta_0_deg)
theta_1 = np.radians(theta_1_deg)

omegas_list = []
beta_0_list = []
beta_1_list = []

for i in range(len(theta_0)):
    #gets the current wavelength
    currentWavelength = wavelengths[i]
    omega_temp = 2*np.pi*v1/currentWavelength
    omegas_list.append(omega_temp)

    theta_0_temp = theta_0[i]

    beta_0_temp = ((2*np.pi*n1)/currentWavelength)*np.sin(theta_0_temp)
    beta_0_list.append(beta_0_temp)

omegas_section = omegas_list[0:num_theta_1]

for i in range(len(theta_1)):

    currentWavelength = wavelengths_section[i]
    theta_1_temp = theta_1[i]
    beta_1_temp = ((2*np.pi*n1)/currentWavelength)*np.sin(theta_1_temp)
    beta_1_list.append(beta_1_temp)



#creates the two plots for the comparison
tempLine1 = []
tempLine2 = []
for omega in omegas_list:
    line1 = omega/v1
    line2 = omega/v2
    tempLine1.append(line1)
    tempLine2.append(line2)

    
plt.figure(0)
plt.plot(omegas_list, beta_0_list, label='TE0')
plt.plot(omegas_section, beta_1_list, label='TE 1')
plt.plot(omegas_list, tempLine1, label='c/n1')
plt.plot(omegas_list, tempLine2, label='c/n2')
plt.xlabel('omega')
plt.ylabel('beta')
plt.legend()
plt.title("beta 1 plot")
plt.show()
    
testPoint = 0

#pg 101
#pg 170
