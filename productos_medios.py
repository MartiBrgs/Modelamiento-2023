from pydantic import BaseModel, conint
import numpy as np

class nonDDigitNumber(Exception):
    def __init__(self, mensaje="The seed must have D digits"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class prodMParams(BaseModel):
    D: conint(gt=3)
    """
    pow(10,D-1) es el primer numero de D cifras
    Pro ejemplo: D = 4 --> 10^(D-1)=10^(3)=1000
    y 1000 es el primer numero de D=4 cifras
    """
    x0: conint(gt=0) 
    x1: conint(gt=0)
    output_len: conint(gt=0)

def checkDDigits(value: int, D: int) -> bool:
    return True if (len(value) == D) else False

def DCentralDigits(y_str: str, D: int) -> str:
    """
    agregar ceros antes del numero cuando ocurra el caso
    que el numero de digitos resultante no sea el doble 
    del numero de digitos de las raices
    """
    while (len(y_str) < 2 * D):
        y_str = f"0{y_str}"

    # print(y_str)
    slices = int(D/2)
    y_central_d = y_str[slices:-slices]
    # print(y_central_d)
    return y_central_d

def zeroPadding(value: int, D: int = 0, y_flag: int = 0) -> str:
    """
    Si el numero de digitos es impar, se agregar ceros
    a la izquierda del número para que el numero sea par
    y asi si hayan D digitos centrales
    """
    value_str = str(value)
    if (y_flag):
        while (len(value_str) < 2*D):
            value_str = f"0{value_str}"
    else:
        while (len(value_str) % 2 != 0):
            value_str = f"0{value_str}"
        
    return value_str

def algortimoProdMedios(x0: str, x1: str, D: int, output_len: int = 10) -> list:
    x_list = []
    y_list = []
    r_list = []
    
    x_list.append(x0)
    x_list.append(x1)

    # Desarrollo algoritmo
    for i in range(output_len):
        
        y_i = int(x_list[i]) * int(x_list[i+1])
        y_i_str = zeroPadding(y_i, D, 1)
        y_list.append(y_i_str)

        x_list.append(DCentralDigits(y_i_str, D))

        r_i_str = f"0.{x_list[i+2]}"
        r_list.append(float(r_i_str))

    # x_list = x_list[2:]

    return y_list, r_list

def prodMedios(params: prodMParams) -> list:
    output_len = params.output_len

    # Parámetros del algoritmo
    D = params.D
    # si D es impar, se convierte en par sumandole 1
    if (D % 2 != 0):
        D += 1
    # Si D es impar se agregan ceros a la izquierda de los numeros dados
    x0 = zeroPadding(params.x0)
    x1 = zeroPadding(params.x1)

    if not(checkDDigits(x0,D) and checkDDigits(x1,D)):
        error = f"Las dos semillas deben tener D={D} digitos"
        raise nonDDigitNumber(error)

    # obteniendo D digitos centrales
    if output_len:
        y_list, r_list = algortimoProdMedios(x0, x1, D, output_len)
    
    else:
        y_list, r_list = algortimoProdMedios(x0, x1, D)
    
    return y_list, r_list

if __name__ == "__main__":
    
    test_params = {
        "D": 4,
        "x0": 1568,
        "x1": 1568,
        "output_len": 10
    }

    prodMedios(prodMParams(**test_params))