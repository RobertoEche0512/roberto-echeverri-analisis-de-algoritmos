"""Las pruebas son verificar que ambos algoritmos funcionan bien"""

# Se traen las funciones que vamos a probar
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def test_serie_ejemplo():
    """Prueba principal: el caso que viene en el enunciado del laboratorio"""
    # Esta es la lista de valores que nos dieron como ejemplo
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    # Probamos con el método de fuerza bruta
    res_fb = subarreglo_fuerza_bruta(serie)
    # La respuesta correcta debe ser 17
    assert res_fb[2] == 17, f"Esperábamos 17, pero dio {res_fb[2]}"
    print(f" Fuerza bruta → desde el índice {res_fb[0]} hasta {res_fb[1]}, suma = {res_fb[2]}")

    # Luego probamos con divide y vencerás
    res_dyv = subarreglo_maximo(serie, 0, len(serie) - 1)
    # Debe dar el mismo resultadoque el otro método
    assert res_dyv[2] == 17, f"Esperábamos 17, pero dio {res_dyv[2]}"
    print(f" Divide y vencerás → desde el índice {res_dyv[0]} hasta {res_dyv[1]}, suma = {res_dyv[2]}")


def test_todos_negativos():
    """Cuando todos los números son negativos, la mejor opción es el menos malo"""
    datos = [-5, -2, -8, -1]
    # El menos negativo es -1
    assert subarreglo_fuerza_bruta(datos)[2] == -1
    assert subarreglo_maximo(datos, 0, len(datos) - 1)[2] == -1
    print(" Los negativos: funciona bien")


def test_un_elemento():
    """Si solo hay un número, ese es la respuesta"""
    datos = [42]
    assert subarreglo_fuerza_bruta(datos)[2] == 42
    assert subarreglo_maximo(datos, 0, 0)[2] == 42
    print(" Un solo elemento: funciona bien")


def test_todos_positivos():
    """Si todos son positivos, lo mejor es sumar todo junto"""
    datos = [2, 3, 1, 5]
    # La suma de todos es 11
    assert subarreglo_fuerza_bruta(datos)[2] == 11
    assert subarreglo_maximo(datos, 0, len(datos) - 1)[2] == 11
    print(" Los positivos: funciona bien")


# Ejecutamos todas las pruebas al correr el archivo
if __name__ == "__main__":
    test_serie_ejemplo()
    test_todos_negativos()
    test_un_elemento()
    test_todos_positivos()
    print("\n Todo salió bien: todas las pruebas son correctas")