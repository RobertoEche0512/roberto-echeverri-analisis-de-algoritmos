# Retroalimentación — Laboratorio evaluativo 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Roberto Echeverri Arroyave · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `768edbb`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 17 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 12 / 20 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **68 / 100** |
| **Nota (0–5)** | **3.40** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Separa bien "da el resultado correcto" de "lo entrega a tiempo" y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica por qué duplicar el servidor no basta (el tiempo crece con el cuadrado y el volumen seguirá subiendo).
- Incluye un segundo ejemplo propio (facturación de un consultorio) con cifras y una restricción clara.
- En la Parte 2 relaciona el tiempo con el gasto de energía acumulado y señala quién asume el costo del error.

**Lo que puede mejorar:**
- El segundo perjuicio de la Parte 2 (operador y paciente) se parece mucho al primero; sería mejor un caso distinto, por ejemplo el de la Secretaría o el equipo de desarrollo.

## 2. Calidad de la explicación teórica (17 / 25)
**Lo que hizo bien:**
- En 3.1 define los tres casos indicando sobre qué se toma cada uno, justifica usar el peor caso y deja la predicción escrita antes de medir.
- La recurrencia de merge sort está bien explicada y el método maestro verifica la condición del caso 2.
- La tabla de complejidades es correcta.

**Lo que puede mejorar:**
- El análisis línea a línea de insertion sort se queda corto: dice cuántas veces corre cada línea del `for`, pero no suma los costos ni llega al resultado final (por ejemplo `n(n-1)/2` en el peor caso) para cada caso.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista recibida y cuentan solo comparaciones entre elementos. Los conteos son los esperados (por ejemplo 45 comparaciones para el peor caso con 10 elementos).
- Los generadores devuelven listas del tamaño pedido y sin repetidos.

**Lo que puede mejorar:**
- En `datos.py` usó `sorted()` para armar los escenarios B y C con tamaños grandes. Aunque no está en los algoritmos, la regla era no usar funciones de ordenamiento de Python; conviene construir esas listas sin ellas.
- Los generadores cambian de forma de construir la lista según el tamaño (hasta 1001 o más) y el inverso usa una semilla fija escondida (123); eso hace el código confuso.
- Faltan docstrings en las funciones internas del merge sort y en `medir`/`medir_insertion` no tienen el formato Google completo. Los archivos no terminan con una línea en blanco.

## 4. Calidad del análisis de las gráficas (12 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidades y leyenda, y muestran lo que usted describe.
- Identifica con cifras el peor caso (inverso), el mejor (casi ordenado) y el promedio (aleatorio), y lo contrasta con su predicción.
- En 4.3 recomienda merge sort, estima 7,1 horas para insertion sort y declara que es una estimación, y menciona la memoria extra.

**Lo que puede mejorar:**
- Las gráficas no se ven en el informe: solo escribió la ruta como texto. Debían incrustarse como imagen para que se vean en GitHub.
- La respuesta al servidor del doble de velocidad no cita explícitamente la gráfica ni el tamaño de donde sale el dato.
- Falta explicar con más cuidado por qué con tamaños pequeños los dos algoritmos se parecen, y la extrapolación de merge sort podría explicar mejor el factor del logaritmo.

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en un lugar válido y tiene todos los archivos pedidos.
- El informe sigue el orden de las partes y trae instrucciones para ejecutar.

**Lo que puede mejorar:**
- Las gráficas no están incrustadas con imagen.
- Los enlaces al código de las Partes 3 y 4 son solo texto, no enlaces; faltan enlaces a `algoritmos.py` y `datos.py` en las primeras menciones fuera de la Parte 3.
- Hay un solo commit del laboratorio y se pedían al menos cinco con avance gradual.
- Las instrucciones para activar el entorno solo sirven en Windows y no se menciona la instalación de `matplotlib`.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien y ambos scripts corren sin errores y generan las tres gráficas.

## Para el próximo laboratorio
- Incruste las gráficas con la sintaxis de imagen de Markdown y verifique que se vean en GitHub.
- Haga commits pequeños y descriptivos a medida que avanza (mínimo cinco).
- Muestre el desarrollo completo de cada cálculo, sumando los costos hasta el resultado final.
- Evite `sorted()` en cualquier parte del código, también en los generadores de datos.
- Redacte y revise todo el texto con sus palabras, sin símbolos sueltos.
