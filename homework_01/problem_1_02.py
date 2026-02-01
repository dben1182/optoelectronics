import numpy as np

lamb = 1.5e-6
linewidth = 2e-9
c = 3e8

secondDerivative = 400.0

D = (lamb*secondDerivative)/c


#gets the dispersion per unit length
dispersion = D*linewidth


testPoint = 0
