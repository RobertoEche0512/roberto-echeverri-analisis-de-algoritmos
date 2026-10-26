"""Se mide cuánto tarda cada algoritmo y graficamos los resultados"""

import time       # Para medir el tiempo que se tarda
import random     # Se generan listas de números al azar
import os         # Crear la carpeta donde guardaremos la gráfica
import matplotlib.pyplot as plt  # Dibuja la gráfica

# Se tienen los dos algoritmos que se van a comparar
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_tiempo(funcion, *argumentos):
    """Ejecuta una función y se devuelve los segundos que tardó"""
    # Tomamos la hora exacta antes de empezar
    hora_inicio = time.time()
    # Ejecutamos la función con los datos que le pasamos
    funcion(*argumentos)
    # Restamos la hora de inicio con la hora de fin para saber cuánto tardó
    return time.time() - hora_inicio


def main():
    # Se prueban distintos tamaños de lista para ver cómo crece el tiempo
    tamanos = [50, 100, 200, 400, 800, 1200, 1600]

    # Se guardan los tiempos de cada método
    tiempos_fuerza_bruta = []
    tiempos_divide_y_venceras = []

    print(" Comparando tiempos de ejecución ")

    # Se prueba cada tamaño de lista
    for n in tamanos:
        # Creamos una lista con números al azar entre -10 y 10
        datos = [random.uniform(-10, 10) for _ in range(n)]

        # Se mide cuánto tarda fuerza bruta
        t_fb = medir_tiempo(subarreglo_fuerza_bruta, datos)

        # Se mide cuánto tarda divide y vencerás
        t_dyv = medir_tiempo(subarreglo_maximo, datos, 0, n - 1)

        # Se guardan los resultados para graficar
        tiempos_fuerza_bruta.append(t_fb)
        tiempos_divide_y_venceras.append(t_dyv)

        # En pantalla se muestra el avance
        print(f"n = {n:4d} | Fuerza bruta: {t_fb:.6f}s | Divide y vencerás: {t_dyv:.6f}s")

    # Se crea la carpeta "graficas" 
    os.makedirs("graficas", exist_ok=True)

    # Se dibuja la gráfica
    plt.figure(figsize=(10, 6))
    # La línea roja para fuerza bruta
    plt.plot(tamanos, tiempos_fuerza_bruta, "o-", label="Fuerza bruta", color="#e74c3c")
    # La línea verde para divide y vencerás
    plt.plot(tamanos, tiempos_divide_y_venceras, "s-", label="Divide y vencerás", color="#2ecc71")

    # Etiquetas para la gráfica
    plt.xlabel("Cantidad de números en la lista")
    plt.ylabel("Tiempo que tardó (segundos)")
    plt.title("Comparación: Fuerza bruta vs. Divide y vencerás")
    plt.legend()  # leyenda con colores
    plt.grid(True, alpha=0.3)  # Líneas en el fondo para leer mejor

    # se guarda ala gráfica como imagen y la mostramos
    plt.savefig("graficas/tiempo_vs_n.png", dpi=150)
    print("\n La gráfica se guardó en: graficas/tiempo_vs_n.png")
    plt.show()

# Con esto se corre todo el archivo
if __name__ == "__main__":
    main()