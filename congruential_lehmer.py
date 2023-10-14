"""
This script contains differents methods of getting random numbers
"""
from pydantic import BaseModel, conint
import numpy as np

class NonPrimeRelativesNumbers(Exception):
    def __init__(self, mensaje="The congruential algorithm needs c and m to be relatively prime numbers"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class congruentialParam(BaseModel):
    x0: conint(gt=0)
    k: conint(gt=0)
    g: conint(gt=0)
    c: conint(gt=0)

def relative_prime_checker(a:int, b:int) -> int:
    """
    This function check if two numbers are relative primes to each other
    It will only check from 2 to 99 their greatest common divisor (GCD)
    """
    for i in range(2,100):
        if a % i == 0 and b % i == 0:
            return i
    return 0

def lehmer_algorithm(x0, a, c, m) -> list:
    """
    This function returns two lists, one with the x_n 
    and the other one with the actual random number r_n
    """

    # initilizes two lists with zeros
    x_list = np.zeros(m+1)
    r_list = np.zeros(m)
    # Add the first seed to the x list
    x_list[0] = x0

    # Calculating every x and adding it to the list
    for i in range(len(x_list)-1):
        x_list[i+1] = (a * x_list[i] + c) % m

    # Making the list start from x1 up to xn
    x_list = x_list[1:]

    # Calculating every r_i associated with every x_i, with i=1,2,3...
    for i in range(len(x_list)):
        r_list[i] = x_list[i] / (m - 1)

    # rounding to 4 decimals
    r_list = np.round(r_list, decimals=4)

    return x_list, r_list


def congruential(params: congruentialParam) -> list:
    """
    This function creates a list of random generated numbers between 0 and 1
    using the D.H Lehmer congruential algorithm (a linear algorithm)

    Inputs are:
    x0: an integer wich represents the initial seed for the algorithm
    k: an integer used to define "a"
    g: an integer to define "m=2^g", wich is the maximum life time of the algorithm (N)
    c: an integer that should be a relative prime to "m"

    Returns two lists of lenght "m" containing #m random generated numbers in list_r (floats between 0 and 1)
    and the inter-calculations of x's.
    """
    # Parameters
    x0 = params.x0
    k = params.k
    g = params.g
    c = params.c

    m = pow(2,g)
    a = 1 + (4 * k)

    # Checking if m and c are relatively prime numbers    
    gcd = relative_prime_checker(m,c) # calculates gratest common divisor between m and c
    
    if (gcd > 1):
        error = "The congruential algorithm needs c and m to be relatively prime numbers.\n" + \
                f"c={c}, m={m}, Gretest Common Divisor={gcd}"
        raise NonPrimeRelativesNumbers(error)

    # Generating the random generated numbers
    x_list, r_list = lehmer_algorithm(x0, a, c, m)

    return x_list, r_list

if __name__ == "__main__":
    
    test_params = {
        "x0": 6, 
        "k": 3, 
        "g": 3, 
        "c": 7
    }
    
    x_list, r_list = congruential(congruentialParam(**test_params))

    print("Valores para lehmer")
    for key, value in test_params.items():
        print(f"{key}: {value}")
    print("resultados")
    for i in range(len(x_list)):
        print(f"x[{i+1}]: {x_list[i]}  --> r[{i+1}]: {r_list[i]}")
