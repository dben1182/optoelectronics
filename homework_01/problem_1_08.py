import os
import sys
from pathlib import Path
sys.path.insert(0,os.fspath(Path(__file__).parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from tools.dirtyDerivative import dirtyDerivative


c = 3e8

#defines the function to find the index of refraction based on wavelength
def getIndex(sellmeierCoefficients: list[list[float]],
             wavelength: float):

    A1 = sellmeierCoefficients[0][0]
    A2 = sellmeierCoefficients[0][1]
    A3 = sellmeierCoefficients[0][2]

    lamb_1 = sellmeierCoefficients[1][0]
    lamb_2 = sellmeierCoefficients[1][1]
    lamb_3 = sellmeierCoefficients[1][2]


    #gets n squared
    n_squared = 1 + (A1*(wavelength**2))/(wavelength**2 - lamb_1**2) +\
                    (A2*(wavelength**2))/(wavelength**2 - lamb_2**2) +\
                    (A3*(wavelength**2))/(wavelength**2 - lamb_3**2)

    refractive_index = np.sqrt(n_squared)

    return refractive_index




def main(numSamples: int = 1000):
    


    minWavelength = 0.5e-6
    maxWavelength = 1.8e-6

    delta_wavelength = maxWavelength - minWavelength
    wavelength_increment = delta_wavelength / numSamples

    #creates the table for the sellmeier coefficients
    Sellmeier_SiO2 = [[0.696749, 0.408218, 0.890815],
                      [0.0690660, 0.115662, 9.900559]]

    Sellmeier_SiO2_GeO2 = [[0.711040, 0.451885, 0.704048],
                           [0.0642700, 0.129408, 9.425478]]

    #creates the linspace between the min and max wavelengths
    wavelengths = np.linspace(start=minWavelength, stop=maxWavelength, num=numSamples).tolist()

    SiO2_indices = []
    SiO2_GeO2_indices = []

    #creates the indices of refraction for 
    
    for i in range(numSamples):
        tempWavelength = wavelengths[i]

        #gets the coefficient for pure silica
        n_SiO2_temp = getIndex(sellmeierCoefficients=Sellmeier_SiO2,
                               wavelength=tempWavelength)

        #gets it for doped SiO2
        n_SiO2_GeO2_temp = getIndex(sellmeierCoefficients=Sellmeier_SiO2_GeO2,
                                    wavelength=tempWavelength)

        SiO2_indices.append(n_SiO2_temp)
        SiO2_GeO2_indices.append(n_SiO2_GeO2_temp)

        testPoint = 0



    diff_pure = dirtyDerivative(spacing=wavelength_increment)
    diff_doped = dirtyDerivative(spacing=wavelength_increment)
    diff_second_pure = dirtyDerivative(spacing=wavelength_increment)

    SiO2_indices_diff = []
    SiO2_GeO2_indices_diff = []
    SiO2_indices_diff_second = []

    SiO2_group_indices = []
    SiO2_GeO2_group_indices = []

    SiO2_group_velocities = []
    SiO2_GeO2_group_velocities = []

    desiredSecondDiff = 0.0

    #creates the derivatives of each sample for both materials
    for pure_index, doped_index, wavelength in zip(SiO2_indices, SiO2_GeO2_indices, wavelengths):
        n_SiO2_diff_temp = diff_pure.update(z=pure_index)
        n_SiO2_diff_second_temp = diff_second_pure.update(n_SiO2_diff_temp)
        n_SiO2_GeO2_diff_temp = diff_doped.update(z=doped_index)

        if wavelength >= 1.5e-6:

            testPoint = 0

        SiO2_indices_diff.append(n_SiO2_diff_temp)
        SiO2_GeO2_indices_diff.append(n_SiO2_GeO2_diff_temp)
        SiO2_indices_diff_second.append(n_SiO2_diff_second_temp)

        SiO2_group_index = pure_index - wavelength*n_SiO2_diff_temp
        SiO2_GeO2_group_index = doped_index - wavelength*n_SiO2_GeO2_diff_temp

        SiO2_group_indices.append(SiO2_group_index)
        SiO2_GeO2_group_indices.append(SiO2_GeO2_group_index)

        SiO2_group_velocity = c / SiO2_group_index
        SiO2_GeO2_group_velocity = c / SiO2_GeO2_group_index

        SiO2_group_velocities.append(SiO2_group_velocity)
        SiO2_GeO2_group_velocities.append(SiO2_GeO2_group_velocity)

        if wavelength > 1.0e-6:

            testPoint = 0
    
    diff_pure_group_vel = dirtyDerivative(spacing=wavelength_increment)
    diff_doped_group_vel = dirtyDerivative(spacing=wavelength_increment)

    pure_group_vel_diff_list = []
    doped_group_vel_diff_list = []

    for pure_vel, doped_vel in zip(SiO2_group_velocities, SiO2_GeO2_group_velocities):
        
        pure_group_vel_diff = diff_pure_group_vel.update(z=pure_vel)
        doped_group_vel_diff = diff_doped_group_vel.update(z=doped_vel)

        pure_group_vel_diff_list.append(pure_group_vel_diff)
        doped_group_vel_diff_list.append(doped_group_vel_diff)

    
        
    plt.figure(0)
    plt.plot(wavelengths, SiO2_indices, label='n Pure Silica')
    plt.plot(wavelengths, SiO2_GeO2_indices, label='n Silica Germanium')
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('index of refraction')
    plt.title("Index of Refraction")
    plt.legend()
    plt.show()

    plt.figure(1)
    plt.plot(SiO2_group_indices, label='Pure Silica')
    plt.plot(SiO2_GeO2_group_indices, label='Silica Germanium')
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('group index')
    plt.title('Group Index')
    plt.legend()
    plt.show()


    plt.figure(2)
    plt.plot(SiO2_group_velocities, label='silica group velocity')
    plt.plot(SiO2_GeO2_group_velocities, label = 'doped silica group velocity')
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('group velocity')
    plt.title('Group Velocity')
    plt.legend()
    plt.show()


    plt.figure(3)
    plt.plot(pure_group_vel_diff_list, label='silica group velocity derivatives')
    plt.plot(doped_group_vel_diff_list, label = 'doped group velocity derivatives')
    plt.xlabel('Wavelength (microns)')
    plt.ylabel('group velocity diff')
    plt.title('Group Velocity diff')
    plt.legend()
    plt.show()


    testPoint = 0




if __name__ == '__main__':

    main()
