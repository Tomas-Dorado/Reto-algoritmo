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

f(n, m) = 1, si m == 0 Σ f(s, m - 1), para cada s en movimientos_válidos(n), si m > 0


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
