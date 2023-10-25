from scipy.stats import chi2
import numpy as np

def promedio(r_list: list):
    """
    Devuelve el valor promedio de una lista de valores dados
    """
    n = len(r_list)
    
    r_sum = 0
    for value in r_list:
        r_sum += value

    r_avg = (1 / n) * r_sum
    return r_avg

def V_r_list(r_list: list):
    r_avg = promedio(r_list)
    n = len(r_list)

    r_sum = 0
    for value in r_list:
        r_sum += (value - r_avg)**2

    return r_sum / (n - 1) 

def lowerBound(n:int, confidence: float):
    alpha = 1 - confidence
    degrees_of_freedom = n - 1 
    chi2_value = chi2.ppf((1-alpha)/2, degrees_of_freedom)
    LB = chi2_value / (12*(n-1)) 
    return LB

def lowerBound(n:int, confidence: float):
    alpha = 1 - confidence
    degrees_of_freedom = n - 1 
    chi2_value = chi2.ppf(alpha/2, degrees_of_freedom)
    LB = chi2_value / (12 * (n - 1)) 
    return LB

def upperBound(n:int, confidence: float):
    alpha = 1 - confidence
    degrees_of_freedom = n - 1 
    chi2_value = chi2.ppf(1-alpha/2, degrees_of_freedom)
    UB = chi2_value / (12 * (n - 1)) 
    return UB
    
def pruebaDeVarianza(confidence: float, r_list: list):
    V_r = V_r_list(r_list)
    n = len(r_list)
    LB = lowerBound(n, confidence)
    UB = upperBound(n, confidence)

    return V_r, LB, UB


if __name__ == "__main__":
    # Test only
    confidence = 0.95
    alpha = 1 - confidence
    r_list = [0.4667, 0.6667, 0.6, 0., 0.2, 0.9333, 0.3333, 0.2667, 1., 0.1333 ,0.0667, 0.5333, 0.7333, 0.4, 0.8667, 0.8]

    V_r, LB, UB = pruebaDeVarianza(confidence, r_list)

    print("Prueba de varianza")

    print(f"Varianza: {V_r}, Lower bound: {LB}, Upper bound: {UB}")

    if (V_r >= LB and V_r <= UB):
        print(f"La varianza se encuentra entre los limites, no se rechaza H0 con un nivel de aceptación de {confidence}")
    else:
        print(f"La varianza no se encuentra entre los limites, se rechaza H0 con un nivel de aceptación de {confidence}")
