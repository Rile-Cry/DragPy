# Module Title: Vect
# Created By: Rile_Cry
# Created On: 29 June 2019
# Description: This module handles all vector related matters

# Imports

from math import ceil, floor # For ceil and floor the vectors
from math import acos, sqrt # For angle differences and magnitude respectively
from typing import Union # For hinting multiple types

# Main Class

class Vect:
    '''
    Class: Vect
    Params:
        *args: [float, int] Values to be made into a vector
    Functions:
        append:
        add: Adds vectors or numbers to a vector
        sub: Subtracts vectors or numbers from a vector
        mult: Multiplies numbers with a vector
        div: Divides vectors by a number
        dot: Results in the dot product between two vectors
        cross: Results in the cross product between two vectors (3D only)
        angle: The angle between some vector and 'origin' vector
        angle_between: The angle between two vectors
        zeros: A vector of zeros
        ones: A vector of ones
    '''

    # Vector setup

    def __init__(self, *args: Union[int, float]) -> None:
        # Goes through the arguments and ensures that they are either
        # float or int.
        self.vector = []
        for arg in args:
            if type(arg) in [float, int]:
                self.vector.append(arg)
            else:
                raise(Exception('Value is not int or float.'))

    # Magic Methods for Vector Operations

    # Makes the vector iterable
    def __iter__(self) -> 'Vect':
        return self.vector

    # Allows of len on the vector
    def __len__(self) -> int:
        return len(self.vector)

    # Allows indexing of the vector
    def __getitem__(self, key: int) -> Union[float,  int]:
        return self.vector[key]

    # Allows to set the value at certain indexes
    def __setitem__(self, key: int, value: Union[float, int]) -> None:
        if type(value) in [float, int]:
            self.vector[key] = value
        else:
            raise(Exception('Value is not int or float.'))

    # Allows returning of the vector
    def __repr__(self) -> list:
        return self.vector

    # Allows returning of string for print
    def __str__(self) -> str:
        return str(self.vector)

    # Returns the magnitude of the vector
    def __abs__(self) -> float:
        # A variable to hold the total of a square
        square = 0

        # Adds the square of each part of the vector to the square variable
        for val in self.vector:
            square += pow(val, 2)

        # Returns the square root of the square variable
        return sqrt(square)

    # Checks if two vectors are equal
    def __eq__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return self.vector == other
        else:
            raise(Exception('Other is not a vector'))

    # Checks if two vectors are not equal
    def __ne__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return self.vector != other
        else:
            raise(Exception('Other is not a vector'))

    # Checks if the vector is smaller than another
    def __lt__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return abs(self) < abs(other)
        else:
            raise(Exception('Other is not a vector'))

    # Checks if the vector is smaller than or equal to another
    def __le__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return abs(self) <= abs(other)
        else:
            raise(Exception('Other is not a vector'))

    # Checks if the vector is larger than another
    def __gt__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return abs(self) > abs(other)
        else:
            raise(Exception('Other is not a vector'))

    # Checks if the vector is larger than or equal to another
    def __ge__(self, other: 'Vect') -> bool:
        if type(other) == type(Vect()):
            return abs(self) >= abs(other)
        else:
            raise(Excpetion('Other is not a vector'))

    # Reverses the vector for a -Vector
    def __neg__(self) -> 'Vect':
        # Creates a new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector and negates them
        for val in self.vector:
            new_v.append(-val)

        # Return the new vector
        return new_v
    
    # Allows for rounding of the vector
    def __round__(self, dig: int) -> 'Vect':
        # Creates a new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector and rounds the values
        for val in self.vector:
            new_v.append(round(val, dig))

        # Return the new vector
        return new_v

    # Allows for ceiling operation
    def __ceil__(self) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector and ceil the values
        for val in self.vector:
            new_v.append(ceil(val))

        # Return the new vector
        return new_v

    # Allows for floor operation
    def __floor__(self) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector and floor the values
        for val in self.vector:
            new_v.append(floor(val))

        # Returns the new vector
        return new_v

    # Allows for vector addition
    def __add__(self, other: 'Vect') -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The addition will only work between same-dimension vectors
        if len(self.vector) == len(other):
            for i, val in enumerate(self.vector):
                new_v.append(val + other[i])
        else:
            raise(Exception('Vectors are not of equal length'))

        # Return the new vector
        return new_v

    # Allows for vector subtraction
    def __sub__(self, other: 'Vect') -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The subtraction will only work between same-dimension vectors
        if len(self.vector) == len(other):
            for i, val in enumerate(self.vector):
                new_v.append(val - other[i])
        else:
            raise(Excpetion('Vectors are not of equal length'))

        # Return the new vector
        return new_v

    # Allows for scalar multiplication in vect * scal form
    def __mul__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The multiplication can only take place if scalar is float or int
        if type(other) in [float, int]:
            for i, val in enumerate(self.vector):
                new_v.append(val * other)
        else:
            raise(Exception('Scalar is not a float or int'))

        # Return the new vector
        return new_v

    # Allows for scalar multiplication in scal * vect form
    def __rmul__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The mulitplication can only take place if scalar is float or int
        if type(other) in [float, int]:
            for val in self.vector:
                new_v.append(val * other)
        else:
            raise(Exception('Scalar is not a float or int'))

        # Return the new vector
        return new_v

    # Allows for scalar division in vect / scal form (only)
    def __truediv__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The division can only take place if scalar is float or
        # int and not zero
        if type(other) in [float, int] and other != 0:
            for val in self.vector:
                new_v.append(val / other)
        else:
            raise(Excpetion('Scalar is not a float or int, or is equal to 0'))

        # return the new vector
        return new_v

    # Allows for scalar floor division in vect // scal form (only)
    def __floordiv__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The division can only take place if scalar is float or
        # int and not zero
        if type(other) in [float, int] and other != 0:
            for val in self.vector:
                new_v.append(val // other)
        else:
            raise(Exception('Scalar is not a float or int, or is equal to 0'))

        # return the new vector
        return new_v

    # Allows for modulo operation on the vector
    def __mod__(self, value: int) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector for modulo operation
        if type(other) == int:
            for val in self.vector:
                new_v.append(val % other)
        else:
            raise(Exception('Value is not a int'))

    # Allows for power operation on the vector
    def __pow__(self, value: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # Iterates through the vector for power operation
        if type(value) in [float, int]:
            for val in self.vector:
                new_v.append(pow(val, value))
        else:
            raise(Exception('Value is not an int or float'))

        # Return the new vector
        return new_v

    # Utility Functions

    def append(self, value: Union[int, float]) -> None:
        '''
        Function: append
        Params:
            value: [int, float] The value to be appended to the vector
        Description:
            append takes a value and places it at the end of the vector
        '''
        # Checks if the value is float or int and then appends to the vector
        if type(value) in [int, float]:
            self.vector.append(value)
        else:
            raise(Exception('Value is not int or float'))

    def add(self, *args: Union[int, float, 'Vect']) -> None:
        '''
        Function: add
        Params:
            args: [int, float, vector] The values to be added to the vector
        Description:
            add takes the arguments and adds them all onto the vector itself
        '''
        # Checks if the arguments are int, float, or a vector
        for arg in args:
            if type(arg) in [int, float]:
                for i, val in enumerate(self.vector):
                    self.vector[i] += arg
            elif type(arg) == type(Vect()):
                for i, val in enumerate(self.vector):
                    self.vector[i] += arg[i]
            else:
                raise(Exception('Argument is not an int, float, or vector'))

    def sub(self, *args: Union[int, float, 'Vect']) -> None:
        '''
        Function: sub
        Params:
            args: [int, float, vector] The values to be subtracted from the
                vector
        Description:
            sub takes the arguments and subtracts them all from the vector
                itself
        '''
        # Checks if the arguments are int, float, or a vector
        for arg in args:
            if type(arg) in [int, float]:
                for i, val in enumerate(self.vector):
                    self.vector[i] -= arg
            elif type(arg) == type(Vect()):
                for i, val in enumerate(self.vector):
                    self.vector[i] -= arg[i]
            else:
                raise(Exception('Argument is not an int, float, or vector'))

    def mult(self, *args: Union[int, float]) -> None:
        '''
        Function: mult
        Params:
            args: [int, float] The scalars to multiply the vector against
        Description:
            mult takes the arguments and multiplies them all onto the vector
                itself
        '''
        # Checks if the arguments are int or float
        for arg in args:
            if type(arg) in [int, float]:
                for i, val in enumerate(self.vector):
                    self.vector[i] *= arg
            else:
                raise(Exception('Argument is not an int or a float'))

    def div(self, *args: Union[int, float], div_type: str='reg') -> None:
        '''
        Function: div
        Params:
            args: [int, float] The scalars to divide against
            div_type: [str] The type of division wanted ('reg' or 'floor')
        Description:
            div takes the arguments and divides them all onto the vector itself
        '''
        # Checks if the arguments are int or float
        for arg in args:
            if type(arg) in [int, float]:
                for i, val in enumerate(self.vector):
                    if div_type == 'reg':
                        self.vector[i] /= arg
                    elif div_type == 'floor':
                        self.vector[i] = val // arg
                    else:
                        raise(Exception('div_type not a proper value'))
            else:
                raise(Exception('Argument is not an int or a float'))

    def dot(self, other: 'Vect') -> float:
        '''
        Function: dot
        Params:
            other: [vector] The other vector to dot product with
        Description:
            dot takes the current vector and dots it with another vector
        '''
        # Variable to hold the result
        result = 0

        # Checks to see if both vectors are of the same length
        if len(self.vector) == len(other):
            for i, val in enumerate(self.vector):
                result += val * other[i]
        else:
            raise(Exception('Vectors are not of equal length'))

        # Return the result
        return result

    def angle_between(self, other: 'Vect',
                      ret_type: str='list') -> Union[float, list]:
        '''
        Function: angle_between
        Params:
            other: [vector] The other vector to grab the angle from
            ret_typ: [str] The return type; A 'list' of angles, or 'one'
                general angle
        Description:
            angle_between takes the current vector and another and finds the
                angle between them
        '''
        # The variable to hold the result
        result = []

        # Checks to see if both vectors are of the same length
        if len(self.vector) == len(other):
            if ret_type == 'list':
                i = 0
                while i < len(self.vector) - 1:
                    v1 = Vect(self.vector[i], self.vector[i+1])
                    v2 = Vect(other[i], other[i+1])
                    result.append(acos(v1.dot(v2) / (abs(v1) * abs(v2))))
                    i += 1
            elif ret_type == 'one':
                result = (acos(self.dot(other) / (abs(self) * abs(other))))
            else:
                raise(Exception('ret_type does not match argument values'))
        else:
            raise(Exception('Vectors are not of equal length'))

        # Return the result
        return result

    def angle(self, ret_type: str='list') -> Union[float, list]:
        '''
        Function: angle
        Params:
            ret_type: [str] The return type; A 'list' of angles, or 'one'
                general angle
        Description:
            angle takes the angle between the vector and an 'origin' vector
        '''
        # The origin vector
        origin = Vect()
        i = 0
        while i < len(self.vector):
            if i == len(self.vector) - 1:
                origin.append(0)
            else:
                origin.append(1)
            i += 1

        # return the angle between
        return self.angle_between(origin, ret_type)
    
    def cross(self, other: 'Vect') -> 'Vect':
        '''
        Function: cross
        Params:
            other: [vector] The other vector to cross product with
        Description:
            cross takes the cross product between two 3d vectors
        '''
        # New vector to hold the result
        new_v = Vect()

        # Checks if both vectors are 3D
        if len(self.vector) == 3 and len(other) == 3:
            new_v.append(self.vector[1] * other[2] - self.vector[2] * other[1])
            new_v.append(self.vector[2] * other[0] - self.vector[0] * other[2])
            new_v.append(self.vector[0] * other[1] - self.vector[1] * other[0])
        else:
            raise(Exception('Both vectors are not 3-dimensional'))

        # Return the new vector
        return new_v

    def fill(self, dim: int, val: Union[float, int]=0) -> 'Vect':
        '''
        Function: zeros
        Params:
            dim: [int] The dimension of the vector
            val: [float, int] The value to fill the vector with
        Description:
            zeros creates a vector of dim-dimension full of val
        '''
        # A new vector to hold the values
        new_v = Vect()

        # Loop to fill the vector with 0s
        i = 0
        while i < dim:
            new_v.append(val)
            i += 1

        # Return the vector
        return new_v

# Test condition

if __name__ == '__main__':
    a = Vect(1, 0, 0)
    b = Vect(0, 2, 0)
    print(a + b)
    print(a - b)
    c = 5
    print(a * 5)
    print(a / 5)
    print(a // 5)
    print(a ** 2)
    print(a.dot(b))
    print(a.cross(b))
    print(a.cross(-b))
    a = Vect(1, 0)
    print(a.angle(ret_type='one'))
    b = Vect(0, 5)
    print(a.angle_between(b, ret_type='one'))
    a = Vect(1, 2, 3)
    b = Vect(3, 2, 1)
    print(a.angle_between(b))
    print(a.angle_between(b, ret_type='one'))