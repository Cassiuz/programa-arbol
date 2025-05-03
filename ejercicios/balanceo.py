from estructura import ArbolBinarioBusqueda

def ejemplo_balanceo():
    print('\n=== EJEMPLO DE BALANCEO ===\n')

    # Árbol desbalanceado
    arbol_desbalanceado = ArbolBinarioBusqueda()
    for i in range(1, 8):
        arbol_desbalanceado.insertar(i)

    print(f'Árbol desbalanceado (inorden): {arbol_desbalanceado.recorrido_inorden()}')
    print(f'Altura del árbol desbalanceado: {arbol_desbalanceado.altura()}')
    print(f'¿Está balanceado? {arbol_desbalanceado.esta_balanceado()}')

    # Árbol mas balanceado
    arbol_balanceado = ArbolBinarioBusqueda()
    valores = [4, 2, 6, 1, 3, 5, 7]
    for valor in valores:
        arbol_balanceado.insertar(valor)

    print(f'Árbol más balanceado (inorden): {arbol_balanceado.recorrido_inorden()}')
    print(f'Altura del árbol balanceado: {arbol_balanceado.altura()}')
    print(f'¿Está balanceado? {arbol_balanceado.esta_balanceado()}')

    