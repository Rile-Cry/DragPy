# Module Title: Physics
# Created By: Rile_Cry
# Created On: 29 June 2019
# Description: This module houses all of the specifics regarding how the
# physics is handled for the DragPy simulation

# Imports

from drag import Drag
from typing import Union
from vect import Vect

# Main Class

class Physics:
    '''
    Class: Physics
    Params:
        None
    Functions:
        None
    '''

    # Engine setup
    def __init__(self, dim: float=3, filename: str='earth') -> None:
        # Define the acceleration at some surface
        self.model = Drag(filename)
        self.bodies = []
        g = self.model.data['surface_g']
        if dim == 1:
            self.g = Vect(-g)
        else:
            self.g = Vect().fill(dim)
            self.g[1] = -g

    # Utility Functions
    def addBody(self, body: dict) -> None:
        '''
        Function: addBody
        Params:
            body: [dict] The body to be added to the engine
        Description:
            addBody adds a body to the engine, typically should hold the keys
                (mass, pos: [vect], vel: [vect], acc: [vect], area, Cd)
        '''
        # Adds the body to the list of bodies in the system
        if type(self.bodies) == list:
            self.bodies.append(body)
            print(self.bodies)

    def grabBodies(self) -> None:
        return self.bodies

    def update_pos(self, dt: float) -> None:
        '''
        Function: update_pos
        Params:
            dt: [float] The change in time
        Description:
            update_pos updates the position of all bodies in the system
        '''
        # Iterate through all the bodies to update their positions
        for i, body in enumerate(self.bodies):
            if 'pos' in body:
                del_acc = 0.5 * body['acc'] * pow(dt, 2)
                body['pos'] = body['pos'] + body['vel'] * dt + del_acc
            self.bodies[i] = body

    def update_vel(self, dt: float) -> None:
        '''
        Function: update_vel
        Params:
            dt: [float] The change in time
        Description:
            update_vel updates the velocity of all bodies in the system
        '''
        # Iterate through all the bodies to update their velocity
        for i, body in enumerate(self.bodies):
            if 'vel' in body:
                body['vel'] = body['vel'] + body['acc'] * dt
            self.bodies[i] = body

    def update_acc(self) -> None:
        '''
        Function: update_acc
        Params:
            dt: [float] The change in time
        Description:
            update_acc updates the acceleration of all bodies in the system
        '''
        # Iterate through all the bodies to update their acceleration
        for i, body in enumerate(self.bodies):
            # Ensure that the body has drag properties
            if 'acc' in body:
                if 'Cd' in body and 'area' in body and 'mass' in body:
                    # To keep things under 80, set variables
                    mass = body['mass']
                    if len(body['pos']) == 1:
                        height = body['pos'][0]
                    else:
                        height = body['pos'][1]
                    Cd = body['Cd']
                    area = body['area']

                    # Calculate the vectoral drag
                    for i2, val in enumerate(body['vel']):
                        acc_drag = self.model.drag(mass, height, val, Cd, area)
                        body['acc'][i2] = self.g[i2] + acc_drag
                else:
                    body['acc'] = self.g
            self.bodies[i] = body

    def update(self, dt: float, result: bool=False) -> Union[None, list]:
        '''
        Function: update
        Params:
            dt: [float] The change in time
            result: [bool] If update returns anything or not
        Description:
            update updates the position, velocity, and acceleration of all
                bodies in a system over a period of dt.
        '''
        # update pos, vel, and acc
        self.update_pos(dt)
        self.update_vel(dt)
        self.update_acc()

        if result:
            print(self.bodies)
            return self.bodies

    def sim(self, dt: float, time: float) -> list:
        '''
        Function: sim
        Params:
            dt: [float] The change in time
            time: [float] Total runtime
        Description:
            sim runs through a loop of updates for time in dt increments
        '''
        # Variable for storing results
        result = []

        # While loop for simulation
        t = 0
        while t < time:
            result.append(self.update(dt, True))
            t += dt

        # Return the results
        return result

# Test condition

if __name__ == '__main__':
    engine = Physics()
    print(engine.g)
    a = {'mass': 400, 'pos': Vect(0., 10000., 0.), 'vel': Vect(0., 0., 0.),
         'acc': Vect(0., 0., 0.), 'Cd': 0.75, 'area': 8}
    engine.addBody(a)
    sim_res = engine.sim(0.1, 100)