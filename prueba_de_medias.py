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

def pruebaDeMedias(r_list: list, confidence: float=0.95):
    r_avg = promedio(r_list)
    n = len(r_list)
    LB = lowerBound(n, confidence)
    UB = upperBound(n, confidence)

    r_avg = round(r_avg, 4)
    LB = round(LB, 4)
    UB = round(UB, 4)

    pmedias_list = [r_avg, LB, UB]

    return pmedias_list


if __name__ == "__main__":
    # Test only
    r_list = [0.4667, 0.6667, 0.6, 0., 0.2, 0.9333, 0.3333, 0.2667, 1., 0.1333 ,0.0667, 0.5333, 0.7333, 0.4, 0.8667, 0.8]

    pmedias = pruebaDeMedias(r_list=r_list)

    print("Prueba de medias")

    print(f"promedio: {pmedias[0]}, Lower bound: {pmedias[1]}, Upper bound: {pmedias[2]}")

    if (pmedias[0] >= pmedias[1] and pmedias[0] <= pmedias[2]):
        print("El promedio se encuentra entre los limites, no se rechaza H0")
    else:
        print("El promedio no se encuentra entre los limites, se rechaza H0")
