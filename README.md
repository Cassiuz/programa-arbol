# Árboles Binarios de Búsqueda (BST)

Una implementación en Python de la estructura de datos Árbol Binario de Búsqueda con ejemplos prácticos.

## 📋 Descripción

Este proyecto implementa la estructura de datos Árbol Binario de Búsqueda (BST) en Python, demostrando las operaciones fundamentales y características de esta importante estructura de datos usada en algoritmos de búsqueda eficientes.

Un Árbol Binario de Búsqueda es una estructura de datos jerárquica donde cada nodo tiene como máximo dos hijos (izquierdo y derecho). La propiedad principal de un BST es que para cada nodo:
- Todos los nodos en el subárbol izquierdo tienen valores menores que el nodo actual
- Todos los nodos en el subárbol derecho tienen valores mayores que el nodo actual

Esta propiedad permite realizar búsquedas, inserciones y eliminaciones en tiempo logarítmico (O(log n)) en el caso promedio.

## 🚀 Características

- **Operaciones básicas**:
  - Inserción de nodos
  - Búsqueda de valores
  - Eliminación de nodos (con manejo de diferentes casos)
  - Recorridos del árbol (inorden, preorden, postorden)

- **Operaciones avanzadas**:
  - Encontrar el valor mínimo/máximo
  - Calcular la altura del árbol
  - Verificar si el árbol está balanceado

## 📁 Estructura del Proyecto

```
programa-arbol/
│
├── estructura/               # Implementación de las clases principales
│   ├── __init__.py
│   └── clases.py             # Definición de NodoArbol y ArbolBinarioBusqueda
│
├── ejercicios/               # Ejemplos prácticos de uso
│   ├── __init__.py
│   ├── basico.py             # Operaciones básicas (inserción, búsqueda, recorridos)
│   ├── eliminacion.py        # Demostración de eliminación de nodos
│   └── balanceo.py           # Comparación de árboles balanceados vs. desbalanceados
│
└── main.py                   # Punto de entrada que ejecuta todos los ejemplos
```

## 🔧 Requisitos

- Python 3.6 o superior

## 🚀 Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Cassiuz/programa-arbol.git
   cd programa-arbol
   ```

2. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

## 📖 Conceptos Implementados

1. **Nodo del Árbol**: Estructura básica que contiene un valor y referencias a los hijos izquierdo y derecho.

2. **Inserción**: Mantiene la propiedad BST colocando los valores menores a la izquierda y los mayores a la derecha.

3. **Eliminación**: Maneja tres casos:
   - Eliminar una hoja (nodo sin hijos)
   - Eliminar un nodo con un hijo
   - Eliminar un nodo con dos hijos (requiere encontrar el sucesor inorden)

4. **Recorridos**:
   - Inorden: Izquierda → Raíz → Derecha (produce valores en orden ascendente)
   - Preorden: Raíz → Izquierda → Derecha
   - Postorden: Izquierda → Derecha → Raíz

5. **Balance**: Un árbol está balanceado cuando la diferencia de altura entre los subárboles izquierdo y derecho de cualquier nodo no es mayor que 1.

