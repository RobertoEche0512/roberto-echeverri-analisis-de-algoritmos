"""Mediciones de tiempo de busqueda: lista enlazada frente a tabla hash."""

import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion."""
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def primo_cercano(objetivo: int) -> int:
    """Devuelve el primo mas cercano por debajo o igual a `objetivo`."""
    if objetivo < 2:
        return 2

    def es_primo(x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    candidato = objetivo
    while not es_primo(candidato):
        candidato -= 1
    return candidato


def generar_guias(n: int, semilla: int = 42) -> list[int]:
    """Genera n guias distintas de diez digitos de forma reproducible."""
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def tiempo_medio_busqueda(
    estructura, guias: list[int], repeticiones: int
) -> float:
    """Cronometra solo las busquedas y devuelve el tiempo medio."""
    inicio = time.perf_counter()
    for guia in guias:
        estructura.buscar(guia)
    fin = time.perf_counter()
    return (fin - inicio) / repeticiones


def experimento_lista_vs_tabla() -> None:
    """Experimento A: compara lista y tabla al crecer n."""
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    repeticiones = 200
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in valores_n:
        guias = generar_guias(n)
        estados = ["en bodega", "en reparto", "entregado"]

        lista = ListaEnlazada()
        m = primo_cercano(max(3, n // 2))
        tabla = TablaHash(m)

        for i, guia in enumerate(guias):
            estado = estados[i % len(estados)]
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias[: min(50, n)]:
            assert lista.buscar(guia) == tabla.buscar(guia)

        inexistentes = generar_guias_inexistentes(set(guias), repeticiones)
        t_lista = tiempo_medio_busqueda(lista, inexistentes, repeticiones)
        t_tabla = tiempo_medio_busqueda(tabla, inexistentes, repeticiones)

        tiempos_lista.append(t_lista)
        tiempos_tabla.append(t_tabla)
        print(
            f"n={n:>6}  m={m:>6}  lista={t_lista * 1e6:9.3f} us  "
            f"tabla={t_tabla * 1e6:9.3f} us"
        )

    plt.figure()
    plt.plot(valores_n, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(valores_n, tiempos_tabla, marker="s", label="Tabla hash")
    plt.title("Tiempo medio de busqueda frente al numero de guias")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_factor_carga() -> None:
    """Experimento B: efecto del factor de carga con n fijo."""
    n = 20000
    guias = generar_guias(n)
    estados = ["en bodega", "en reparto", "entregado"]
    repeticiones = 200

    alfas = [0.5, 1.0, 2.0, 4.0, 8.0]
    tiempos: list[float] = []
    alfas_reales: list[float] = []

    for alfa in alfas:
        m = max(2, int(n / alfa))
        tabla = TablaHash(m)
        for i, guia in enumerate(guias):
            tabla.insertar(guia, estados[i % len(estados)])

        inexistentes = generar_guias_inexistentes(set(guias), repeticiones)
        t = tiempo_medio_busqueda(tabla, inexistentes, repeticiones)
        tiempos.append(t)
        alfas_reales.append(tabla.factor_carga())
        print(
            f"alfa objetivo={alfa:>4}  alfa real={tabla.factor_carga():7.3f}  "
            f"tiempo={t * 1e6:9.3f} us"
        )

    plt.figure()
    plt.plot(alfas_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Tiempo medio de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    experimento_lista_vs_tabla()
    experimento_factor_carga()