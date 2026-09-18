# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Estudiante:** Roberto Echeverri Arroyave  
**Curso:** Algoritmos y estructuras de datos  

## Instrucciones para reproducir el experimento

1. Active el entorno virtual desde la raíz del repositorio escribiendo en la terminal:

    venv\Scripts\activate

   Si está dentro de la carpeta del laboratorio:

    ..\..\venv\Scripts\activate

### Ejecutar Parte 3

python parte3_casos.py

### Ejecutar Parte 4

python parte4_complejidad.py

### Parte 1 — Analizar el algoritmo antes de comprar hardware

La Secretaría de Salud va a firmar la compra de un servidor con el doble de velocidad de reloj, para que el proceso nocturno de Tamiza, ordenar 1.200.000 registros de riesgo cardiovascular, quepa en la ventana de 2:00 a 6:00 a.m. Antes de firmar, conviene mirar el algoritmo. El que está en producción lleva ocho años dando el resultado correcto.

Pero que algo entregue bien el resultado no significa que alcance a entregarlo a tiempo. Hay que separar dos cosas. Una es que el algoritmo produzca la salida esperada para toda entrada válida: una lista ordenada de mayor a menor por índice de riesgo, sin perder registros. Insertion sort cumple esa parte; la invariante de ciclo lo respalda. Otra cosa es que lo haga dentro de las cuatro horas. Ahí no hablamos de si acierta, sino de cuánto tiempo de cómputo consume frente al límite de cuatro horas que impone la ventana nocturna. Frente a esa restricción, el algoritmo no da abasto.

Tamiza no termina antes de las 6:00 a.m. El centro de contacto arranca el día con una lista parcial o mal ordenada. Eso es lo que hay que resolver, no el hecho de que el algoritmo "esté mal", porque no lo está.

Duplicar la velocidad del servidor reduce el tiempo a la mitad. Suena bien hasta que uno mira cómo crece el algoritmo. Si el trabajo crece con el cuadrado del tamaño de la entrada, como pasa con insertion sort en el peor caso y en el promedio, la situación se complica. Cuando el programa pasó de 20.000 a 1.200.000 registros, un factor de 60, el tiempo se multiplicó por un factor cercano a 3.600. Partir eso por la mitad no lo mete en la ventana. Y el volumen seguirá subiendo: más laboratorios, más pruebas. El mismo algoritmo volverá a desbordar el servidor nuevo.

Un caso parecido ocurre en un sistema de facturación de un consultorio médico. Cada noche procesa los 8.000 movimientos del día (consultas, procedimientos, pagos parciales) para armar el estado de cuenta de cada paciente antes de las 7:00 a.m., cuando abre la recepción. Usaron búsqueda lineal para cruzar cada movimiento con la lista de pacientes, unas 15.000 historias clínicas. El algoritmo está bien: encuentra al paciente o dice que no existe. Pero con 8.000 movimientos contra 15.000 pacientes, el cruce supera tres horas. La recepción abre sin los estados de cuenta al día.

Otra vez, el problema no es de acierto sino de tiempo de ejecución frente a la ventana nocturna. Duplicar el hardware bajaría el tiempo a la mitad, pero el número de movimientos crece cada año. Un índice o una estructura de búsqueda logarítmica ataca el problema de raíz.

En el fondo, es lo mismo en los dos casos: que algo funcione no significa que aguante. Revisar el algoritmo primero permite saber si el cuello de botella está en el diseño o en la capacidad del equipo. Así se evita gastar en hardware que solo retrasa el próximo colapso.

### Parte 2 — Responsabilidad ambiental y ética de la implementación

Como responsable técnico de Tamiza, la decisión de qué algoritmo de ordenamiento se ejecuta cada madrugada sobre 1.200.000 registros de pacientes implica dos dimensiones de responsabilidad que no se agotan en "que el código funcione".

