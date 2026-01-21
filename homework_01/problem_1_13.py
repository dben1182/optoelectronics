import numpy as np


sigma_deg = 60
sigma = np.radians(sigma_deg)
d = 1


#creates the list of indices of refraction and wavelengths
n_list = [1.4634, 1.4587, 1.4567]
lambda_list = [486.1, 589.2, 656.3]

#states the input alpha
alpha1_deg = 45
alpha1 = np.radians(alpha1_deg)

deflectionList = []
displacementList = []
deflectionList_deg = []


for n in n_list:

    beta1 = np.arcsin(np.sin(alpha1)/n)
    alpha2 = sigma - beta1
    beta2 = np.arcsin(n*np.sin(alpha2))

    delta = alpha1 + beta2 - sigma
    deflectionList.append(delta)
    deflectionList_deg.append(np.degrees(delta))

    #gets the downward angle
    downwardAngle = beta2 - (sigma/2)

    #gets the total downward position
    pos_d = d*np.tan(downwardAngle)

    displacementList.append(pos_d)

displacement_0 = displacementList[1] - displacementList[0]
displacement_1= displacementList[2] - displacementList[1]

testPoint = 0
