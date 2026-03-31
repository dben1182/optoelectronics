import numpy as np
import scipy.constants as scp

lamb = 632.8e-9

# sets the temperature in celsius
Temp_celsius = 130
Temp = Temp_celsius + 273.15

# sets the length
length = 40e-2

# sets the mass of the helium neon laser
mass_molecule = 3.35e-26

# gets the v_x velocity
V_x = np.sqrt(scp.Boltzmann * Temp / mass_molecule)


# gets the central frequency
nu_0 = scp.c / lamb


# gets nu_1 and nu_2
nu_1 = nu_0 * (1 + V_x / scp.c)
nu_2 = nu_0 * (1 - V_x / scp.c)

# gets the lambda1 and lambda2
lamb_1 = scp.c / nu_1
lamb_2 = scp.c / nu_2

delta_lamb = lamb_2 - lamb_1

testPoint = 0

#gets the central mode
m_0 = 2*length/(lamb)

delta_lamb_m = (lamb**2)/(2*length)

delta_nu_m = scp.c/(2*length)

intList = list(range(-5, 5))

modeLambList = []
modeNumList = []

for tempInt in intList:

    #gets the calculated wavelength of the particular mode
    lamb_calculated = lamb + tempInt*delta_lamb_m

    #adds it to the list if it is between the two allowable wavelengths
    if lamb_calculated >= lamb_1 and lamb_calculated <= lamb_2:
        modeLambList.append(lamb_calculated)
        modeNum = 2*length/lamb_calculated
        modeNumList.append(modeNum)


#part d

#sets the expansion coefficient alpha
alpha = 1e-6

#sets the start temperature
TempStart_C = 20
TempStart = TempStart_C + 273.15
TempEnd_C = 130
TempEnd = TempEnd_C + 273.15


testPoint = 0
