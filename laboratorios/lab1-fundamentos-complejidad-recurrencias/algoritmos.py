"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

from typing import List, Tuple


def insertion_sort(datos: List[int]) -> Tuple[List[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor (riesgo alto primero), como requiere Tamiza.
    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos[:]  # copia para no modificar la original
    comparaciones = 0
    n = len(arreglo)

    for i in range(1, n):
        clave = arreglo[i]
        j = i - 1
        # Desplaza elementos menores que clave hacia la derecha
        # (porque ordenamos de mayor a menor)
        while j >= 0:
            comparaciones += 1  # comparación entre elementos
            if arreglo[j] < clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                break
        arreglo[j + 1] = clave

    return arreglo, comparaciones


def merge_sort(datos: List[int]) -> Tuple[List[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor (riesgo alto primero), como requiere Tamiza.
    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = [0]  # usamos lista para mutabilidad en recursión

    def merge(izquierda: List[int], derecha: List[int]) -> List[int]:
        resultado = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            comparaciones[0] += 1  # comparación entre elementos
            if izquierda[i] >= derecha[j]:  # mayor o igual primero
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    def _merge_sort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        medio = len(arr) // 2
        izquierda = _merge_sort(arr[:medio])
        derecha = _merge_sort(arr[medio:])
        return merge(izquierda, derecha)

    copia = datos[:]
    ordenado = _merge_sort(copia)
    return ordenado, comparaciones[0]