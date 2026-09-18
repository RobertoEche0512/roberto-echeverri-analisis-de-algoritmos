"""Medición comparativa de insertion sort vs merge sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def medir(algoritmo, datos: list[int]) -> float:
    """Mide solo el tiempo de ejecución del algoritmo."""
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return fin - inicio


def main() -> None:
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    algoritmos = {
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
    }

    resultados: dict[str, list[float]] = {nombre: [] for nombre in algoritmos}

    print("Ejecutando mediciones comparativas (escenario A - aleatorio)...")
    for n in tamanos:
        print(f"  n = {n}")
        datos = generar_aleatorio(n, semilla=42)
        for nombre, algo in algoritmos.items():
            tiempos = [medir(algo, datos) for _ in range(3)]
            promedio = sum(tiempos) / 3
            resultados[nombre].append(promedio)
            print(f"    {nombre}: {promedio:.6f}s")

    graficas_dir = Path("graficas")
    graficas_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in resultados.items():
        plt.plot(tamanos, tiempos, marker="o", label=nombre)
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución: Insertion sort vs Merge sort (escenario aleatorio)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(graficas_dir / "parte4_tiempo.png", dpi=150)
    plt.close()
    print("Guardada graficas/parte4_tiempo.png")

    print("\n=== Resumen (n=6400) ===")
    for nombre in algoritmos:
        print(f"{nombre}: {resultados[nombre][-1]:.6f}s")


if __name__ == "__main__":
    main()