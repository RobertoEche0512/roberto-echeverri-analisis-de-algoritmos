"""Algoritmos para encontrar el subarreglo contiguo de suma máxima."""

def subarreglo_fuerza_bruta(valores: list[int]) -> tuple[int, int, int]:
    """Encuentra por fuerza bruta el subarreglo contiguo de suma máxima.

    Args:
        valores: Lista no vacía de números enteros.

    Returns:
        Una tupla (índice_inicio, índice_fin, suma_maxima).

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not valores:
        raise ValueError("La lista debe contener al menos un elemento.")

    n = len(valores)
    suma_maxima = valores[0]
    mejor_inicio = mejor_fin = 0

    for inicio in range(n):
        suma_actual = 0
        for fin in range(inicio, n):
            suma_actual += valores[fin]
            if suma_actual > suma_maxima:
                suma_maxima = suma_actual
                mejor_inicio, mejor_fin = inicio, fin

    return mejor_inicio, mejor_fin, suma_maxima


def suma_cruzada(
    valores: list[int], inicio: int, medio: int, fin: int
) -> tuple[int, int, int]:
    """Calcula el mejor subarreglo que cruza la división entre medio y medio+1.

    Args:
        valores: Lista de enteros.
        inicio: Índice inicial del segmento que se analiza.
        medio: Último índice de la mitad izquierda.
        fin: Índice final del segmento que se analiza.

    Returns:
        Una tupla (índice_inicio, índice_fin, suma_maxima_cruzada).
    """
    suma_actual = 0
    mejor_suma_izquierda = valores[medio]
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    suma_actual = 0
    mejor_suma_derecha = valores[medio + 1]
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    return mejor_inicio, mejor_fin, mejor_suma_izquierda + mejor_suma_derecha


def subarreglo_maximo(
    valores: list[int], inicio: int, fin: int
) -> tuple[int, int, int]:
    """Encuentra recursivamente el subarreglo contiguo de suma máxima.

    Args:
        valores: Lista de enteros.
        inicio: Índice inicial del segmento que se analizará.
        fin: Índice final del segmento que se analizará.

    Returns:
        Una tupla (índice_inicio, índice_fin, suma_maxima).
    """
    if not valores:
        raise ValueError("La lista debe contener al menos un elemento.")
    if inicio < 0 or fin >= len(valores) or inicio > fin:
        raise ValueError("Los índices deben delimitar un segmento válido.")

    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2
    izq_inicio, izq_fin, izq_suma = subarreglo_maximo(valores, inicio, medio)
    der_inicio, der_fin, der_suma = subarreglo_maximo(valores, medio + 1, fin)
    cruz_inicio, cruz_fin, cruz_suma = suma_cruzada(valores, inicio, medio, fin)

    if izq_suma >= der_suma and izq_suma >= cruz_suma:
        return izq_inicio, izq_fin, izq_suma
    if der_suma >= izq_suma and der_suma >= cruz_suma:
        return der_inicio, der_fin, der_suma
    return cruz_inicio, cruz_fin, cruz_suma
