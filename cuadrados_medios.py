from pydantic import BaseModel, conint, validator
import numpy as np

class nonDigitos(Exception):
    def __init__(self, mensaje="The seed must have d digits"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class cuadParams(BaseModel):
    d: conint(gt=3)
    x0: conint(gt=0)
    output_len: conint(gt=0)

def checkDigitos(value: int, d: int) -> bool:
    return True if (len(value)) == d else False

def dDigitosCentrales(y_str: int, d: int) -> str: 
    while (len(str(y_str)) < 2*d):
        y_str = f"0{y_str}"

    y_d = y_str[int(d/2):int(-d/2)]

    return y_d

def zeros(value: int, d: int = 0, y_flag: int = 0) -> str:
    """
    Funcion para agregar ceros si el numero de digitos es impar 
    """
    value_str = str(value)
    if (y_flag):
        while (len(str(value_str)) < 2*d):
            value_str = f"0{value_str}"
    else:
        while (len(value_str) % 2 != 0):
            value_str = f"0{value_str}"
    
    return value_str


def algoritmoCuadMedios (x0: str, d: str, output_len: int = 10) -> list:
    x_list = []
    y_list = []
    r_list = []

    x_list.append(x0)

    
    for i in range(output_len):

        y_i = pow(int(x_list[i]), 2)
        y_i_str = zeros(y_i, d, 1)
        y_list.append(y_i_str)

        x_list.append(dDigitosCentrales(y_i_str, d))

        r_i_str = f"0.{x_list[i+1]}"
        r_list.append(float(r_i_str))

    #x_list = x_list[1:]
    
    return y_list, r_list




    




def cuadMedios(params: cuadParams) -> list:
    output_len = params.output_len
    #Parámetros
    d = params.d
    if (d % 2 != 0):
        d += 1
    x0 = zeros(params.x0)

    if (checkDigitos(x0,d) == False):
        raise nonDigitos(f"La semilla {x0} debe tener {d} dígitos")
    
    if output_len:
        y_list, r_list = algoritmoCuadMedios(x0, d, output_len)
    else:
        y_list, r_list = algoritmoCuadMedios(x0, d)
    return y_list, r_list

    
    


    pass


if __name__ == "__main__":
    test_params = {
        "d": 4,
        "x0": 1568,
        "output_len": 12
    }

    cuadMedios(cuadParams(**test_params))
 