Dimensión ambiental. El servidor que ejecuta el proceso nocturno consume energía mientras corre. Si el proceso tarda, por ejemplo, 6 horas en lugar de 30 minutos, el consumo eléctrico de esa noche es aproximadamente doce veces mayor. Como el proceso se repite todas las madrugadas durante años, la diferencia se acumula en miles de kilovatios-hora. Esa energía la paga la Secretaría (o el operador del centro de datos) y la genera el sistema eléctrico, con su huella de emisiones. Cambiar de un algoritmo cuadrático a uno de crecimiento 
n
log
⁡
n
nlogn no solo reduce el tiempo de ejecución, reduce de forma permanente el consumo energético asociado a una operación que no se detiene nunca. La decisión de diseño tomada en una tarde se convierte, con el tiempo, en una cifra ambiental medible.

Dimensión ética. La lentitud o el fallo del algoritmo perjudica a personas identificables de al menos dos maneras concretas.

Paciente con alto riesgo que no es contactado a tiempo. Si el proceso no termina antes de las 6:00 a.m., el centro de contacto trabaja con una lista incompleta o no ordenada. Un paciente cuyo índice de riesgo lo ubicaría en los primeros lugares de la lista puede quedar fuera de la lista del día o ser llamado mucho después. El costo del error lo asume el paciente: pierde la oportunidad de una valoración médica oportuna y, en el peor caso, sufre un evento cardiovascular que podría haberse prevenido o mitigado. La Secretaría y el equipo de desarrollo también cargan con la responsabilidad institucional, pero el daño directo recae sobre la persona cuyo dato de riesgo no fue priorizado.

Operador del centro de contacto y paciente que recibe una llamada fuera de orden. Cuando la lista llega desordenada, el operador llama según el orden que tenga parcial o aleatorio. Un paciente de riesgo bajo puede ser contactado antes que uno de riesgo alto. El operador asume el costo de gestionar quejas o de reorganizar su trabajo; el paciente de alto riesgo asume el costo de la demora. De nuevo, el algoritmo cometió el error de no entregar la prioridad correcta, pero quien lo paga es quien espera la llamada o quien debe explicar por qué no fue priorizado.

Además, el orden de la lista decide a quién se llama primero. Esa decisión no es un detalle de implementación: es una asignación de prioridad médica. Por tanto, la corrección del ordenamiento (producir realmente el orden de mayor a menor riesgo) tiene una obligación adicional que va más allá del tiempo de ejecución. Un algoritmo que a veces intercambia dos registros de riesgo cercano, o que deja la lista parcialmente ordenada, no solo incumple una especificación técnica: altera quién recibe atención prioritaria. Esa responsabilidad no se puede delegar al hardware ni al algoritmo que ya estaba probado hace ocho años. Quien elige el algoritmo elige, cada madrugada, el orden en que se asigna la capacidad limitada del centro de contacto.

### Parte 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

Código de esta parte: parte3_casos.py

Algoritmo instrumentado: [algoritmos.py](algoritmos.py)

Generadores de escenarios: [datos.py](datos.py)

### 3.1 Explicación

Para un algoritmo de ordenamiento que recibe una secuencia de n elementos, los tres casos se definen sobre el conjunto de todas las entradas de tamaño fijo n:

Peor caso: el máximo, sobre todas las entradas de tamaño n, del número de operaciones básicas (o del tiempo) que realiza el algoritmo. Es la cota superior que garantiza el desempeño incluso en la entrada más adversa.
Mejor caso: el mínimo, sobre todas las entradas de tamaño n, del número de operaciones básicas. Es el desempeño cuando la entrada ya está “casi lista” para el algoritmo.
Caso promedio: el promedio, asumiendo una distribución de probabilidad sobre las entradas de tamaño n (habitualmente la distribución uniforme sobre las permutaciones), del número de operaciones básicas.

Para decidir si el algoritmo de Tamiza entra en producción, sabiendo que la ventana de cuatro horas es estricta, usaría el peor caso. La ventana no admite excepciones: si una noche los datos llegan en el orden más desfavorable y el proceso no termina, el centro de contacto trabaja con una lista incompleta. El caso promedio o el mejor caso pueden ser optimistas; el peor caso es la garantía que el sistema necesita.
Predicción antes de medir (ordenamiento de mayor a menor):

