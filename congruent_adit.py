from pydantic import BaseModel, conint

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

    for i in range(n + 1, n + output_len + 1):
        xi = (sequence[-1] + sequence[-n]) % m
        sequence.append(xi)
    
    return n, sequence  # Devolver n junto con la secuencia generada

def congruentAditivo(n, sequence, m):
    r_list = [x / m for x in sequence[n:]]
    return r_list

if __name__ == "__main__":
    test_params = {
        "n": 5,  # Cantidad de elementos de la lista inicial 
        "x_values": [65, 89, 98, 3, 5],  # Valores iniciales 
        "m": 100,  
        "output_len": 15
    }