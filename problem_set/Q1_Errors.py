# This python code has errors, fix them
#I am Done
from math import pi


def counting_numbers(x: int) -> list:
    """
    Creates a list of numbers up to and including x beginning from 0,
    x > 0
    """
    result=[]
    numbers=0
    if x <= 0:
        return [0]
    while numbers <= x:
        result.append(numbers)
        numbers += 1
    return result

# numbers=counting_numbers(-5)
# print(numbers)

def old_enough_to_drive(age: str) -> int:
    """
    return True if age is over 16
    """
    if age>16:
        return True
    else:
        return False

# old_enough = old_enough_to_drive(20)

# print(f"This age is old enough: {old_enough}")

def volume_of_sphere(radius: float) -> float:
    """
    Returns the volume of a sphere given a radius
    """
    Volume = (4/3)*pi*radius**3

    return Volume


# vol1 = volume_of_sphere(2)

# print(vol1)
