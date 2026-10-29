# Laboratorio 03 — Estructuras de datos

**Estudiante:** Roberto Echeverri Arroyave  
**Asignatura:** Análisis de algoritmos

## Objetivo

Este proyecto compara el rendimiento de una lista enlazada y una tabla hash con encadenamiento para resolver las consultas de una empresa de mensajería. Se analiza el tiempo de búsqueda de guías de envío, el efecto del factor de carga y se determina cuál estructura conviene usar para consultas puntuales y para búsquedas por rango.

## Contenido del repositorio

- `estructuras.py`: implementación de `ListaEnlazada` y `TablaHash`.
- `pruebas.py`: script con `assert` para verificar que ambas estructuras funcionan y coinciden.
- `medicion.py`: experimento para medir los tiempos de búsqueda.
- `graficas/lista_vs_tabla.png`: gráfica comparativa de tiempos según el número de guías (n).
- `graficas/tiempo_vs_alfa.png`: gráfica del efecto del factor de carga.

## Cómo ejecutar el proyecto

Desde la carpeta del proyecto, ejecuta las pruebas y la medición:

```bash
python pruebas.py
python medicion.py
Las pruebas verifican búsquedas exitosas e inexistentes, la colisión forzada de las guías 10, 24 y 17 con m = 7, el cálculo del factor de carga y la consistencia en 20 colecciones aleatorias. La medición utiliza guías distintas de diez dígitos con semilla fija, prueba tamaños de 100, 500, 1000, 5000, 20000 y 50000, y mide 200 búsquedas inexistentes por cada tamaño con time.perf_counter().

```

## Implementación y verificación de las soluciones

Se implementaron dos estructuras:

Lista enlazada: cada guía se agrega al inicio. La inserción es inmediata, pero buscar una guía obliga a recorrer los nodos uno por uno.

Tabla hash: utiliza el método de la división h(k) = k mod m y resuelve las colisiones con encadenamiento. Cada casilla de la tabla reutiliza una lista enlazada para guardar las guías que caen en ella.

Las pruebas cubren la búsqueda exitosa y la búsqueda infructuosa en ambas estructuras. La colisión forzada se probó insertando las guías 10, 24 y 17 en una tabla de tamaño m = 7, verificando que las tres caen en la casilla 3 y que se pueden recuperar. Al final, la lista de esa casilla queda con tres nodos y el factor de carga da 3 / 7. También se generaron veinte colecciones aleatorias para comprobar que lista y tabla devuelven el mismo resultado, tanto para guías existentes como para guías que no están.

## Gráfica y análisis de rendimiento

La primera gráfica compara el tiempo medio de búsqueda de ambas estructuras al aumentar el número de guías. La lista enlazada muestra un crecimiento lineal: para n = 1000 tardó 55.533 µs y para n = 50000 tardó 4043.483 µs. La tabla hash se mantiene prácticamente plana: pasó de 0.661 µs con n = 1000 a 1.141 µs con n = 50000. Esto ocurre porque la lista recorre todos los nodos hasta encontrar la guía o llegar al final, mientras que la tabla calcula la casilla y recorre solo los elementos que hay en ella. Con n = 50000 la diferencia entre ambas es de más de 3500 veces.

La segunda gráfica muestra qué pasa con el tiempo de búsqueda cuando la tabla está más llena. Manteniendo n = 20000 y cambiando el número de casillas, el tiempo pasó de 0.833 µs con un factor de carga de 0.5 a 2.524 µs con un factor de carga de 8.0. El crecimiento es suave y casi lineal, lo que confirma que el costo de búsqueda depende del promedio de elementos por casilla.

Los tiempos dependen del computador y de las condiciones de ejecución. La gráfica muestra los resultados del experimento realizado; no permite afirmar un punto exacto de cruce entre las estructuras si ese punto no se midió directamente.

## Costo teórico

Buscar una guía inexistente en la lista enlazada cuesta Θ(n). No hay forma de saber que la guía no está hasta haber revisado todos los nodos.

