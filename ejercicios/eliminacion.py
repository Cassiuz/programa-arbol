from estructura import ArbolBinarioBusqueda

# Eliminicación de nodos
def ejemplo_eliminacion():
    print('\n=== EJEMPLO DE ELIMINACION ===\n')
    arbol = ArbolBinarioBusqueda()

    # Insertar valores
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    print(f'Árbol original (inorden): {arbol.recorrido_inorden()}')

    # Eliminar una hoja (20)
    hoja = 20
    arbol.eliminar(hoja)
    print(f'Después de eliminar {hoja} (hoja): {arbol.recorrido_inorden()}')

    # Eliminar un nodo con un hijo (30)
    nodo_un_hijo = 30
    arbol.eliminar(nodo_un_hijo)
    print(f'Después de eliminar {nodo_un_hijo} (nodo con hijo): {arbol.recorrido_inorden()}')

    # Eliminar un nodo con dos hijos (70)
    nodo_dos_hijos = 70
    arbol.eliminar(nodo_dos_hijos)
    print(f'Después de eliminar 70 (nodo con 2 hijos): {arbol.recorrido_inorden()}')
