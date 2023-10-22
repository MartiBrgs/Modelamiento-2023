"""
This script contains congruential product method for getting random numbers
"""
from pydantic import BaseModel, conint, validator
import numpy as np

class NonConditionError(Exception):
    def __init__(self, mensaje="The conditions are not met"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Validando datos de entrada
class multParams(BaseModel):
    x0: conint(gt=0)
    a: conint(gt=0)
    b: conint(gt=0)
    c: conint(gt=0)
    g: conint(gt=0)

def odd_check(value: int) -> bool:
    if value % 2 == 0:
        return False
    return True

def even_check(value: int) -> bool:
    if value % 2 != 0:
        return False
    return True

def int_check(numero):
  try:
    int(numero)
    return True
  except NonConditionError:
    return False

    
def algorit_no_lineal_cuad(x0, a, b, c, m, N) -> list:
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
        x_list[i+1] = (a * pow(x_list[i],2) + b * x_list[i] + c) % m

    x_list = x_list[1:]

    # Calculating r_n values
    for i in range(len(x_list)):
        r_list[i] = x_list[i] / (m - 1)

    # rounding to 4 decimals
    r_list = np.round(r_list, decimals=4)

    return x_list, r_list


    
def noLinealCuad(params: multParams) -> list:
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

    a = params.a
    if (odd_check(a) == True):
        error = f"El valor de a debe ser par\nValor ingresado a: {a}"
        raise NonConditionError(error)

    
    b = params.b
    if ((b - 1) % 4 != 1):
        error = f"No se cumple con la condición (b -1) mod 4 = 1\nValor ingrsado: {b}"

    c = params.c
    if (odd_check(c) == False):
        error = f"El valor de c debe ser impar\nValor ingresado c: {c}"
        raise NonConditionError(error)

    g = params.g

    if (int_check(g) != True):
        error = f"El valor de g no es entero\nValor ingresado g: {g}"
        raise NonConditionError(error)

    m = pow(2, g)
    N = m
    # life time of the algorithm

    # Obtaining random number list
    x_list, r_list = algorit_no_lineal_cuad(x0, a, b, c, m, N)

    return x_list, r_list


# Testing only
if __name__ == "__main__":
    
    test_params = {
        "x0": 15, 
        "a": 2, 
        "b": 5,
        "c": 7,
        "g": 4
    }
    
    x_list, r_list = noLinealCuad(multParams(**test_params))

    print("Valores para congruencial multiplicativo")
    for key, value in test_params.items():
        print(f"{key}: {value}")
    print("resultados")
    for i in range(len(x_list)):
        print(f"x[{i+1}]: {x_list[i]}  --> r[{i+1}]: {r_list[i]}")