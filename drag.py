# Module Title: Drag
# Created By: Rile_Cry
# Created On: 28 June 2019
# Description: This module was created to come up with an
# atmospheric model and to calculate drag based on that model

# Imports

from math import exp
import json

# Main Class

class Drag:
    '''
    Class: Drag
    Params:
        filename: [str] The name of the file used for the atmospheric model
    Functions:
        density_one: Takes in the current height and lapse_rate index to
            calculate the current density at a height, lapse rate != 0
        density_two: Takes in the current height and lapse_rate index to
            calculate the current density at a height, lapse rate == 0
    '''

    # Constants

    R = 8.3144598 # N*m/(mol*K)

    # Class Setup

    def __init__(self, filename: str) -> None:
        # Use filename to grab atmospheric data
        self.data = {}
        with open('atmospheres/' + filename + '.json', 'r') as file:
            self.data = json.load(file)

        # Inner function for calculating scale temperature
        def __temp(height: float, H: float, lapse_rate: float,
                   temp_b: float) -> float:
            # Use the equation temp = temp_b + lapse_rate * (height - H)
            return temp_b + lapse_rate * (height - H)

        # Inner functions for calculating scale density
        def __rho_one(height: float, H: float, lapse_rate: float,
                  temp_b: float, g: float, M: float,
                  rho: float, R: float) -> float:
            # Use the same equation located in density_one
            expt = 1 + ((g * M)/(R * lapse_rate))
            mult = (temp_b / (temp_b + lapse_rate * (height - H)))
            return rho * pow(mult, expt)

        def __rho_two(height: float, H: float, temp_b: float, g: float,
                      M: float, rho: float, R: float) -> float:
            # Use the same equation located in density_two
            expt = (-g * M * (height - H)) / (R * temp_b)
            return rho * exp(expt)

        # Create a tempurature and density scale with height
        H = 0
        M = self.data['molar_mass']
        g = self.data['surface_g']
        R = self.R
        rho = self.data['surface_density']
        T = self.data['surface_temp']
        self.data['scale_temp'] = []
        self.data['scale_rho'] = []
        for i,item in enumerate(self.data['lapse_rate']):
            if item[0] == 0:
                rho = __rho_two(item[1], H, T, g, M, rho, R)
            else:
                rho = __rho_one(item[1], H, item[0], T, g, M, rho, R)
            T = __temp(item[1], H, item[0], T)
            H = item[1]
            self.data['scale_temp'].append((T, H))
            self.data['scale_rho'].append((rho, H))

    # Modelling Functions

    def density_one(self, key: int, height: float) -> float:
        '''
        Function: density_one
        Params:
            key: [int] The index for lapse_rate, scale_temp, and H
            height: [float] The current height of an object in meters
            rho: [float] The current density of the atmosphere
        Description:
            density_one takes in a key and height and calculates the density
            at that height using rho * [temp_b / (temp_b +
            lapse_rate_b * (height - H))] ^ (1 + ((surface_g * molar_mass))/
            (R * lapse_rate_b))
        '''

        # Grab constants
        Lb = self.data['lapse_rate'][key][0]
        Tb = self.data['scale_temp'][key][0]
        H = self.data['lapse_rate'][key][1]
        rho = self.data['scale_rho'][key][0]

        # Calculate the exponent 
        expt_top = self.data['surface_g'] * self.data['molar_mass']
        expt = 1 + (expt_top / (self.R * Lb))

        # Calculate the density multiple
        rho_mult = pow((Tb/(Tb + Lb * (height - H))), expt)

        # Return the new density
        return rho_mult * rho

    def density_two(self, key: int, height: float) -> float:
        '''
        Function: density_two
        Params:
            key: [int] The index for scale_temp, and H
            height: [float] The current height of an object in meters
            rho: [float] The current density of the atmosphere
        Description:
            density_two takes in a key and height, then calculates the density
            at that height using rho *
        '''

        # Grab constants
        Tb = self.data['scale_temp'][key][0]
        H = self.data['scale_temp'][key][1]
        rho = self.data['scale_rho'][key][0]

        # Calculate the exponent
        expt_top = -self.data['surface_g']*self.data['molar_mass']*(height - H)
        expt = expt_top / (self.R * Tb)

        # Return the new density
        return rho * exp(expt)

    def drag(self, mass: float, height: float, vel: float, Cd: float,
             area: float) -> float:
        '''
        Function: drag
        Params:
            mass: [float] The mass of an object
            height: [float] The current y position of an object
            vel: [float] The current velocity of 1-D of an object
            Cd: [float] The coefficient of drag of an object
            area: [float] The surface area being pelted with atmosphere
        Description:
            drag takes in details concerning an object and calculates the
            acceleration due to drag on that object.
        '''

        # Calculate the density of atmosphere at that location
        rho = 0.
        for key, item in enumerate(self.data['scale_rho']):
            if height < item[0]:
                continue
            else:
                if self.data['lapse_rate'][key][0] == 0:
                    rho = self.density_two(key, height)
                else:
                    rho = self.density_one(key, height)

        # Calculate the force of drag
        Fd = (rho * Cd * area * pow(vel, 2)) / 2

        # Return the acceleration due to drag
        return Fd / mass

# Test

if __name__ == '__main__':
    atmo = Drag('earth')
    print(atmo.data['scale_rho'])
    print(atmo.drag(400, 35000, 100, 0.75, 8))