Escenario A (aleatorio) → se aproxima al caso promedio.

Escenario B (casi ordenado: 98 % ya en el orden correcto + 2 % desordenado al final) → mejor caso.

Escenario C (orden inverso: ascendente cuando se desea descendente) → peor caso.

### 3.2 Demostración experimental

Se midió insertion sort sobre los tres escenarios para los tamaños n = 100, 200, 400, 800, 1600, 3200, 6400$. Cada medición es el promedio de tres corridas. Se registraron tiempo de ejecución (time.perf_counter) y número de comparaciones entre elementos.

Resultados observados (n = 6400):

Escenario A(aleatorio), comparación: ≈ 10.210.599, tiempo(s):≈ 0,74

Escenario B(casi ordenado), comparación: ≈ 10.367, tiempo(s):≈ 0,0008

Escenario C(inverso), comparación: ≈ 20.476.800, tiempo(s):≈ 1,48

Peor caso: escenario C (inverso). Coincide con la predicción.

Mejor caso: escenario B (casi ordenado). Coincide con la predicción.

Caso promedio (aproximado): escenario A (aleatorio). Coincide con la predicción.

La predicción de 3.1 se confirma: el número de comparaciones en el peor caso es del orden de n^2/2, en el mejor caso del orden de n, y en el aleatorio intermedio (del orden de n^2/4).

### Gráfica de comparaciones

graficas/parte3_comparaciones.png

### Gráfica de tiempos

graficas/parte3_tiempo.png

### Parte 4 — Complejidad de merge sort e insertion sort: cálculo y validación

Código de esta parte: parte4_complejidad.py

### 4.1 Cálculo teórico

Recurrencia de merge sort
Merge sort divide el problema de tamaño nnn en dos subproblemas de tamaño n/2 (dividir), resuelve cada uno recursivamente (conquistar) y luego combina las dos mitades ordenadas en tiempo lineal (combinar). Por tanto:

T(n)=2T(n/2)+Θ(n)

2: número de subproblemas.

n/2: tamaño de cada subproblema.

Θ(n): costo de la mezcla (recorrer las dos mitades una sola vez).

Resolución por el método maestro

Identificamos a = 2, b = 2, f(n) = Θ(n)

Calculamos n^{\log_b a} = n^{\log_2 2} = n^1 = n

Comparamos f(n) con n^{\log_b a}: f(n) = Θ(n) = Θ(n)(n^{\log_b a})

Se cumple la condición del caso 2 del método maestro (cuando f(n) = Θ(n)(n^{\log_b a})):

T(n) = Θ(n^{\log_b a} \log n) = Θ(n \log n)

Complejidad de insertion sort (análisis línea a línea)
Implementación (orden descendente):

for i in range(1, n):          # se ejecuta n-1 veces

    clave = arreglo[i]         # Θ(1) por iteración → Θ(n)

    j = i - 1                  # Θ(1) por iteración → Θ(n)

    while j >= 0 and ...:      # el cuerpo se ejecuta un número de veces que depende de la entrada

        comparaciones += 1
        if arreglo[j] < clave:
            arreglo[j+1] = arreglo[j]
            j -= 1
        else:
            break
    arreglo[j+1] = clave       # Θ(1) por iteración → Θ(n)

Mejor caso (entrada ya ordenada de mayor a menor): el while hace exactamente una comparación por cada i y sale.

Peor caso (entrada en orden inverso): para cada $i$, el while recorre los $i$ elementos anteriores.

Caso promedio (permutación aleatoria): el elemento se inserta, en promedio, a mitad de camino.

Tabla de complejidades esperadas

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---|---|---|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ |
| Merge sort | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ |

### 4.2 Validación experimental

Se midió el tiempo de ejecución de ambos algoritmos sobre el escenario A (aleatorio) para los mismos tamaños de la Parte 3. Cada punto es el promedio de tres corridas.

Lectura de la gráfica:

