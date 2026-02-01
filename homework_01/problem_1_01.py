import numpy as np

delta = 0.01
n1 = 1.5
lamb = 1e-6
V = 2.405

#for second case
n2 = n1*(1-delta) 

#first case section
na1 = np.sqrt(n1**2 - 1.0**2)

a1 = V*lamb/(2*np.pi*na1)
d1 = 2*a1

#secnd case section
na2 = np.sqrt(n1**2 - n2**2)

a2 = V*lamb/(2*np.pi*na2)
d2 = 2*a2

testPoint = 0
