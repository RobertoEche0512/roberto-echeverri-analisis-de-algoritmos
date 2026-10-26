# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Roberto Echeverri · **Laboratorio:** Dividir y vencer (subarreglo máximo)
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `b1f1029`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 8 / 20 |
| Calidad de la explicación teórica | 11 / 20 |
| Corrección de la implementación | 15 / 25 |
| Calidad del análisis de las gráficas | 9 / 25 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **46 / 100** |
| **Nota (0–5)** | **2.30** |

## 1. Corrección conceptual (8 / 20)
**Lo que hizo bien:**
- Explica que dividir el problema del máximo de un arreglo no mejora nada, mientras que aquí sí mejora.
- Entiende que la fuerza bruta se vuelve inviable con muchos datos.

**Lo que puede mejorar (y cómo corregirlo):**
- Las preguntas del informe no son las cinco que pedía el laboratorio. No responde cuál es el tamaño desde el cual divide y vencerás gana, apoyado en sus datos.
  → *Cómo corregirlo:* copie las cinco preguntas del enunciado como títulos del informe y conteste cada una debajo. Para el tamaño de cruce, mire en su tabla de tiempos desde qué `n` la columna de divide y vencerás pasa a ser la menor y se mantiene así.
- La comparación con hallar el máximo de un arreglo es de una sola frase: falta el costo de combinar y la recurrencia de ese problema.
  → *Cómo corregirlo:* escriba la recurrencia de ese problema (cuántos subproblemas, de qué tamaño, cuánto cuesta combinar las dos mitades) y compare el costo de combinar con el del subarreglo máximo.
- Falta la recomendación para la cooperativa con una estimación para 1.000.000 de registros, declarada como estimación. Estimó para 100.000, pero sin recomendar.
  → *Cómo corregirlo:* parta de un tiempo medido, multiplíquelo por el factor que predice cada `Θ` al pasar a 1.000.000, diga que es una estimación y cierre con cuál algoritmo recomienda y por qué.

## 2. Calidad de la explicación teórica (11 / 20)
**Lo que hizo bien:**
- Plantea bien `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término (2 subproblemas, tamaño n/2, costo del caso cruzado).
- Llega al resultado correcto `Θ(n log n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- Nombra el teorema maestro pero no muestra la condición del caso que aplica ni cómo se verifica.
  → *Cómo corregirlo:* identifique `a`, `b` y `f(n)` de su recurrencia, calcule `n^(log_b a)`, compárelo con `f(n)` y diga explícitamente qué caso se cumple y por qué.
- No explica por qué la fuerza bruta es `Θ(n²)` (cuántos pares de días se revisan).
  → *Cómo corregirlo:* cuente cuántos pares (inicio, fin) revisan sus dos ciclos y exprese esa cantidad como una suma; de ahí sale el orden de crecimiento.

## 3. Corrección de la implementación (15 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos: la serie de ocho días da 17 y coinciden con la fuerza bruta en listas aleatorias que probé.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista.
- Hay pruebas con `assert` para la serie de ocho días, un elemento, todos negativos y todos positivos.

**Lo que puede mejorar (y cómo corregirlo):**
- Faltan las veinte listas aleatorias en las pruebas y un caso cruzado explícito.
  → *Cómo corregirlo:* en `pruebas.py` haga un ciclo de 20 listas aleatorias que compare la suma de ambos algoritmos con `assert`, y agregue una lista pequeña escrita a mano en la que el mejor tramo cruce la mitad.
- Los docstrings no siguen el formato pedido (con Args y Returns); las funciones de `medicion.py` no tienen indicaciones de tipo.
  → *Cómo corregirlo:* a cada función agréguele un docstring con las secciones `Args:` y `Returns:`, y escriba los tipos en la firma (por ejemplo `lista: list[int]` y `-> int`).

## 4. Calidad del análisis de las gráficas (9 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Usó la misma lista para ambos algoritmos.

**Lo que puede mejorar (y cómo corregirlo):**
- No calculó cuánto se multiplica el tiempo al duplicar n ni lo contrastó con `Θ(n²)` y `Θ(n log n)`.
  → *Cómo corregirlo:* para cada par de tamaños donde `n` se duplica, divida `t(2n)` entre `t(n)`, ponga los cocientes en una tabla y compárelos con lo que predice cada orden de crecimiento.
- Dice que en n = 1600 divide y vencerás es unas 90 veces más rápido, pero en la gráfica publicada se lee cerca de 0.054 s contra 0.0026 s, unas 20 veces.
  → *Cómo corregirlo:* calcule la razón directamente de los números de su tabla o gráfica final y escriba solo esa cifra; revise que el texto se actualice cada vez que repita la medición.
- Solo hay un tamaño menor de 100 (50) y el mayor es 1600; se pedían dos menores de 100 y uno de 4000 o más.
  → *Cómo corregirlo:* agregue a la lista de tamaños uno más pequeño (por ejemplo, 10 o 25) y uno de 4000 o más. Si la fuerza bruta tarda demasiado, repita menos veces solo ese tamaño.
- Cronometró con `time.time()` en vez de `time.perf_counter()`.
  → *Cómo corregirlo:* cambie las llamadas a `time.perf_counter()`, que tiene mejor resolución para tiempos cortos.
- No usó semilla fija (los datos cambian en cada corrida) ni valores enteros entre -100 y 100, y no verificó que ambas sumas coincidan dentro de la medición.
  → *Cómo corregirlo:* fije la semilla con `random.seed(...)` al inicio, genere los datos con `random.randint(-100, 100)` y, en cada tamaño, compare con `assert` las sumas de ambos algoritmos.

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- El informe trae su nombre, instrucciones para reproducir y el orden general de partes.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió la convención de nombres: el archivo de pruebas se llama `Pruebas.py` (el entregable pide `pruebas.py`); el informe manda ejecutar `pruebas.py`, que en GitHub o Linux no existe.
  → *Cómo corregirlo:* renombre el archivo a `pruebas.py` con `git mv` (así Git registra el cambio de mayúsculas) y revise que las instrucciones del informe usen ese nombre.
- La gráfica no se ve en el informe: está escrita como texto con otro nombre (`comparacion_subarreglo.png`) que no existe, y no usa la sintaxis de imagen.
  → *Cómo corregirlo:* use la sintaxis de imagen de Markdown con la ruta real de su archivo, `graficas/tiempo_vs_n.png`, y compruebe en GitHub que se vea.
- Los archivos de código se nombran pero no están enlazados.
  → *Cómo corregirlo:* escriba cada nombre como enlace relativo, por ejemplo `[subarreglo.py](subarreglo.py)`.
- Hay un solo commit ("Add files via upload") para el laboratorio; se pedían al menos tres, descriptivos.
  → *Cómo corregirlo:* trabaje desde su computador con `git add`, `git commit` y `git push` y haga un commit por etapa (algoritmos, mediciones, informe) con un mensaje que diga qué cambió.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma y `medicion.py` corre y genera la gráfica. Lo que falla es el cumplimiento de los requisitos de la medición y del informe.