Para n pequeños (100–200) ambos algoritmos tienen tiempos del mismo orden de magnitud; a veces insertion sort es ligeramente más rápido por las constantes menores (no crea listas auxiliares ni realiza llamadas recursivas). A partir de n \approx 400 la curva de insertion sort crece de forma cuadrática y se separa claramente. En n = 6400 merge sort es aproximadamente 60 veces más rápido (0,012 s frente a 0,73 s). La forma de las curvas coincide con las complejidades calculadas en 4.1: n^2 frente a n log n.

Comparación de tiempos

graficas/parte4_tiempo.png

La conclusión experimental es que merge sort es mejor para Tamiza.

### 4.3 Concepto técnico a la Secretaría de Salud

Recomendación sobre el algoritmo de ordenamiento del proceso nocturno de Tamiza y la propuesta de duplicar la capacidad del servidor.

El proceso de Tamiza debe ordenar cada madrugada aproximadamente 1.200.000 registros de índice de riesgo en una ventana estricta de cuatro horas (2:00–6:00 a.m.). El algoritmo actual, insertion sort, produce resultados correctos, pero su tiempo de ejecución crece de forma cuadrática. En las mediciones realizadas, con 6.400 registros aleatorios tardó aproximadamente 0,73 segundos, mientras que merge sort tardó 0,012 segundos.

Recomendación del algoritmo

Debido a que los datos pueden llegar aleatorios, casi ordenados o en orden inverso, se recomienda utilizar un solo algoritmo: merge sort. Su complejidad es Θ(n log n) en todos los casos y, por tanto, no depende de la forma en que lleguen los datos.

Insertion sort puede ser eficiente cuando la entrada está casi ordenada, pero esta condición no puede garantizarse permanentemente. Para un proceso con una ventana de tiempo estricta, resulta más conveniente utilizar un algoritmo cuyo comportamiento sea predecible.

Estimación para 1.200.000 registros

La siguiente estimación se basa en las mediciones realizadas y no constituye una medición directa.

Para insertion sort, si el tiempo crece aproximadamente como n², pasar de 6.400 a 1.200.000 registros representa un factor de 187,5. Al elevarlo al cuadrado, el tiempo aumenta aproximadamente 35.156 veces. Por tanto:

0,73 × 35.156 ≈ 25.700 segundos ≈ 7,1 horas

Esto supera la ventana disponible de cuatro horas.

Para merge sort, el crecimiento es n log n. Con los mismos datos, el factor aproximado es:

187,5 × (20,2 / 12,6) ≈ 300

Por tanto:

0,012 × 300 ≈ 3,6 segundos

Incluso considerando un margen adicional por otras tareas del proceso, el ordenamiento estaría ampliamente dentro de la ventana establecida.

Sobre duplicar la velocidad del servidor

Duplicar aproximadamente la velocidad de procesamiento podría reducir los tiempos cerca de la mitad. En el caso estimado de insertion sort, 7,1 horas / 2 ≈ 3,5 horas, pero esto dejaría un margen muy pequeño y no garantizaría el cumplimiento de la ventana en escenarios desfavorables.

Además, el crecimiento cuadrático significa que futuros aumentos en el volumen de datos volverían a generar el mismo problema. Por ello, mejorar el hardware puede retrasar la dificultad, pero no modifica el comportamiento del algoritmo.

Consideración de memoria

Merge sort requiere espacio auxiliar O(n) para realizar las operaciones de mezcla. Para 1.200.000 registros, este consumo adicional debe considerarse, aunque normalmente resulta manejable en un servidor con recursos adecuados. Si la memoria fuera el principal recurso limitado, podrían evaluarse alternativas como heapsort.

Conclusión

Se recomienda migrar el proceso a merge sort, mantener un único algoritmo independiente del orden de llegada de los datos y no utilizar la compra de un servidor de doble velocidad como solución principal. El cambio de algoritmo aborda directamente el problema de complejidad y ofrece un margen mucho mayor para cumplir la ventana de cuatro horas.
