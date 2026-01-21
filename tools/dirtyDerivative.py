import numpy as np


class dirtyDerivative:

    def __init__(self,
                 spacing: float,
                 sigma: float = 0.05,
                 z_prev_init: float = 0.0,
                 z_dot_init: float = 0.0):
        #spacing is the equivalent of time sample spacing, which means
        #if the samples are seperated by time, it  is the time between samples.
        #if the samples are a function of something else, it is the spacing
        #between that something else. Like physical spacing between samples
        self.spacing = spacing 
        self.sigma = sigma
        self.z_prev = z_prev_init
        self.z_dot = z_dot_init

    def update(self,
               z: float):

        self.z_dot = ((2.0*self.sigma - self.spacing) / (2.0*self.sigma + self.spacing))*self.z_dot \
            + (2.0 / (2.0*self.sigma + self.spacing)) * (z - self.z_prev)
        #saves the current z to be the previous 
        self.z_prev = z


        return self.z_dot
