import numpy as np
import scipy.constants as scp

eV_to_joules = 1.60218e-19

InGaAs_bandgap_eV = 0.70
InGaAs_bandgap = InGaAs_bandgap_eV*eV_to_joules

InGaAs_thickness = 10e-9

InAlAs_bandgap_eV = 1.45
InAlAs_bandgap = eV_to_joules*InAlAs_bandgap_eV

InGaAs_conductionElectrons_effective_mass = 0.04*scp.electron_mass
InGaAs_valenceHoles_effective_mass = 0.44*scp.electron_mass

n = [1,2]

n_prime = [1]


eps = [((scp.Planck**2)*(n_temp**2))/(8*(InGaAs_conductionElectrons_effective_mass)*(InGaAs_thickness**2)) for n_temp in n]

eps_prime = [((scp.Planck**2)*(n_prime_temp**2))/(8*InGaAs_valenceHoles_effective_mass*(InGaAs_thickness**2)) for n_prime_temp in n_prime]

eps_eV = [eps_temp/eV_to_joules for eps_temp in eps]

eps_prime_eV = [eps_prime_temp/eV_to_joules for eps_prime_temp in eps_prime]

wavelength_g = (scp.Planck*scp.c)/InGaAs_bandgap


wavelength_qw = (scp.Planck*scp.c)/(InGaAs_bandgap + eps[0] + eps_prime[0])


testPoint = 0