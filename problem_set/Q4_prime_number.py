# A prime number is a number that is divisble only by 1 and itself
# examples are 2,3,5,7
# 4,6,8 are not prime numbers as they are divisble by other numbers 

# Write a function that checks if the following number is prime:

number = 107352437281

# Do not use a naive approach of checking every single number below
# At the least, do not check even numbers

def prime_number_solver(number):
    divisor = 3
    sqrt_number = number**.5
    compute = 0
    #check if even: num % 2 == 0
    if number == 1:
        print("1 is neither prime nor composite!")
        return None
    elif number == 2:
        print("2 is a prime number!")
        return False
    else:
        if number % 2 == 0:
            print(f"{number} is composite! It is even!")
            return False
    while divisor <= sqrt_number:
        compute = number % divisor
        if compute == 0:
            print(f"{number} is composite! It failed with {divisor}.")
            return False
        divisor += 2
    else:
        print(f"{number} is prime!")
        return True
x=prime_number_solver(49)
print(x)