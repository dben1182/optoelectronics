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
nu_2 = nu_0 * (1 + V_x / scp.c)
nu_1 = nu_0 * (1 - V_x / scp.c)

# gets the lambda1 and lambda2
lamb_1 = scp.c / nu_1
lamb_2 = scp.c / nu_2

delta_lamb = lamb_2 - lamb_1

testPoint = 0
