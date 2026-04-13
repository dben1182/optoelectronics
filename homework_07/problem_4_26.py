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


