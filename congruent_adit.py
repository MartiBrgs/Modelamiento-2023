from pydantic import BaseModel, conint
import numpy as np

class nonDigitos(Exception):
    def __init__(self, mensaje="The seed must have D digits"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Params(BaseModel):
    n: conint(ge=1)  # Longitud de la secuencia previa
    x_values: list  # Lista de n números enteros iniciales
    m: conint(gt=0)  # Módulo m, debe ser un entero positivo
    output_len: conint(gt=0)

def secuenciaX(params: Params):
    n = params.n
    x_values = params.x_values
    m = params.m
    output_len = params.output_len

    if len(x_values) != n:
        raise ValueError(f"La longitud de la secuencia previa debe ser igual a n = {n}")

    sequence = x_values.copy()

    for i in range(n, n + output_len):
        xi = (sequence[i-1] + sequence[i-n]) % m
        sequence.append(xi)

    return n, sequence[n:]  

def congruentAditivo(n, sequence, m):
    r_list = [x / (m - 1) for x in sequence]
    return r_list

if __name__ == "__main__":
    test_params = {
        "n": 3,  # Cantidad de elementos de la lista inicial 
        "x_values": [15, 23, 38],  # Valores iniciales 
        "m": 100,  
        "output_len": 15
    }

    n, x_list = secuenciaX(Params(**test_params))
    r_list = congruentAditivo(n, x_list, test_params["m"])
    
    print("Secuencia X generada:", x_list)
    print("Números r_i:", r_list)
