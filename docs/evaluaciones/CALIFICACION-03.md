# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Roberto Echeverri Arroyave · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `a78e467`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 18 / 25 |
| Calidad del análisis de las gráficas | 17 / 25 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque haya más casillas que guías, usando el ejemplo de 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica que la tabla hash no sirve para rangos y que el árbol sí.
- Estima la altura del árbol degenerado (unas 400.000) y la del equilibrado (unas 19), con el número aproximado de comparaciones.
- Declara que la proyección a 5.000.000 de envíos es una estimación y recomienda una combinación coherente.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la tabla hash a 5.000.000 de envíos dice que el tiempo sería "un poco más de un milisegundo", pero la cifra que da (1.141) está en microsegundos. Además no explica de dónde sale ese valor ni cómo cambia el tamaño de la tabla.
  → *Cómo corregirlo:* revise las unidades de su propia medición y explique con qué `m` y qué `α` esperaría ese tiempo con 5.000.000 de guías.
- Para la lista usa una proporción directa; la justificación de por qué la curva es lineal es muy breve.
  → *Cómo corregirlo:* apoye la forma de la curva en lo que usted observó entre dos valores de `n` de su gráfica.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista para una guía inexistente y el `Θ(1 + α)` de la tabla.
- Nombra el supuesto de hash uniforme simple y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista con costo `Θ(n)`.

## 3. Corrección de la implementación (18 / 25)
**Lo que hizo bien:**
- Las dos estructuras funcionan: búsquedas exitosas e infructuosas correctas, colisión forzada en la casilla 3 con lista de 3 nodos y `factor_carga` igual a 3/7.
- La tabla reutiliza `ListaEnlazada` y no usa `dict`, `set` ni `hash()`. La búsqueda en la lista es iterativa.
- Las pruebas cubren los casos pedidos, con veinte colecciones aleatorias, y todas pasan.

**Lo que puede mejorar (y cómo corregirlo):**
- Los *docstrings* de las funciones son de una sola línea: no tienen las secciones `Args` ni `Returns` que se pidió, ni en `estructuras.py` ni en `medicion.py`.
  → *Cómo corregirlo:* use el estilo Google de la plantilla del enunciado, con `Args:` y `Returns:` en cada función.
- Faltan *type hints* en el parámetro `estructura` de `tiempo_medio_busqueda` y en las funciones internas de `primo_cercano`.
  → *Cómo corregirlo:* agregue el tipo de cada parámetro y del valor que devuelve cada función.
- En las pruebas aleatorias la tabla siempre usa m = 7, así que no se prueba con otros tamaños.
  → *Cómo corregirlo:* varíe `m` en cada colección.

## 4. Calidad del análisis de las gráficas (17 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con las dos curvas en los mismos ejes y la segunda cinco valores de `α`.
- En la pregunta 2 calcula factores de crecimiento (6.59 en la lista y 0.91 en la tabla) y los contrasta con `Θ(n)` y `Θ(1)`.
- Describe que el tiempo crece al subir `α`, de forma coherente con `Θ(1 + α)`.

**Lo que puede mejorar (y cómo corregirlo):**
- Las gráficas no se ven en el informe: el `README.md` solo nombra los archivos, no los incrusta. Por eso lo que dice sobre ellas no se puede comprobar al leerlo.
  → *Cómo corregirlo:* inserte cada gráfica con `![Lista vs tabla](graficas/lista_vs_tabla.png)` y compruebe en la vista web de GitHub que se vean.
- Un factor de 6.59 frente a 5 esperado se atribuye a "ruido" sin más. Tampoco menciona que en la segunda gráfica el primer punto (α = 0.5) es más alto que el de α = 1.
  → *Cómo corregirlo:* repita la medición varias veces, indique si lo hizo y comente esos puntos que no siguen la tendencia.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- El informe tiene su nombre, las cinco respuestas de la Parte 3 y menciona cuántas búsquedas se midieron.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió la estructura de carpetas acordada: la carpeta se llama `laboratorios/Lab3-estructuras-datos/` (con mayúscula), en vez de `lab3-estructuras-datos/`. Se anota como incumplimiento de convención; no descuenta por sí sola.
- El informe no enlaza `estructuras.py`, `pruebas.py` ni `medicion.py` al inicio de las partes prácticas.
  → *Cómo corregirlo:* agregue enlaces Markdown con ruta relativa, por ejemplo `[estructuras.py](estructuras.py)`.
- Las instrucciones de reproducción no dicen cómo activar el entorno virtual, y el bloque de código quedó mal cerrado: el texto que sigue se ve dentro del bloque.
  → *Cómo corregirlo:* cierre el bloque con tres comilladas justo después de `python medicion.py` y agregue el comando de activación del entorno.
- El informe no indica el `m` usado para cada `n`, y no sigue el orden pedido (Parte 1, Parte 2 con gráficas, Parte 3).
  → *Cómo corregirlo:* titule las secciones "Parte 1", "Parte 2" y "Parte 3" y agregue una tabla con `n` y `m`.
- El laboratorio se subió en un solo commit; se piden al menos tres commits descriptivos.
  → *Cómo corregirlo:* haga un commit por cada avance (estructuras, pruebas, medición, informe) con mensajes que digan qué cambió.
- Se publicó la carpeta `__pycache__/`.
  → *Cómo corregirlo:* agréguela a `.gitignore`.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición se ejecuta completa y genera las dos gráficas. Las dos estructuras dan respuestas iguales en las búsquedas.
