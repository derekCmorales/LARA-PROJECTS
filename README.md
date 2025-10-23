# LARA Projects

Colección de cuatro proyectos desarrollados durante el semestre y un lanzador
principal con interfaz gráfica. El menú principal permite abrir cada utilidad
de forma independiente y proporciona un acceso directo a un visualizador web
del algoritmo de Dijkstra incluido en el repositorio.

## Estructura del repositorio

```
LARA-PROJECTS/
├── main.py              # Menú principal en PyQt5
├── requirements.txt     # Dependencias comunes de Python
├── proyecto1/           # Generador de tablas de verdad (PySide6)
├── proyecto2/           # Simplificador booleano con SymPy (PyQt6)
├── proyecto3/           # Analizador y probador de expresiones regulares (PyQt6)
├── proyecto4/           # Visualizador web interactivo del algoritmo de Dijkstra
├── header.png, logo.png # Recursos de interfaz del menú principal
└── README.md
```

## Configuración rápida

1. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows usar: .venv\Scripts\activate
   ```
2. **Instala todas las dependencias de Python con un solo comando:**
   ```bash
   pip install -r requirements.txt
   ```
3. **(Opcional) Define variables de entorno:**
   - El menú principal lee `PYTHON_INTERPRETER` y `DIJKSTRA_WEB_URL` si están
     definidos en tu entorno o en un archivo `.env` que puedes crear en la raíz
     del proyecto.
   - `PYTHON_INTERPRETER` permite ajustar la ruta del ejecutable de Python.
   - `DIJKSTRA_WEB_URL` indica el recurso que se abrirá al lanzar el
     visualizador de Dijkstra (por defecto `proyecto4/index.html`).
4. **Ejecuta el menú principal:**
   ```bash
   python3 main.py
   ```

> **Nota:** En sistemas Linux puede ser necesario instalar bibliotecas del
> sistema para Qt (por ejemplo, `sudo apt install libegl1` y otros paquetes
> relacionados) antes de ejecutar las aplicaciones gráficas.

## Dependencias

Las dependencias compartidas se definen en `requirements.txt`:

- `PyQt5`: interfaz del menú principal.
- `PySide6`: GUI del generador de tablas de verdad.
- `PyQt6`: interfaces para el simplificador booleano y el probador de regex.
- `sympy`: simplificación booleana simbólica en `proyecto2`.
- `python-dotenv`: carga automática de variables definidas en un `.env`
  opcional.

El módulo estándar `itertools` utilizado en `proyecto1` forma parte de Python y
no requiere instalación adicional.

## Descripción de los proyectos

### Menú principal (`main.py`)

Aplicación PyQt5 que centraliza los accesos a cada proyecto. Lee variables de
entorno (o de un `.env` opcional) para utilizar el intérprete de Python
preferido y la ruta del visualizador web.

### Proyecto 1 — Generador de tablas de verdad (`proyecto1/`)

- Construido con PySide6.
- Genera tablas de verdad a partir de expresiones booleanas.
- Permite exportar resultados en formatos CSV y JSON.

### Proyecto 2 — Simplificación booleana (`proyecto2/`)

- Basado en PyQt6 y `sympy`.
- Simplifica expresiones booleanas mostrando los pasos principales del proceso.

### Proyecto 3 — Analizador de expresiones regulares (`proyecto3/`)

- Implementado con PyQt6.
- Destaca coincidencias en texto, evalúa patrones y valida expresiones en
  tiempo real.

### Proyecto 4 — Visualizador web de Dijkstra (`proyecto4/`)

- Interfaz web estática (HTML, CSS y JavaScript) para construir grafos dirigidos
  con pesos no negativos.
- Permite añadir nodos y aristas, importar/exportar el grafo como JSON y
  ejecutar el algoritmo de Dijkstra para mostrar distancias mínimas, predecesor
  y ruta.
- Puede abrirse directamente desde un navegador o a través del menú principal.

## Ejecución individual

Cada módulo puede iniciarse por separado desde la raíz del repositorio. El
intérprete puede ajustarse mediante la variable de entorno `PYTHON_INTERPRETER`
definida en tu shell o en un `.env` opcional.

```bash
python3 proyecto1/main.py         # Generador de tablas de verdad (PySide6)
python3 proyecto2/main.py         # Simplificador booleano (PyQt6 + SymPy)
python3 proyecto3/regex_gui.py    # Probador de expresiones regulares (PyQt6)
```

Para abrir el visualizador web sin utilizar el menú principal:

```bash
python -m http.server --directory proyecto4 8000
# Luego visita http://localhost:8000/index.html
```

o bien abre directamente `proyecto4/index.html` en tu navegador.

¡Disfruta explorando los proyectos!
