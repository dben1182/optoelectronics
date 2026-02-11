import numpy as np
import matplotlib.pyplot as plt

#creats the bandgap table
bandgap_list = [5.0, 1.1, 0.66]
index_list = [2.4, 3.46, 4.0]



#gets index list to the fourth power
index_list_4 = [n**4 for n in index_list]
Reciprocal_List = [1/Eg for Eg in bandgap_list]


#gets the value of k
K_list = [(n**4)*(Eg) for n, Eg in zip(index_list, bandgap_list)]

K_ave = np.mean(K_list)

testPoint = 0

plt.figure(0)
plt.plot(bandgap_list, index_list, label='Index of Refraction')
plt.xlabel("Bandgap (eV)")
plt.title("Index of Refraction given Bandgap")
plt.legend()
plt.show()



plt.figure(1)
plt.plot(Reciprocal_List, index_list_4, label="quartic")
plt.xlabel("Bandgap reciprocal")
plt.ylabel("n^4")
plt.legend()
plt.show()



