# Visualizador Web del Algoritmo de Dijkstra

Este módulo ofrece una página web estática que permite definir un grafo
ponderado, seleccionar un nodo origen y ejecutar el algoritmo de Dijkstra para
calcular la distancia mínima hacia el resto de nodos. Todo el procesamiento se
realiza en el navegador, por lo que no requiere dependencias de Python.

## Características

- Editor sencillo para registrar nodos y aristas ponderadas.
- Validación de pesos positivos antes de ejecutar el algoritmo.
- Visualización de la tabla de distancias y predecesores resultantes.
- Exportación e importación rápida del grafo en formato JSON para volver a
  cargar escenarios.

## Cómo ejecutar el proyecto

1. Abre `index.html` directamente en tu navegador, o bien sirviendo la carpeta
   con un servidor estático sencillo:
   ```bash
   python -m http.server --directory proyecto4 8000
   ```
   Después visita <http://localhost:8000/index.html>.
2. Utiliza los formularios para añadir nodos y aristas.
3. Selecciona el nodo de inicio y pulsa **Ejecutar Dijkstra** para ver las
   distancias resultantes.

> **Nota:** El menú principal `main.py` abre automáticamente esta interfaz
> empleando la ruta definida en el archivo `.env` (`DIJKSTRA_WEB_URL`).

## Dependencias

La interfaz está construida con HTML, CSS y JavaScript puro. No requiere
instalación adicional.
