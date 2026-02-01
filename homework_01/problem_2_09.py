import numpy as np
import matplotlib.pyplot as plt

d = 10e-6
a = d/2.0
n1 = 1.4446
n2 = 1.4440


lamb1 = 1.0e-6
lamb2 = 1.5e-6

V1 = ((2*np.pi*a)/(lamb1))*(n1**2 - n2**2)**(0.5)
V1 = ((2*np.pi*a)/(lamb2))*(n1**2 - n2**2)**(0.5)

theta_m = np.linspace(0, np.pi*2, 1000)
theta_m_list = theta_m.tolist()
leftSide_list = []
rightSide_list = []
wholeSide_list = []

k1 = 2*np.pi*n1/lamb1
k2 = 2*np.pi*n1/lamb2

#gets the left half of hte equation
for theta_m in theta_m_list:

    tempLeftSide = np.tan(a*k2*np.cos(theta_m))
    tempRightside = np.sqrt((np.sin(theta_m)**2) - (n2/n1)**2)/np.cos(theta_m)

    leftSide_list.append(tempLeftSide)
    rightSide_list.append(tempRightside)
    wholeSide = tempLeftSide - tempRightside
    wholeSide_list.append(wholeSide)

    theta_m_deg = np.degrees(theta_m)

    if wholeSide > -1.0 and wholeSide < 1.0:
        potato = 0

    testPoint = 0

plt.figure(0)
plt.plot(theta_m_list, wholeSide_list)
plt.show()



testPoint = 0
