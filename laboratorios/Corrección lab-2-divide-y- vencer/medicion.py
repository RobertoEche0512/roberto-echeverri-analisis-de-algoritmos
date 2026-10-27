"""Medición reproducible del rendimiento de los algoritmos."""

import os
import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempo(funcion, *argumentos) -> float:
    """Mide la duración de una llamada a una función.

    Args:
        funcion: Función cuyo tiempo de ejecución se desea medir.
        *argumentos: Argumentos posicionales que recibirá la función.

    Returns:
        Tiempo de ejecución en segundos, medido con perf_counter.
    """
    inicio = time.perf_counter()
    resultado = funcion(*argumentos)
    fin = time.perf_counter()
    return fin - inicio


def main() -> None:
    """Ejecuta las mediciones, imprime razones de crecimiento y crea la gráfica."""
    random.seed(2026)
    tamanos = [10, 25, 50, 100, 200, 400, 800, 1600, 4000, 5000]
    tiempos_fb = []
    tiempos_dyv = []

    print("Comparación de tiempos (segundos)")
    print(f"{'n':>6} | {'Fuerza bruta':>14} | {'Divide y vencerás':>18} | {'Razón FB/DyV':>13}")

    for n in tamanos:
        datos = [random.randint(-100, 100) for _ in range(n)]

        resultado_fb = subarreglo_fuerza_bruta(datos)
        resultado_dyv = subarreglo_maximo(datos, 0, n - 1)
        assert resultado_fb[2] == resultado_dyv[2], (
            f"Las sumas no coinciden para n={n}: "
            f"{resultado_fb[2]} != {resultado_dyv[2]}"
        )

        # Medición de cada algoritmo sobre exactamente la misma lista.
        t_fb = medir_tiempo(subarreglo_fuerza_bruta, datos)
        t_dyv = medir_tiempo(subarreglo_maximo, datos, 0, n - 1)

        tiempos_fb.append(t_fb)
        tiempos_dyv.append(t_dyv)
        razon = t_fb / t_dyv if t_dyv > 0 else float("inf")
        print(f"{n:6d} | {t_fb:14.6f} | {t_dyv:18.6f} | {razon:13.2f}x")

    # Extrapolación teórica a un millón de elementos usando el mayor tamaño medido.
    n0 = tamanos[-1]
    factor_fb = (1_000_000 / n0) ** 2
    factor_dyv = (1_000_000 * __import__("math").log2(1_000_000)) / (
        n0 * __import__("math").log2(n0)
    )
    estimacion_fb = tiempos_fb[-1] * factor_fb
    estimacion_dyv = tiempos_dyv[-1] * factor_dyv
    print("\nEstimación teórica para 1.000.000 de elementos (no es una medición):")
    print(f"Fuerza bruta: aproximadamente {estimacion_fb:.2f} segundos ({estimacion_fb/3600:.2f} horas).")
    print(f"Divide y vencerás: aproximadamente {estimacion_dyv:.2f} segundos ({estimacion_dyv/60:.2f} minutos).")
    print("La extrapolación supone que se mantienen los órdenes de crecimiento; el tiempo real puede variar.")

    print("\nFactores al duplicar n (se muestran solo pares exactos n y 2n):")
    mapa = {n: i for i, n in enumerate(tamanos)}
    for n in tamanos:
        if 2 * n in mapa:
            i, j = mapa[n], mapa[2 * n]
            factor_fb = tiempos_fb[j] / tiempos_fb[i] if tiempos_fb[i] else float("inf")
            factor_dyv = tiempos_dyv[j] / tiempos_dyv[i] if tiempos_dyv[i] else float("inf")
            teorico_fb = 4.0
            teorico_dyv = (2 * n * __import__("math").log2(2 * n)) / (
                n * __import__("math").log2(n)
            ) if n > 1 else float("nan")
            print(
                f"n={n:4d} -> {2*n:4d}: "
                f"FB={factor_fb:.2f}x (referencia Θ(n²)≈{teorico_fb:.2f}x); "
                f"DyV={factor_dyv:.2f}x (referencia Θ(n log n)≈{teorico_dyv:.2f}x)"
            )

    os.makedirs("graficas", exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, "o-", label="Fuerza bruta")
    plt.plot(tamanos, tiempos_dyv, "s-", label="Divide y vencerás")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Subarreglo máximo: fuerza bruta vs. divide y vencerás")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_n.png", dpi=150)
    print("\nGráfica guardada en graficas/tiempo_vs_n.png")
    print("Los tiempos son mediciones de esta ejecución; pueden variar entre equipos.")


if __name__ == "__main__":
    main()
