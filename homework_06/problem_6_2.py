import numpy as np
import scipy.constants as scp

eV_to_joules = 1.60218e-19


critical_population = 9e21
lifetime = 300e-6
laseLevel_eV = 1.4
laseLevel = laseLevel_eV*eV_to_joules

PowerThreshold = (critical_population*laseLevel)/(2*lifetime)

testPoint = 0
