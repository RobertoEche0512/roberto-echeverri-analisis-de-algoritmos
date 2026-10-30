# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Roberto Echeverri Arroyave · **Laboratorio:** Dividir y vencer (subarreglo máximo)
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `8738269`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 13 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 9 / 25 |
| Documentación y organización del informe | 2 / 10 |
| **Total** | **62 / 100** |
| **Nota (0–5)** | **3.10** |

**Incumplimientos de convención:** No siguió la estructura de carpetas acordada. El trabajo vigente está en `laboratorios/Corrección lab-2-divide-y- vencer/`, una carpeta con un nombre distinto al pedido (`lab2-divide-y-vencer/`). Además, la carpeta correcta `laboratorios/lab2-divide-y-vencer/` sigue en el repositorio con una versión anterior y distinta del trabajo (con `Pruebas.py` en mayúscula), así que el laboratorio quedó duplicado. Se evaluó el contenido de la carpeta "Corrección".

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Compara con el máximo de un arreglo: explica que combinar cuesta solo `Θ(1)`, que la recurrencia es `T(n) = 2T(n/2) + Θ(1)` y que da `Θ(n)`, frente al `Θ(n)` de combinar en el subarreglo máximo. Es una justificación correcta.
- Recomienda divide y vencerás para la cooperativa y estima el tiempo con un millón de registros (cerca de 3,17 s contra unas 7,47 horas), declarando que es una estimación y no una regla de tres lineal.
- En tamaños pequeños explica bien por qué divide y vencerás pierde ventaja (llamadas recursivas y combinación).

**Lo que puede mejorar (y cómo corregirlo):**
- No dice a partir de qué tamaño divide y vencerás empieza a ganar; afirma que sus mediciones no permiten establecerlo, pero su propia gráfica y tabla sí cubren tamaños pequeños.
  → *Cómo corregirlo:* mire en sus datos los tamaños pequeños (por ejemplo, con una tabla de valores medidos) y señale entre cuáles dos tamaños cambia cuál algoritmo es más rápido.

## 2. Calidad de la explicación teórica (13 / 20)
**Lo que hizo bien:**
- Plantea la recurrencia `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada parte: dos subproblemas, tamaño `n/2` y costo lineal de la parte cruzada.
- Indica que el resultado es `Θ(n log n)` y que la fuerza bruta es `Θ(n²)` porque revisa todas las parejas de inicio y fin.

**Lo que puede mejorar (y cómo corregirlo):**
- Dice "al resolverla se obtiene `Θ(n log n)`" sin mostrar el método maestro: no identifica los valores de `a`, `b` y `f(n)` ni comprueba la condición del caso que aplica.
  → *Cómo corregirlo:* escriba qué valen `a`, `b` y `f(n)`, compare `f(n)` con `n^(log_b a)` y diga qué caso del método maestro se cumple y por qué.
- La explicación del `Θ(n²)` de la fuerza bruta es muy breve.
  → *Cómo corregirlo:* cuente cuántas parejas (inicio, fin) se revisan en total y cuánto cuesta cada una cuando la suma se va acumulando.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días, un solo elemento, valores todos negativos, todos positivos y un caso que cruza el punto medio.
- `subarreglo_maximo` resuelve los tres casos y no usa la fuerza bruta. Ninguna función modifica la lista recibida.
- `pruebas.py` incluye veinte listas aleatorias con semilla fija, comparando ambos algoritmos.
- Las funciones de `subarreglo.py` y `pruebas.py` tienen *docstrings* con `Args` y `Returns` y *type hints*.

**Lo que puede mejorar (y cómo corregirlo):**
- En `subarreglo.py` hay solo una línea en blanco antes de la primera función, en vez de dos.
  → *Cómo corregirlo:* deje dos líneas en blanco entre el *docstring* del módulo y la primera función.
- En `medicion.py`, `medir_tiempo` no indica el tipo de `funcion` ni de `argumentos`.
  → *Cómo corregirlo:* anote `funcion` con `Callable` (del módulo `typing`) y los argumentos con `*argumentos: object`.

## 4. Calidad del análisis de las gráficas (9 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` existe y es clara: ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con diez tamaños (de 10 a 5000).
- `medicion.py` usa semilla fija, la misma lista para los dos algoritmos, `time.perf_counter()` solo sobre el algoritmo y comprueba que las sumas coinciden.

**Lo que puede mejorar (y cómo corregirlo):**
- La gráfica no aparece en el informe: en la sección de la gráfica solo hay el texto "Gráfica comparativa de tiempos", sin la imagen.
  → *Cómo corregirlo:* incruste la imagen con `![Tiempo vs n](graficas/tiempo_vs_n.png)`.
- El informe no calcula cuánto se multiplica el tiempo de cada algoritmo al duplicar `n`, ni lo compara con lo que predicen `Θ(n²)` y `Θ(n log n)`.
  → *Cómo corregirlo:* elija dos tamaños consecutivos donde `n` se duplique, divida los tiempos de cada algoritmo y diga si el resultado se parece a lo esperado en cada caso.
- Las afirmaciones sobre el desempeño son genéricas ("se espera que...", "debería ser más eficiente") y no citan valores leídos de la gráfica. La estimación a un millón sí usa un valor medido (0,672 s con 5000 elementos, coherente con la gráfica), pero el informe nunca describe qué hace cada curva al crecer `n`.
  → *Cómo corregirlo:* describa con valores de su gráfica (o de una tabla) cómo cambia cada curva entre un tamaño pequeño, uno mediano y 5000.
- El informe no menciona si repitió las mediciones.
  → *Cómo corregirlo:* agregue una nota sobre cómo midió (una sola vez o varias, y qué valor graficó).

## 5. Documentación y organización del informe (2 / 10)
**Lo que hizo bien:**
- El informe trae su nombre completo y explica el objetivo y el contenido de la carpeta.

**Lo que puede mejorar (y cómo corregirlo):**
- Carpeta con nombre distinto a la convención y laboratorio duplicado (ver arriba).
  → *Cómo corregirlo:* deje una sola carpeta llamada `lab2-divide-y-vencer/` con los archivos del entregable (por ejemplo, con `git mv`) y elimine la copia anterior.
- El informe no enlaza el código de cada parte: solo nombra los archivos entre comillas.
  → *Cómo corregirlo:* al inicio de la Parte 1 enlace `subarreglo.py` y `pruebas.py`, y al inicio de la Parte 2 enlace `medicion.py`, con enlaces de Markdown como `[subarreglo.py](subarreglo.py)`.
- No sigue el orden pedido (reproducción, Parte 1, Parte 2, Parte 3) ni numera las cinco preguntas; la parte de verificación no cubre cada caso probado.
  → *Cómo corregirlo:* organice el informe con esos cuatro bloques y responda las cinco preguntas en el orden de la guía.
- Las instrucciones de reproducción no explican cómo activar el entorno, y hay frases sueltas ("Desde la carpeta del proyecto, ejecuta las pruebas:" sin comando).
  → *Cómo corregirlo:* indique cómo activar el entorno virtual e instalar `requirements.txt`, y ponga cada comando justo después de la frase que lo introduce.
- El laboratorio tiene solo dos commits con mensaje "Add files via upload", que no describen el cambio; se piden al menos tres descriptivos.
  → *Cómo corregirlo:* haga commits pequeños y frecuentes con mensajes que digan qué se hizo, por ejemplo "Agrega suma_cruzada y sus pruebas".

## ¿El código funciona?
Sí. Las pruebas pasan y ambos algoritmos dan la misma suma máxima en todos los casos. La medición corre sin errores y genera la gráfica en `graficas/`.
