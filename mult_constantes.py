from pydantic import BaseModel, conint

class nonDigitos(Exception):
    def __init__(self, mensaje="The seed must have d digits"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class multConstParams(BaseModel):
    d: conint(gt=3)
    x0: conint(gt=0)
    a: conint(gt=3)  # Nueva entrada para la constante 'a'
    output_len: conint(gt=0)

def checkDigitos(value: int, d: int) -> bool:
    return True if len(str(value)) == d else False

def dDigitosCentrales(y_str: str, d: int) -> str:
    while len(y_str) < d:
        y_str = '0' + y_str
    return y_str[int(len(y_str) / 2) - int(d / 2):int(len(y_str) / 2) + int(d / 2)]

def zeros(value: int, d: int = 0, y_flag: int = 0) -> str:
    value_str = str(value)
    if y_flag:
        while len(value_str) < 2 * d:
            value_str = '0' + value_str
    else:
        while len(value_str) % 2 != 0:
            value_str = '0' + value_str
    return value_str

def algoritmoMultConstante(x0: str, a: str, d: int, output_len: int = 10) -> list:
    x_list = []
    y_list = []
    r_list = []

    x_list.append(x0)

    for i in range(output_len):
        y_i = a * int(x_list[i])
        y_i_str = zeros(y_i, d, 1)
        y_list.append(y_i_str)

        x_list.append(dDigitosCentrales(y_i_str, d))

        r_i_str = '0.' + x_list[i + 1]
        r_list.append(float(r_i_str))

    return y_list, r_list

def multConstante(params: multConstParams) -> list:
    output_len = params.output_len
    d = params.d
    a = params.a
    if d % 2 != 0:
        d += 1
    x0 = zeros(params.x0)

    if not checkDigitos(x0, d):
        raise nonDigitos(f"The seed {x0} must have {d} digits")

    y_list, r_list = algoritmoMultConstante(x0, a, d, output_len)
    return y_list, r_list

if __name__ == "__main__":
    test_params = {
        "d": 4,
        "x0": 1568,
        "a": 1234,  
        "output_len": 12
    }

    y_list, r_list = multConstante(multConstParams(**test_params))

    print("Valores para test")
    for key, value in test_params.items():
        print(f"{key}: {value}")
    print("resultados")
    for i in range(len(y_list)):
        print(f"y[{i+1}]: {y_list[i]}  --> r[{i+1}]: {r_list[i]}")
