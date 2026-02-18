import numpy as np
import matplotlib.pyplot as plt


alpha_array = np.linspace(0,np.pi/2, num=100)
alpha_list = alpha_array.tolist()
alpha_deg_list = np.degrees(alpha_list)

a = 1.353
b = 0.7
c = 0.678

Intensity_list = []

for alpha in alpha_list:

    Intensity = a * (b)**((1.0/(np.sin(alpha)))**c)
    Intensity_list.append(Intensity)


plt.figure(0)
plt.plot(alpha_deg_list, Intensity_list)
plt.xlabel('Alpha (deg)')
plt.ylabel('Intensity (kW/m^2)')
plt.title("Intensity Plot")
plt.show()

#gets the max 
max_intensity = max(Intensity_list)
max_intensity_index = Intensity_list.index(max_intensity)
max_intensity_alpha_rad = alpha_list[max_intensity_index]
max_intensity_alpha_deg = alpha_deg_list[max_intensity_index]


Area = 1.0
Efficiency = 0.20
TotalPower = max_intensity*Area*Efficiency

testPoint = 0
