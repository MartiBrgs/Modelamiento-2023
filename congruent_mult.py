"""
This script contains congruential product method for getting random numbers
"""
from pydantic import BaseModel, conint, validator
import numpy as np

class NonOddSeedError(Exception):
    def __init__(self, mensaje="The seed must be an odd number"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Validando datos de entrada
class multParams(BaseModel):
    x0: conint(gt=0)
    k: conint(ge=0)
    g: conint(gt=0)

def odd_check(value: int) -> bool:
    if value % 2 == 0:
        return False
    return True
    
def mult_c_algorithm(x0, a, m, N) -> list:
    """
    This function calculates random generated numbers with
    the product congruential method and returns two lists
    """

    # Initialazing numpy arrays to contain the numbers generated (to work with floats)
    x_list = np.zeros(N+1)
    r_list = np.zeros(N)

    x_list[0] = x0

    # Calculating x_n values
    for i in range(len(x_list) - 1):
        x_list[i+1] = (a * x_list[i]) % m

    x_list = x_list[1:]

    # Calculating r_n values
    for i in range(len(x_list)):
        r_list[i] = x_list[i] / (m - 1)

    # rounding to 4 decimals
    r_list = np.round(r_list, decimals=4)

    return x_list, r_list


    
def congruentMult(params: multParams) -> list:
    """
    This function creates a list of random generated numbers between 0 and 1
    using the product congruential algorithm

    Inputs are:
    x0: an odd integer wich represents the initial seed for the algorithm
    k: an integer used to define "a" k should be greater or equal to 0
    g: an integer to define "m=2^g", wich is the maximum life time of the algorithm (N)

    Returns two lists of lenght "m" containing #m random generated numbers in list_r (floats between 0 and 1)
    and the inter-calculations of x's.
    """
    # parameters
    x0 = params.x0

    if (odd_check(x0) == False):
        error = f"La semilla x0 debe ser impar\nValor ingresado x0: {x0}"
        raise NonOddSeedError(error)
    
    k = params.k
    g = params.g

    # a = 3 + (8 * k)
    a = 5 + (8 * k)
    m = pow(2, g)
    N = pow(2, g-2) # life time of the algorithm

    # Obtaining random number list
    x_list, r_list = mult_c_algorithm(x0, a, m, N)

    return x_list, r_list


# Testing only
if __name__ == "__main__":
    
    test_params = {
        "x0": 15, 
        "k": 2, 
        "g": 5
    }
    
    x_list, r_list = congruentMult(multParams(**test_params))

    print("Valores para congruencial multiplicativo")
    for key, value in test_params.items():
        print(f"{key}: {value}")
    print("resultados")
    for i in range(len(x_list)):
        print(f"x[{i+1}]: {x_list[i]}  --> r[{i+1}]: {r_list[i]}")