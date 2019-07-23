# Program Title: Dragpy
# Created By: Rile_Cry
# Created On: 24 June 2019
# Current Version: 1.1.0
# Description: Dragpy is a aerodynamic entry simulation program originally
# built for L'Space Academy Level 1 2019 for atmospheric entry of Titan.

# Imports

import glob
import matplotlib.pyplot as plt
import numpy as np
from physics import Physics
from report import Report

# Functions

def breakup(string: str) -> list:
    # Initialize the list variable
    lst = []

    # Run through the string and grab any that are before commas
    word = ''
    for i, let in enumerate(string):
        if i == len(string):
            lst.append(word)
        elif let == ',':
            lst.append(word)
            word = ''
        else:
            word += let

    # Return the list
    return lst

# Main Function

def main() -> None:
    # Generate list of atmospheric templates
    cel_list = glob.glob('./atmospheres/*.json')
    for i, loc in enumerate(cel_list):
        cel_list[i] = loc[len('./atmospheres/'):len(loc) - 5]
    cel_list.remove('template')

    # Ask which atmosphere the user would like to use.
    print('Please pick an atmosphere to use in this simulation\n')
    for item in cel_list:
        print(item)
    atmos = input('\nAtmosphere: ')

    # Generate the engine
    while True:
        try:
            dim = int(input('\nDimensions: '))
            break
        except:
            print('Value is not an integer, try again.\n')
    if dim == '':
        dim = 3
    engine = Physics(dim, atmos)

    # Generate the body to simulate
    while True:
        try:
            mass = float(input('\nMass of object (kg): '))
            pos = list(map(float,
                           breakup(input("\nPosition (1,2,3,...) (m): "))))
            pos = np.array(pos)
            vel = list(map(float,
                           breakup(input("\nVelocity (1,2,3,...) (m/s): "))))
            vel = np.array(vel)
            acc = list(map(float,
                           breakup(
                               input("\nAcceleration (1,2,...) (m/s^2): "))))
            acc = np.array(acc)
            Cd = input('\nCoefficient of drag (leave empty if none): ')
            if Cd != '':
                area = float(input('\nArea affected by drag (m^3): '))
                engine.addBody(mass, pos, vel, acc, float(Cd), area)
            else:
                engine.addBody(mass, pos, vel, acc)
            break
        except:
            print('Value was not a float.')

    # Run the simulation
    while True:
        try:
            dt = float(input('\ndt: '))
            time = float(input('\nTotal time for sim to run: '))
            break
        except:
            print('Value couldn\'t be converted to float, try again.')
    sim = engine.sim(dt, time)

    # Report
    while True:
        ans = input('\nWould you like to save the sim in a report (y, n): ')
        if ans == 'y':
            filename = input('\nName of file: ')
            rep = Report(filename, 'log')
            rep.setData(sim)
            rep.report()
            break
        elif ans == 'n':
            x_data = []
            y_data = []
            v_data = []
            a_data = []
            for n in sim:
                y_data.append(n[0]['pos'][1])
                v_data.append(n[0]['vel'][1])
                a_data.append(n[0]['acc'][1])
            print('\nEnd of simulation result:')
            print(sim[len(sim) - 1])
            x_data = np.linspace(0, time, len(sim))
            plt.plot(x_data, y_data)
            plt.axis([0, time, 0, max(y_data)])
            plt.xlabel('Time (s)')
            plt.ylabel('Altitude (m)')
            plt.show()
            break
        else:
            print('Answer was invalid, try again.\n')

# Run Condition

if __name__ == '__main__':
    main()
