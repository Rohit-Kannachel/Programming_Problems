# Newton-Raphson method for finding roots of a function

# Use this root finding method to evaluate the square root of 2 to 6 decimal places

# The square root of 2 is 1.414213 or 1.4142135623730951

true_value = 1.414213
import math
# compare your answer with the true value

# Define the function whose root we are trying to find

### write comments and code here ###
## Tool 1
def function_x(x):
    ##define the function you're using
    y= x**2 - 2
    return y
# print(newton_rahpson(math.pi/2))


# def RootstoQuadratic(x1,x2):
#     """
#     Using the knowledge of what a factored Quadratic looks like: x1,x2 = x² -x(x1+x2) + x1*x2.
#     We can descrivbe a quadratic equation for any two inputted roots (in the Real plane).
#     a = 1 because the value of c may compensate for the distances between the roots. 
#     (I hope to fix the issue and optimize for using a so that the value of c doesn't erupt.)
#     """
#     a= 1
#     b= -(x1+x2)
#     c= (x1*x2)
#     equation = f"x² "
#     if b == 0:
#         equation = f"x² "
#     else:
#         if b < 0:
#             equation += f"- {-b}x "
#         else:
#             equation += f"+ {b}x "

#     if c < 0:
#         equation += f"- {-c}"
#     else:
#         equation += f"+ {c}"
#     if c == 0:
#         equation = f"x²"
#     print(f"The equation for these roots is: {equation}")
#     return a,b,c
# a,b,c = RootstoQuadratic((3/2),6)

# # Define the derivative of the function

# ### write comments and code here ###
# ## Tool 2

def derivative_of_f(x):
    ##define the derivative of the fuction you input before
    y_prime= 2*(x)
    return y_prime


# """
# We have an advantage because we always know we are dealing with a quadratic.
# It will be: 2x -(x1 + x2)
# """
# def QuadraticDerivative(b):
#     if b != 0:
#         if b < 0:
#             print(f"The derivative is: 2x - {-b}")
#         else:
#             print(f"The derivative is: 2x + {b}")
#     else:
#         print("The derivative is: 2x")
#     return b
# QuadraticDerivative(b)
# # Run the algorithm for the necessary amount of iterations to converge to 6 d.p. accuracy, make sure to start with a good initial guess
# ## Newton_Raphson_method
## xn+1 = xn - f(x)/f'(x)
def newton_rahpson(guess: int):
    """
    This function uses a parent and derivative to approximate a root given an initial guess. To a certain error.
    """
    y = 1
    while abs(y) > .000001:
        next_guess = guess - (function_x(guess)/derivative_of_f(guess))
        guess=next_guess
        y = function_x(next_guess)
    return next_guess

print(newton_rahpson(5))