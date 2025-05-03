from estructura import ArbolBinarioBusqueda

# Operaciones básicas con un árbol binario de búsqueda
def ejemplo_basico():
    print('\n=== EJEMPLO BASICO ===\n')
    arbol = ArbolBinarioBusqueda()

    # Insertar valores
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    # mostrar recorridos
    print(f'Recorrido inorden: {arbol.recorrido_inorden()}')
    print(f'Recorrido preorden: {arbol.recorrido_preorden()}')
    print(f'Recorrido postorden: {arbol.recorrido_postorden()}')

    # Buscar valores
    print(f'¿El valor 40 está en el árbol? {arbol.buscar(40)}')
    print(f'¿El valor 90 está en el árbol? {arbol.buscar(90)}')

    # encontrar minimo y maximo
    print(f'Valor mínimo: {arbol.minimo()}')
    print(f'Valor máximo: {arbol.maximo()}')

    # mostrar altura del arbol
    print(f'Altura del árbol: {arbol.altura()}')

    # verificar si está balanceado
    print(f'¿Está balanceado? {arbol.esta_balanceado()}')


