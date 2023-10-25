from scipy.stats import norm
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

def lowerBound(n: int, confidence: float):
    alpha_over_2 = (1 - confidence) / 2
    z_value = norm.ppf(1 - alpha_over_2)
    return (1/2) - z_value * (1 / np.sqrt(12 * n)) 

def upperBound(n: int, confidence: float):
    alpha_over_2 = (1 - confidence) / 2
    z_value = norm.ppf(1 - alpha_over_2)
    return (1/2) + z_value * (1 / np.sqrt(12 * n)) 

def pruebaDeMedias(confidence: float, r_list: list):
    r_avg = promedio(r_list)
    n = len(r_list)
    LB = lowerBound(n, confidence)
    UB = upperBound(n, confidence)

    return r_avg, LB, UB


if __name__ == "__main__":
    # Test only
    confidence = 0.95
    r_list = [0.4667, 0.6667, 0.6, 0., 0.2, 0.9333, 0.3333, 0.2667, 1., 0.1333 ,0.0667, 0.5333, 0.7333, 0.4, 0.8667, 0.8]

    r_avg, LB, UB = pruebaDeMedias(confidence, r_list)

    print("Prueba de medias")

    print(f"promedio: {r_avg}, Lower bound: {LB}, Upper bound: {UB}")

    if (r_avg >= LB and r_avg <= UB):
        print("El promedio se encuentra entre los limites, no se rechaza H0")
    else:
        print("El promedio no se encuentra entre los limites, se rechaza H0")
