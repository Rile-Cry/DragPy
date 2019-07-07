# Module Title: Physics
# Created By: Rile_Cry
# Created On: 29 June 2019
# Description: This module houses all of the specifics regarding how the
# physics is handled for the DragPy simulation

# Imports

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
    def __init__(self, dim: float=3, g: float=-9.8066) -> None:
        # Define the acceleration at some surface
        if dim == 1:
            self.g = Vect(g)
        else:
            self.g = Vect().fill(dim)
            self.g[1] = g

        self.bodies = []

# Test condition

if __name__ == '__main__':
    engine = Physics()
    print(engine.g)