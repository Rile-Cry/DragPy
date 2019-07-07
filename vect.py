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
        None
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

    # Allows indexing of the vector
    def __getitem__(self, key: int) -> Union[float,  int]:
        return self.vector[key]

    # Allows to set the value at certain indexes
    def __setitem__(self, key: int, value: Union[float, int]):
        if type(value) in [float, int]:
            return self.vector[key] = value
        else:
            raise(Exception('Value is not int or float.'))

    # Allows returning of the vector
    def __repr__(self) -> list:
        return self.vector

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
    def __floor_(self) -> 'Vect':
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
            for i, val in self.vector:
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
    def __div__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The division can only take place if scalar is float or
        # int and not zero
        if type(other) in [float, int] and other != 0:
            for val in self.vector:
                new_v.append(val / other)
        else:
            raise(Excpetion('Scalar is not a float or int, or is equal to 0'))

    # Allows for floor division of the vector in vect / scal form (only)
    def __floordiv__(self, other: Union[float, int]) -> 'Vect':
        # A new vector to hold the new values
        new_v = Vect()

        # The division can only take place if scalar is float or int
        # and the value is not zero
        if type(other) in [float, int] and other != 0:
            for val in self.vector:
                new_v.append(val // other)
        else:
            raise(Exception('Scalar is not a float or int, or is equal to 0'))

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

# Test condition

if __name__ == '__main__':
    v = Vect()