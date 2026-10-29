"""Pruebas de verificacion para ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_busquedas_basicas() -> None:
    """Verifica busquedas exitosas e infructuosas en lista y tabla."""
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(9999999999) is None

    tabla = TablaHash(7)
    tabla.insertar(1000000010, "en bodega")
    tabla.insertar(1000000024, "en reparto")
    assert tabla.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000024) == "en reparto"
    assert tabla.buscar(9999999999) is None


def probar_colision_forzada() -> None:
    """Fuerza la colision de 10, 24 y 17 en la casilla 3 con m = 7."""
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias(cantidad: int = 20) -> None:
    """Compara lista y tabla en colecciones aleatorias de guias."""
    for semilla in range(cantidad):
        azar = random.Random(semilla)
        n = azar.randint(1, 50)
        guias = azar.sample(range(10**9, 10**10), n)

        lista = ListaEnlazada()
        tabla = TablaHash(7)
        for guia in guias:
            estado = azar.choice(["en bodega", "en reparto", "entregado"])
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        candidatas = [
            g for g in range(10**9, 10**9 + 1000) if g not in set(guias)
        ]
        inexistentes = azar.sample(candidatas, 5)
        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None


if __name__ == "__main__":
    probar_busquedas_basicas()
    probar_colision_forzada()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")