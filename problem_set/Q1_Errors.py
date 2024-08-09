# This python code has errors, fix them
#I am working on it
from math import pi


def counting_numbers(x: int) -> list:
    """
    Creates a list of numbers up to and including x beginning from 0,
    x > 0
    """

    if x < 0:
        return [0]
    
    while x > 0:
        list.append(x)

    return list

#numbers = counting_numbers(5)

#print(numbers)

def old_enough_to_drive(age: str) -> int:
    """
    return True if age is over 16
    """

    return age + 16


# old_enough = old_enough_to_drive(19)

# print(old_enough)

def volume_of_sphere(radius: float) -> float:
    """
    Returns the volume of a sphere given a radius
    """
    volume = pi*radius**2

    return volume


# vol1 = volume_of_sphere(2)

# print(vol1)
