"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio (int): Año a evaluar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    return anio % 4 == 0


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros.

    Returns:
        list[int]: Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2000,2023,2024): ")
        try:
            return [int(x.strip()) for x in entrada.split(",")]
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    bisiestos = [a for a in anios if es_bisiesto(a)]

    print(f"\nAños ingresados: {anios}")
    print(f"Años bisiestos: {bisiestos}")
    print(f"Cantidad de años bisiestos: {len(bisiestos)} de {len(anios)}")


if __name__ == "__main__":
    main()
