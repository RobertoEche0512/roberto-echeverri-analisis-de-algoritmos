# Laboratorio Evaluativo 02 — Divide y Vencerás: Subarreglo Máximo

**Estudiante:** Roberto Echeverri Arroyave  
**Curso:** Algoritmos y Estructuras de Datos

---

# Instrucciones para reproducir el experimento

## 1. Activar el entorno

```bash
# Desde la raíz del repositorio
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Ejecutar

```bash
python pruebas.py
python medicion.py
```

---

# Parte 1 — Verificación de las soluciones

**Código de los algoritmos:** `subarreglo.py`  
**Script de validación:** `pruebas.py`

Se verificó que ambos enfoques, **fuerza bruta** y **divide y vencerás**, entregan exactamente la misma suma máxima y los mismos límites de tramo para cada caso de prueba.

Los casos cubiertos fueron:

| Caso de prueba | Qué valida | Resultado esperado |
|----------------|------------|-------------------|
| `[-3, 5, -2, 8, -6, 3, 9, -4]` | Ejemplo principal del laboratorio | Suma = **17**, tramo índices 1 a 6 |
| `[-5, -2, -8, -1]` | Cuando no hay ganancia, se elige la menor pérdida | Suma = **-1** |
| `[42]` | Caso base mínimo posible | Suma = **42** |
| `[2, 3, 1, 5]` | Lo mejor es sumar todo el arreglo | Suma = **11** |

Cada prueba utiliza `assert` para comparar la salida de ambos algoritmos contra el resultado esperado. Si alguna validación falla, el programa se detiene e informa la discrepancia.

Al ejecutar:

```bash
python pruebas.py
```

se confirma que **todas las pruebas son superadas correctamente**.

Ambos métodos producen la misma solución, pero con costos computacionales diferentes:

- Fuerza bruta: **Θ(n²)**
- Divide y vencerás: **Θ(n log n)**

---

# Parte 2 — Medición y gráfica de rendimiento

**Script de medición:** `medicion.py`

## Cómo se realizó la medición

1. Se definieron **7 tamaños de entrada**: 50, 100, 200, 400, 800, 1200 y 1600 elementos.
2. Para cada tamaño se generó un arreglo aleatorio con valores entre -10 y 10.
3. Cada algoritmo se ejecutó sobre el **mismo arreglo**, garantizando igualdad de condiciones.
4. Se utilizó `time.perf_counter()` para medir tiempos antes y después de cada ejecución.
5. Los tiempos obtenidos fueron almacenados y mostrados en pantalla.
6. La gráfica se guardó automáticamente dentro de la carpeta `graficas/`.

## Gráfica comparativa

graficas/comparacion_subarreglo.png

## Interpretación

1. La línea **roja** corresponde a la solución por fuerza bruta. Su crecimiento es cuadrático y aumenta rápidamente a partir de tamaños cercanos a 400 elementos.
2. La línea **verde** representa divide y vencerás. Su crecimiento es mucho más moderado y sigue un comportamiento cercano a **n log n**.
3. Para **n = 1600**, divide y vencerás resulta aproximadamente **90 veces más rápido** que fuerza bruta.
4. En tamaños pequeños (menores a 100 elementos), la diferencia es reducida e incluso fuerza bruta puede parecer ligeramente más rápida debido a la ausencia de sobrecarga recursiva.
5. A medida que aumenta el tamaño de los datos, la ventaja de divide y vencerás se vuelve cada vez más evidente.

---

# Parte 3 — Respuestas del análisis

## 1. ¿Conviene aplicar divide y vencerás a este problema? ¿Por qué sí o por qué no?

Sí, conviene claramente.

A diferencia de problemas como encontrar el valor máximo de un arreglo, donde una solución recursiva no mejora la complejidad, en este caso el cambio de estrategia permite pasar de:

- **Θ(n²)** con fuerza bruta.
- **Θ(n log n)** con divide y vencerás.

La mejora no es únicamente teórica. También puede observarse experimentalmente en los tiempos de ejecución obtenidos y se amplía conforme aumenta el tamaño de la entrada.

---

## 2. ¿Cuál es la recurrencia del algoritmo de divide y vencerás implementado?

La recurrencia es:

```text
T(n) = 2T(n/2) + Θ(n)
```

Donde:

- El factor **2** representa los dos subproblemas generados.
- Cada subproblema tiene tamaño **n/2**.
- El término **Θ(n)** corresponde al costo de calcular el subarreglo cruzado y combinar resultados.

Aplicando el Teorema Maestro se obtiene:

```text
T(n) = Θ(n log n)
```

---

## 3. ¿Por qué la función `suma_cruzada` es necesaria? ¿No basta con elegir la mejor mitad?

No basta con tomar la mejor solución de la mitad izquierda o de la mitad derecha.

El subarreglo de suma máxima puede comenzar en la mitad izquierda y terminar en la mitad derecha. En ese caso, la solución óptima cruza el punto de división.

La función `suma_cruzada` evalúa precisamente esa posibilidad:

1. Recorre desde el centro hacia la izquierda buscando la mejor suma acumulada.
2. Recorre desde el centro hacia la derecha buscando la mejor suma acumulada.
3. Combina ambas partes para obtener el mejor tramo que cruza la división.

Sin esta función, el algoritmo podría descartar la solución óptima y producir resultados incorrectos.

---

## 4. ¿Qué pasaría si se aumentara el tamaño de entrada a 100.000 elementos?

### Fuerza bruta

El tiempo crecería aproximadamente:

```text
(100000 / 1600)² ≈ 3900
```

veces respecto a la prueba con 1600 elementos.

Un programa que tarda menos de un segundo podría pasar a requerir horas de ejecución.

### Divide y vencerás

El crecimiento sería aproximadamente:

```text
(100000 / 1600) × (log₂(100000) / log₂(1600)) ≈ 94
```

veces.

Seguiría siendo una alternativa práctica y ejecutable en tiempos razonables.

### Conclusión

La diferencia entre ambos enfoques aumentaría significativamente. Divide y vencerás seguiría siendo viable mientras que fuerza bruta dejaría de ser una opción práctica.

---

## 5. ¿Es cierto que "comprar un servidor más rápido resuelve el problema"?

No.

Comprar hardware más rápido únicamente reduce los tiempos de ejecución, pero **no cambia la complejidad algorítmica**.

- Fuerza bruta sigue siendo cuadrática y para procesar el doble de datos necesita aproximadamente cuatro veces más tiempo.
- Divide y vencerás mantiene un crecimiento mucho más controlado gracias a su mejor complejidad temporal.
- La ventaja de un algoritmo eficiente permanece incluso usando el mismo hardware.

La solución real consiste en mejorar el algoritmo, no únicamente la infraestructura.

En términos económicos y técnicos:

- Optimizar el algoritmo es una inversión única.
- Comprar infraestructura adicional implica costos recurrentes.

Por ello, la estrategia correcta es utilizar algoritmos con mejor complejidad temporal siempre que sea posible.