# Laboratorio 02 — Divide y vencerás: subarreglo máximo

**Estudiante:** Roberto Echeverri Arroyave  
**Asignatura:** Análisis de algoritmos

## Objetivo

Este proyecto compara dos algoritmos para encontrar el subarreglo contiguo cuya suma es máxima: **fuerza bruta** y **divide y vencerás**. También analiza sus tiempos de ejecución y su comportamiento al aumentar el tamaño de la entrada.

## Contenido del repositorio

- `subarreglo.py`: implementación de los algoritmos.
- `pruebas.py`: pruebas para verificar sus resultados.
- `medicion.py`: experimento para medir los tiempos.
- `graficas/tiempo_vs_n.png`: gráfica comparativa generada por el experimento.

## Cómo ejecutar el proyecto

Desde la carpeta del proyecto, ejecuta las pruebas:


Para medir los tiempos y generar la gráfica:

Ejecuta las pruebas y la medición:

```bash
python pruebas.py
python medicion.py
```

El experimento utiliza listas de números enteros aleatorios entre -100 y 100, con tamaños de entrada de 10, 25, 50, 100, 200, 400, 800, 1600, 4000 y 5000. Los tiempos se miden con time.perf_counter().

## Implementación y Verificación de las soluciones

Se implementaron dos métodos:

Fuerza bruta: revisa las posibles posiciones de inicio y fin para encontrar el subarreglo con la mayor suma.
Divide y vencerás: divide el arreglo en dos mitades y compara el mejor resultado de la mitad izquierda, la mitad derecha y el subarreglo que cruza el punto medio.
Las pruebas contemplan distintos casos, como arreglos de un solo elemento, valores negativos y ceros. También incluyen arreglos aleatorios para comprobar que ambos algoritmos obtengan el mismo resultado.

## Gráfica y análisis de rendimiento

Gráfica comparativa de tiempos

La gráfica compara el tiempo de ejecución de ambos algoritmos para los tamaños probados. En general, se espera que fuerza bruta crezca como Θ(n²) y que divide y vencerás crezca como Θ(n log n). Por eso, al aumentar n, divide y vencerás debería ser más eficiente.

Los tiempos dependen del computador y de las condiciones de ejecución. La gráfica muestra los resultados del experimento realizado; no permite afirmar un punto exacto de cruce entre los algoritmos si ese punto no se midió directamente.

## Recurrencia de divide y vencerás

Para un arreglo de tamaño n, el algoritmo resuelve dos subproblemas, cada uno de tamaño aproximado n/2:

Encuentra el mejor subarreglo de la mitad izquierda.
Encuentra el mejor subarreglo de la mitad derecha.
Encuentra el mejor subarreglo que cruza el punto medio.
El paso de combinación busca el mejor sufijo de la mitad izquierda y el mejor prefijo de la mitad derecha. Para ello recorre, en conjunto, hasta n elementos; por tanto, combinar cuesta Θ(n).

La recurrencia es:

T(n) = 2T(n/2) + Θ(n)

Al resolverla se obtiene T(n) = Θ(n log n).

La fuerza bruta tiene un costo de Θ(n²), porque examina las posibles parejas de inicio y fin del subarreglo y calcula o acumula las sumas correspondientes.

## Comparación con hallar el máximo de un arreglo

Hallar solamente el elemento máximo de un arreglo dividido en dos mitades también produce dos subproblemas de tamaño n/2, pero combinar cuesta Θ(1): basta comparar los dos máximos obtenidos. Su recurrencia es:

T(n) = 2T(n/2) + Θ(1)

Esta recurrencia da Θ(n). En cambio, para el subarreglo máximo, combinar cuesta Θ(n) porque hay que buscar el mejor tramo que cruza el punto medio. Esa diferencia en el costo de combinación lleva a la recurrencia Θ(n log n).

## Tamaños pequeños

Para entradas pequeñas, los tiempos de ambos algoritmos pueden ser muy parecidos. Divide y vencerás tiene trabajo adicional por sus llamadas recursivas y por la combinación de resultados; con entradas pequeñas, ese costo puede reducir su ventaja. Con las mediciones realizadas no se establece un punto exacto a partir del cual un algoritmo supera al otro, así que no se afirma un umbral que no haya sido medido.

## Estimación para 1.000.000 de registros

La siguiente proyección usa como referencia los tiempos medidos para 5.000 elementos. Es una estimación, no una medición directa para un millón de registros. Se supone que el tiempo crece según el orden teórico de cada algoritmo.

Fuerza bruta: Θ(n²)
Se multiplica el tiempo medido por el cuadrado de la proporción entre los tamaños:

0,672102 s × (1.000.000 / 5.000)² ≈ 26.884 s

Esto equivale aproximadamente a 7,47 horas.

Divide y vencerás: Θ(n log₂ n)
Se multiplica el tiempo medido por el factor de crecimiento n log₂ n:

0,009772 s × [(1.000.000 × log₂(1.000.000)) / (5.000 × log₂(5.000))] ≈ 3,17 s

Estas cifras son aproximadas. El tiempo real puede cambiar según el computador, la carga del sistema y la implementación.

## Recomendación para la cooperativa

Recomiendo divide y vencerás para analizar un historial de un millón de registros. Según la estimación, tardaría cerca de 3,17 segundos, frente a unas 7,47 horas para fuerza bruta. La recomendación se basa en su crecimiento Θ(n log n), mucho más favorable para entradas grandes que el crecimiento Θ(n²) de fuerza bruta.