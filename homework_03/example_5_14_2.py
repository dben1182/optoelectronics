import numpy as np
import scipy.constants as sp_c


T = 300


#500 watts per meter squared
illumination = 500
I_sc = 16e-3
V_oc = 0.5
eta = 1.0

#gets the second intensity Which is just double the original intensity
I_ph2 = I_sc*2.0

#creates the ould be measured, for example, using a capacitance bridge in thelaboratory) for various materials. It then compares 3er(LF)4 1>2 with n.For silicon and diamond there is an excellent agreement between 3er(LF)4 1>2 and n. Bothare covalent solids in which electronic polarization (electronic bond polarization) is the onlypolarization mechanism at low and high frequencies. Electronic polarization involves the dis-placement of light electrons with respect to positive ions of the crystal. This process can readilyrespond to the field oscillations up to optical or even ultraviolet frequencies.For GaAs and SiO2 3 er(L



#gets the open circuit voltage
Voc = (eta*sp_c.Boltzmann*sp_c*T/sp_c.elementary_charge)*np.log(I_)


testPoint = 0
