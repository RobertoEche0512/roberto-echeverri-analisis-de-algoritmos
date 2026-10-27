"""Pruebas deterministas y aleatorias para ambos algoritmos."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def comparar_algoritmos(valores: list[int]) -> None:
    """Comprueba que ambos algoritmos encuentran la misma suma máxima.

    Args:
        valores: Lista no vacía de enteros que se desea evaluar.

    Returns:
        None. Si los resultados no coinciden, assert genera un error.
    """
    resultado_fb = subarreglo_fuerza_bruta(valores)
    resultado_dyv = subarreglo_maximo(valores, 0, len(valores) - 1)
    assert resultado_fb[2] == resultado_dyv[2], (
        f"Resultados diferentes para {valores}: "
        f"{resultado_fb[2]} != {resultado_dyv[2]}"
    )


def main() -> None:
    """Ejecuta los casos conocidos y veinte pruebas aleatorias."""
    ejemplo = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(ejemplo)[2] == 17
    assert subarreglo_maximo(ejemplo, 0, len(ejemplo) - 1)[2] == 17

    # Caso explícito: el mejor subarreglo cruza la mitad.
    cruzado = [4, -1, 3, -2, 5, -1]
    assert subarreglo_fuerza_bruta(cruzado)[2] == 9
    assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 9

    comparar_algoritmos([-5, -2, -8, -1])
    comparar_algoritmos([42])
    comparar_algoritmos([2, 3, 1, 5])
    comparar_algoritmos([-4, -2, -7])
    comparar_algoritmos([0, 0, 0, 0])

    random.seed(2026)
    for numero_prueba in range(1, 21):
        longitud = random.randint(1, 30)
        valores = [random.randint(-100, 100) for _ in range(longitud)]
        comparar_algoritmos(valores)
        print(f"Prueba aleatoria {numero_prueba:02d}/20 superada (n={longitud}).")

    print("Todas las pruebas fueron superadas.")


if __name__ == "__main__":
    main()
