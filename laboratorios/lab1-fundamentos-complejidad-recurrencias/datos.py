"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random
from typing import List


def generar_aleatorio(n: int, semilla: int = 42) -> List[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)
    if n <= 1001:
        indices = list(range(n))
        random.shuffle(indices)
        return indices
    else:
        indices = random.sample(range(0, n * 2), n)
        return indices


def generar_casi_ordenado(n: int, semilla: int = 42) -> List[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    El 98% inicial está ordenado de mayor a menor (como produce el algoritmo).
    El 2% restante está desordenado y anexado al final.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    random.seed(semilla)
    if n <= 1001:
        base = list(range(n - 1, -1, -1))  # ordenado mayor a menor
    else:
        base = sorted(random.sample(range(0, n * 2), n), reverse=True)

    corte = int(n * 0.98)
    parte_ordenada = base[:corte]
    parte_desordenada = base[corte:]
    random.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> List[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Orden ascendente (menor a mayor), que es el inverso del orden
    deseado (mayor a menor).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    if n <= 1001:
        return list(range(n))  # ascendente = inverso de descendente
    else:
        import random
        random.seed(123)
        return sorted(random.sample(range(0, n * 2), n))