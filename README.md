# Reto-algoritmo

https://github.com/Tomas-Dorado/Reto-algoritmo.git

---

### README - Carpeta `Caballos`

---

#### **Descripción del Proyecto**
La carpeta `Caballos` contiene una implementación algorítmica para resolver el problema de contar las secuencias válidas de movimientos de un caballo en un teclado numérico. Este problema se basa en las reglas del movimiento del caballo en el ajedrez, donde el caballo puede moverse en forma de "L". El objetivo es calcular cuántas secuencias válidas de longitud `n` se pueden formar comenzando desde cualquier número del teclado.

El módulo incluye una funcionalidad para calcular y mostrar los resultados de estas secuencias para una lista específica de movimientos.

---

#### **Archivos Principales**
- **`lanzador.py`**: Archivo que ejecuta el cálculo de las posibilidades válidas de movimientos del caballo para una lista de números predefinida.
- **`Caballo.py`**: Archivo que contiene la clase `CaballoAjedrez`, la cual implementa la lógica para calcular los movimientos válidos utilizando programación dinámica.

---

#### **Fórmula Matemática**
El cálculo de las secuencias válidas se basa en la siguiente fórmula recursiva:

Sea `f(n, m)` el número de secuencias válidas que comienzan en el número `n` con `m` movimientos restantes. Entonces:

```
f(n, m) = 
    1, si m == 0
    Σ f(s, m - 1), para cada s en movimientos_válidos(n), si m > 0
```

Donde:
- `n` es el número actual en el teclado.
- `m` es el número de movimientos restantes.
- `movimientos_válidos(n)` es el conjunto de números alcanzables desde `n` según las reglas del movimiento del caballo.

---

#### **Resultados Generados**
El archivo `lanzador.py` calcula las posibilidades válidas para una lista de movimientos predefinida: `[1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]`.

A continuación, se muestra una tabla con los resultados generados:

| **Cantidad de Movimientos** | **Posibilidades Válidas** |
|-----------------------------|---------------------------|
| 1                           | *20*   |
| 2                           | *46*   |
| 3                           | *104*   |
| 5                           | *544*   |
| 8                           | *6576*   |
| 10                          | *34432*   |
| 15                          | *2140672*   |
| 18                          | *25881088*   |
| 21                          | *307302400*   |
| 23                          | *1609056256*   |
| 32                          | *2792668987392*   |

> **Nota**: Los valores exactos de las posibilidades válidas se generan dinámicamente al ejecutar el archivo `lanzador.py`.

---

#### **Cómo Ejecutar**
1. Asegúrate de tener Python 3.8 o superior instalado.
2. Navega a la carpeta raíz del proyecto.
3. Ejecuta el archivo `lanzador.py`:
   ```bash
   python Caballos/lanzador.py
   ```

---

### README - Carpeta `Reinas`

---

#### **Descripción del Proyecto**
La carpeta `Reinas` contiene una implementación del problema clásico de las **N-Reinas**, que consiste en colocar `N` reinas en un tablero de ajedrez de tamaño `N x N` de manera que ninguna reina ataque a otra. Esto significa que no puede haber dos reinas en la misma fila, columna o diagonal.

El programa utiliza un enfoque de **backtracking** con una pila para explorar todas las configuraciones posibles del tablero y encontrar soluciones válidas. Además, incluye una funcionalidad para visualizar las soluciones generadas.

---

#### **Archivos Principales**
- **`lanzador.py`**: Archivo principal que ejecuta el cálculo de las soluciones para el problema de las N-Reinas.
- **`Nodo.py`**: Define la estructura de un nodo en el árbol de búsqueda utilizado para el backtracking.
- **`Reina.py`**: Contiene la clase `Reina`, que implementa la lógica para verificar si una reina amenaza a otra.
- **`Visualizar.py`**: Proporciona una función para visualizar las soluciones generadas en un tablero.

---

#### **Fórmula Matemática**
El problema de las N-Reinas se basa en las siguientes restricciones:
1. **Restricción de filas**: Cada reina debe estar en una fila diferente.
2. **Restricción de columnas**: Cada reina debe estar en una columna diferente.
3. **Restricción de diagonales**: Ninguna reina puede estar en la misma diagonal.

Estas restricciones se verifican para cada configuración del tablero durante el proceso de backtracking.

---

#### **Resultados Generados**
El archivo `lanzador.py` calcula las soluciones para diferentes valores de `N`. A continuación, se muestra una tabla con los resultados generados:

| **N-Reinas** | **Soluciones Distintas** | **Todas las Soluciones** | **Una Solución**       |
|--------------|---------------------------|---------------------------|-------------------------|
| 1            | 1                         | 1                         | `[0]`                  |
| 2            | 0                         | 0                         | `-`                    |
| 3            | 0                         | 0                         | `-`                    |
| 4            | 1                         | 2                         | `[1, 2, 0, 3]`         |
| 5            | 2                         | 10                        | `[0, 2, 4, 1, 3]`      |
| 6            | 1                         | 4                         | `[1, 3, 5, 0, 2, 4]`   |
| 7            | 6                         | 40                        | `[0, 2, 4, 6, 1, 3, 5]`|
| 8            | 12                        | 92                        | `[0, 4, 7, 5, 2, 6, 1, 3]` |
| 9            | 46                        | 352                       | `[0, 3, 6, 2, 5, 8, 1, 4, 7]` |
| 10           | 92                        | 724                       | `[0, 2, 5, 7, 9, 4, 8, 1, 3, 6]` |
| 15           | 285,053                   | 2,279,184                 | *(No mostrado por tamaño)* |

> **Nota**: Los valores exactos de las soluciones se generan dinámicamente al ejecutar el archivo `lanzador.py`.

---

#### **Cómo Ejecutar**
1. Asegúrate de tener Python 3.8 o superior instalado.
2. Navega a la carpeta raíz del proyecto.
3. Ejecuta el archivo `lanzador.py`:
   ```bash
   python Reinas/lanzador.py
   ```
4. Ingresa el valor de `N` cuando se solicite. El programa imprimirá:
   - El número total de soluciones distintas.
   - Una solución representada como un arreglo de columnas.
   - Todas las soluciones si se desea visualizarlas.

---

#### **Requisitos**
- Python 3.8 o superior.
- Librerías estándar de Python.

---

#### **Notas**
- Este proyecto es ideal para aprender sobre algoritmos de backtracking y optimización en problemas combinatorios.
- La visualización de las soluciones puede ser útil para entender cómo se distribuyen las reinas en el tablero.

---

#### **Contribuciones**
Si deseas contribuir al proyecto, puedes mejorar la eficiencia del algoritmo, agregar visualizaciones adicionales o extender el problema a variantes como las N-Reinas en tableros no cuadrados. Asegúrate de documentar tus cambios adecuadamente.
