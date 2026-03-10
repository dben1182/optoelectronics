import numpy as np
import matplotlib.pyplot as plt

#irradiance (in microwatts/cm^2)
#for M1, M2, M3, R, G, B
irradiance_microwatts_per_cm2 = [424.0, 564.0, 716.0, 785.0, 814.0, 1240.0]

#Photocurrent for diameter largest first: 
#in microamps
photocurrent_1 = [13.0, 20.2, 29.5, 9.2, 8.1, 11.3]
photocurrent_2 = [14.6, 23.0, 33.2, 9.1, 7.9, 11.3]
photocurrent_3 = [11.1, 18.5, 26.4, 6.0, 5.1, 7.6]

photocurrents_list = [photocurrent_1, photocurrent_2, photocurrent_3]

#sets the diameters in the same order in micrometers (microns)
outer_diameters = [361.8, 302.6, 152.17]

outer_diameters_strings = [str(diameter) + ' microns' for diameter in outer_diameters]

#areas in square 
areas_microns = [np.pi*(diameter/2.0)**2 for diameter in outer_diameters]

microns_per_cm = 1e4

areas_centimeters = [area/(microns_per_cm**2) for area in areas_microns]

#gets the input powers in microwatts
power_microwatts = []

for area in areas_centimeters:
    power_list =[]
    for irradiance in irradiance_microwatts_per_cm2:
        power_temp = irradiance*area
        power_list.append(power_temp)

    power_microwatts.append(power_list)

fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex=True)
ax_list = [ax1, ax2, ax3]

responsivities_list = []
for power_list_temp, current_list_temp, ax_temp, diameter_str in zip(power_microwatts, photocurrents_list, ax_list, outer_diameters_strings):

    ax_temp.scatter(power_list_temp, current_list_temp, color='orange', linewidth=3)
    ax_temp.plot(power_list_temp, current_list_temp, color='orange', linewidth=3)
    ax_temp.set_xlabel('Power (Microwatts)')
    ax_temp.set_ylabel('Current (Microamps)')
    ax_temp.set_title('Diameter: ' + diameter_str)

    tempList = []
    for power_temp, current_temp in zip(power_list_temp, current_list_temp):

        #gets the responsivity of each
        responsivity_temp = current_temp/power_temp
        tempList.append(responsivity_temp)
    responsivities_list.append(tempList)


plt.show()

testPoint = 0