En la tabla hash con encadenamiento, calcular h(k) cuesta tiempo constante, y después solo se recorre la lista de esa casilla. Si las claves están bien repartidas, esa lista mide en promedio α = n/m, así que el costo esperado es Θ(1 + α). Este resultado se apoya en el supuesto de hash uniforme simple: se asume que cada clave tiene la misma probabilidad de caer en cualquier casilla y que no depende de las demás. Si ese supuesto no se cumple y todas las guías cayeran en la misma casilla, la tabla se volvería una sola lista y buscar costaría Θ(n), igual que la lista original.

## Lo medido contra lo esperado

Al pasar de n = 1000 a n = 5000, el tiempo de la lista se multiplicó por 6.59 (366.110 µs / 55.533 µs). Esto se acerca a lo que se espera de Θ(n), pues 5000 / 1000 = 5. La variación se debe al ruido normal de la máquina. En cambio, el tiempo de la tabla se multiplicó por 0.91 (incluso bajó un poco), confirmando que se mantiene constante mientras el factor de carga está acotado.

En la segunda gráfica, al subir el factor de carga de 0.5 a 8.0, el tiempo pasó de 0.833 µs a 2.524 µs. El crecimiento es coherente con Θ(1 + α), porque a mayor carga hay más elementos por casilla y la búsqueda tarda más.

## Colisiones

Una colisión ocurre cuando dos claves distintas producen el mismo índice al aplicar la función hash. Sucede aunque haya más casillas que guías porque la función comprime un espacio enorme de claves posibles en solo m casillas. Con m = 7, las guías 10, 24 y 17 dan 10 mod 7 = 3, 24 mod 7 = 3 y 17 mod 7 = 3, por lo que las tres comparten la casilla 3.

El encadenamiento resuelve esto guardando una lista en cada casilla. No se pierde ningún dato y borrar es sencillo, pero los nodos extra ocupan memoria y las cadenas se alargan si el factor de carga crece. El direccionamiento abierto, en cambio, guarda todo dentro del arreglo y busca otra casilla libre cuando hay colisión. Ahorra memoria, pero genera agrupamientos y exige dejar marcas al borrar para no romper la secuencia de búsqueda. Además, el factor de carga debe mantenerse menor que 1.

## Tabla hash o árbol de búsqueda

La tabla hash no sirve para el monitoreo por rango. Como no guarda orden, pedir las guías entre X e Y obligaría a revisar todas las casillas. Un árbol de búsqueda binario sí lo resuelve, porque el recorrido en orden devuelve las claves ordenadas y un rango se obtiene en Θ(h + k), donde k es la cantidad de resultados.

Si las 400.000 guías llegaran ya ordenadas y se insertaran una a una, cada nueva sería mayor que todas las anteriores y se colgaría siempre a la derecha. El árbol quedaría como una lista de altura h ≈ 400.000. Insertar todas costaría alrededor de n²/2 ≈ 8·10¹⁰ comparaciones. Si el árbol estuviera equilibrado, la altura sería log₂(400000) ≈ 19 y la construcción costaría del orden de n log₂ n ≈ 7,6·10⁶ comparaciones, muchísimo menos.

## Estimación para 5.000.000 de envíos

Esta proyección usa los tiempos medidos para 50000 guías. Es una estimación, no una medición directa para cinco millones.

Lista enlazada: Como el tiempo crece de forma lineal (Θ(n)), se multiplica el tiempo medido por la proporción entre los tamaños. Con n = 50000 tardó 4043.483 µs. Para 5.000.000 de guías:

4043.483 µs × (5.000.000 / 50.000) = 404.348.300 µs

Esto equivale aproximadamente a 404 segundos, es decir, unos 6.7 minutos por búsqueda inexistente.

Tabla hash: Como el tiempo se mantiene constante mientras se ajuste el tamaño de la tabla para que el factor de carga no crezca, el tiempo debería seguir en el orden de 1.141 µs (un poco más de un milisegundo).

Estas cifras son aproximadas. El tiempo real puede cambiar según el computador y la implementación.

## Recomendación para la jefa de operaciones

Recomiendo usar una combinación de las dos estructuras. Una tabla hash para las consultas puntuales del call center, porque con cinco millones de envíos seguiría respondiendo en cerca de un milisegundo, mientras que la lista enlazada tardaría varios minutos y haría que los clientes siguieran colgando. Y un árbol de búsqueda binario (idealmente balanceado) para el monitoreo por rango, porque permite obtener las guías entre dos números sin tener que revisar toda la colección.
