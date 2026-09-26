# Tarea 3 - Grafos en LeetCode

## 547. Number of Provinces

**Problema:**
https://leetcode.com/problems/number-of-provinces/

### Modelo

El problema se representa como un **grafo no dirigido**.

* **Vértices:** cada ciudad.
* **Aristas:** una conexión directa entre dos ciudades cuando `isConnected[i][j] == 1`.
* **Provincia:** corresponde a una componente conexa del grafo.

### Algoritmo

Se utilizó **DFS (Depth-First Search)**.

Se recorren todas las ciudades. Cuando se encuentra una ciudad que todavía no ha sido visitada, se cuenta una nueva provincia y se ejecuta DFS para marcar todas las ciudades conectadas directa o indirectamente con ella.

### Complejidad

* **Tiempo:** `O(n²)`, porque la entrada es una matriz `n × n` y se deben recorrer sus posiciones.
* **Espacio:** `O(n)`, debido al arreglo `visited` y a la pila de llamadas del DFS.

### Código

[Ver código](number-of-provinces/solution.py)

### Evidencia de Accepted

![Accepted - Number of Provinces](evidencias/number-of-provinces-accepted.png)

## 207. Course Schedule

**Problema:**
https://leetcode.com/problems/course-schedule/

### Modelo

El problema se representa como un **grafo dirigido**.

* **Vértices:** cada curso.
* **Aristas:** si `[a, b]` aparece en `prerequisites`, se representa como `b → a`.
* Esto significa que el curso `b` debe realizarse antes que el curso `a`.

### Algoritmo

Se utilizó **Kahn mediante BFS y orden topológico**.

Primero se construye la lista de adyacencia y se calcula el grado de entrada de cada curso. Los cursos que tienen grado de entrada `0` se agregan a una cola.

Después se procesan los cursos de la cola y se reducen los grados de entrada de los cursos siguientes. Si todos los cursos pueden ser procesados, no existe un ciclo y es posible terminar todos los cursos. Si quedan cursos sin procesar, significa que existe un ciclo de prerrequisitos.

### Complejidad

* **Tiempo:** `O(n + m)`.
* **Espacio:** `O(n + m)`.

Donde `n` es el número de cursos y `m` es el número de prerrequisitos.

### Código

[Ver código](course-schedule/solution.py)

### Evidencia de Accepted

![Accepted - Course Schedule](evidencias/course-schedule-accepted.png)
