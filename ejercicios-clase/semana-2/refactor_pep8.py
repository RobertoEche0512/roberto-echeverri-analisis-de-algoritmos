def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números.

    Args:
        numeros (list): Lista de valores numéricos.

    Returns:
        float: Promedio de los números.
    """
    if not numeros:
        return 0.0

    return sum(numeros) / len(numeros)


def clasificar_promedio(promedio):
    """Clasifica un promedio en categorías.

    Args:
        promedio (float): Valor promedio calculado.

    Returns:
        str: Categoría correspondiente.
    """
    if promedio >= 90:
        return "Excelente"
    if promedio >= 75:
        return "Bueno"
    if promedio >= 60:
        return "Aceptable"
    return "Deficiente"


def main():
    """Función principal del programa."""
    valores = [85, 90, 78, 92, 88]

    promedio = calcular_promedio(valores)
    categoria = clasificar_promedio(promedio)

    print(f"Promedio: {promedio:.2f}")
    print(f"Clasificación: {categoria}")


if __name__ == "__main__":
    main()
