# 🧩 Sudoku Solver

Resolutor automático de Sudokus con interfaz gráfica (GUI) desarrollado en Python.

---

## 🎯 Objetivo del proyecto

Crear una aplicación gráfica que permita:
- Visualizar un tablero de Sudoku
- Resolver automáticamente el rompecabezas

---

## 🧠 Tecnologías utilizadas

- **Pytoh 3.10+**
- **pygame** para la interfaz gráfica
- **algoritmo de backtracking** para la resolución
---

## 📂 Estructura del proyecto

```
sudoku-solver/
│
├── src/                 
│   └── main.py
│   └── solver.py
│   └── gui.py
│   └── solver.py
│
├── .gitignore
├── README.md
```


---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.10 o superior** instalado.

1. 1  (Opcional) Crear un entorno virtual con conda

   ```
    conda create -n resolutor_sudoku_env python=3.11
    conda activate resolutor_sudoku_env
   ```

#### 2. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/resolutor_sudoku.git
   ```

#### 3. Accede al directorio del proyecto:

   ```
    cd resolutor_sudoku
   ```

#### 4. Instala las dependencias:

   ```
    pip install pygame
   ```

---

## :rocket: Uso

Desde la raíz del proycento, ejecuta:
   ```
    python src/main.py
   ```
Se abrirá una ventana con:

-  El tablero del Sudoku de ejemplo.
-  Las pistas iniciales en negro.
-  Los números calculados por el solver en azul (tras pulsar S).
-  Un pequeño texto con instrucciones en la parte inferior (S: resolver | R: reiniciar).

### :video_game: Controles:

-  Pulsa S para resolver el Sudoku.
-  Pulsa R para volver al puzzle inicial.
-  Cierra la ventana para salir de la aplicación.

---

## 📌 TODO

-  Mostrar visualmente el proceso de backtracking paso a paso.
-  Permitir que el usuario edite el tablero desde la GUI.
-  Cargar tableros desde archivos externos.
-  Añadir tests automáticos para el solver.