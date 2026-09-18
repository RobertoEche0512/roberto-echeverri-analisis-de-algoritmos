"""Experimento de peor caso, mejor caso y caso promedio para insertion sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def medir_insertion(datos: list[int]) -> tuple[float, int]:
    """Mide tiempo y comparaciones de insertion_sort sobre una copia de datos."""
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()
    return fin - inicio, comparaciones


def main() -> None:
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    escenarios = {
        "A (aleatorio)": generar_aleatorio,
        "B (casi ordenado)": generar_casi_ordenado,
        "C (inverso)": generar_inverso,
    }

    resultados_tiempo: dict[str, list[float]] = {nombre: [] for nombre in escenarios}
    resultados_comp: dict[str, list[int]] = {nombre: [] for nombre in escenarios}

    print("Ejecutando mediciones de insertion sort...")
    for n in tamanos:
        print(f"  n = {n}")
        for nombre, generador in escenarios.items():
            if nombre == "C (inverso)":
                datos = generador(n)
            else:
                datos = generador(n, semilla=42)

            tiempos = []
            comps = []
            for _ in range(3):
                t, c = medir_insertion(datos)
                tiempos.append(t)
                comps.append(c)
            resultados_tiempo[nombre].append(sum(tiempos) / 3)
            resultados_comp[nombre].append(sum(comps) // 3)

            print(f"    {nombre}: tiempo={resultados_tiempo[nombre][-1]:.6f}s, "
                  f"comparaciones={resultados_comp[nombre][-1]}")

    graficas_dir = Path("graficas")
    graficas_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    for nombre, comps in resultados_comp.items():
        plt.plot(tamanos, comps, marker="o", label=nombre)
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.title("Insertion sort: comparaciones vs. tamaño de entrada")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(graficas_dir / "parte3_comparaciones.png", dpi=150)
    plt.close()
    print("Guardada graficas/parte3_comparaciones.png")

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in resultados_tiempo.items():
        plt.plot(tamanos, tiempos, marker="o", label=nombre)
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Insertion sort: tiempo vs. tamaño de entrada")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(graficas_dir / "parte3_tiempo.png", dpi=150)
    plt.close()
    print("Guardada graficas/parte3_tiempo.png")

    print("\n=== Resumen de resultados (n=6400) ===")
    for nombre in escenarios:
        print(f"{nombre}: tiempo={resultados_tiempo[nombre][-1]:.6f}s, "
              f"comparaciones={resultados_comp[nombre][-1]}")


if __name__ == "__main__":
    main()