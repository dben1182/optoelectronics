import numpy as np
import matplotlib.pyplot as plt


#sets the photosensistive area in (mm^2)
ps_area_mm2 = 0.125
#converts to cm^2
ps_area_cm2 = ps_area_mm2 * (1/10.0) * (1/10.0)


#sets the electron charge In Coulomb
q_e = 1.60218e-19
#set's plank's constant
h = 6.6261e-34
#and the speed of light
c = 2.99e8


#creates the list of lambdas and intensities
lamb_list = [450e-9, 700e-9, 1000e-9]
#in watts per cm2
intensity_list = [1.0e-6, 1.0e-6, 1.0e-6]
#
#gets the responsivity of A at each of these in Amps per Watt
responsivity_A = [0.19, 0.45, 0.15]
#same for B
responsivity_B = [0.125, 0.45, 0.38]


#calculates the photocurrent for each device
powerIncident = [ps_area_cm2*intensity for intensity in intensity_list]

photocurrent_a = [power*resp for power, resp in zip(powerIncident, responsivity_A)]
photocurrent_b = [power*resp for power, resp in zip(powerIncident, responsivity_B)]

#gets the list of quantum efficiencies for A, and then B
quant_efficiencies_a = [(resp*h*c)/(q_e*lamb) for resp, lamb in zip(responsivity_A, lamb_list)]
quant_efficiencies_b = [(resp*h*c)/(q_e*lamb) for resp, lamb in zip(responsivity_B, lamb_list)]

#Photocurrent
plt.figure(0)
plt.plot(lamb_list, photocurrent_a, label='A')
plt.plot(lamb_list, photocurrent_b, label='B')
plt.xlabel('lambda (meters)')
plt.ylabel("current (Amps)")
plt.legend()
plt.title("Photocurrent")
plt.show()

plt.figure(1)
plt.plot(lamb_list, quant_efficiencies_a, label='A')
plt.plot(lamb_list, quant_efficiencies_b, label='B')
plt.xlabel('lambda (meters)')
plt.ylabel("efficiency")
plt.legend()
plt.title("Quantum Efficiency")
plt.show()

testPoint = 0
