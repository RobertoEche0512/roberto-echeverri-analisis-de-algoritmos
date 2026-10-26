"""Subarreglo máximo: fuerza bruta y divide y vencerás."""

from typing import Tuple


def subarreglo_fuerza_bruta(valores: list[float]) -> Tuple[int, int, float]:
    """
    Se busca el tramo de números consecutivos que da la suma más alta.
    Se revisa literalmente todas las posibilidades, una por una.
    Complejidad: Θ(n²) entre más valores, mucho más lento.
    """
    n = len(valores)
    suma_max = valores[0]  # Empezamos suponiendo que el primer valor es el mayor
    i_mejor = j_mejor = 0  # Aquí guardaremos dónde empieza y termina la mejor suma

    # Probamos cada inicio del tramo
    for i in range(n):
        suma_actual = 0  # Se reinicia la suma cada vez que cambiamos de inicio

        # Desde ese inicio, extendiendo el tramo hacia la derecha
        for j in range(i, n):
            suma_actual += valores[j]  # sumamos sin volver a calcular todo

            # Encontrando algo mejor, actualizamos los registros
            if suma_actual > suma_max:
                suma_max = suma_actual
                i_mejor, j_mejor = i, j

    return (i_mejor, j_mejor, suma_max)


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> Tuple[int, int, float]:
    """
    Busca la mejor suma que pase obligatoriamente por el centro del arreglo.
    Es necesario para la versión divide y vencerás, porque la mejor suma puede
    partir de dos mitades y no caer en una sola.
    Complejidad: Θ(n) recorre cada lado una sola vez.
    """
    # Hacia la izquierda: desde el medio al principio
    suma_actual = 0
    max_izq = valores[medio]
    pos_izq = medio
    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > max_izq:
            max_izq = suma_actual
            pos_izq = i

    # Hacia la derecha: desde  despuéss del medio al final
    suma_actual = 0
    max_der = valores[medio + 1]
    pos_der = medio + 1
    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > max_der:
            max_der = suma_actual
            pos_der = j

    # Se une lo mejor de cada lado: que es el mejor tramo que cruza el centro
    return (pos_izq, pos_der, max_izq + max_der)


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> Tuple[int, int, float]:
    """
    Encuentra la suma máxima usando divide y vencerás.
    Se divide el problema en dos mitades, se resuelve cada una por su cuenta,
    y revisa si la mejor solución cruza la división.
    Complejidad: Θ(n log n) mucho más rápido que fuerza bruta con datos grandes.
    """
    # Caso simple: si solo hay un número, él mismo es la mejor suma
    if inicio == fin:
        return (inicio, fin, valores[inicio])

    # Dividir: partimos el arreglo justo por la mitad
    medio = (inicio + fin) // 2

    # Conquistar: se busca la mejor suma en cada mitad por separado
    izq_in, izq_fin, izq_suma = subarreglo_maximo(valores, inicio, medio)
    der_in, der_fin, der_suma = subarreglo_maximo(valores, medio + 1, fin)

    # Combinar: también se busca la mejor suma que pase por la mitad
    cruz_in, cruz_fin, cruz_suma = suma_cruzada(valores, inicio, medio, fin)

    # Se toma la mejor de las tres opciones encontradas
    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return (izq_in, izq_fin, izq_suma)       # La mejor está en la izquierda
    elif der_suma >= izq_suma and der_suma >= cruz_suma:
        return (der_in, der_fin, der_suma)       # La mejor está en la derecha
    else:
        return (cruz_in, cruz_fin, cruz_suma)    # La mejor une ambas mitades