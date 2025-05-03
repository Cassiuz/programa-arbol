class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1   # Para implementacion de arbol AVL

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # Metodos basicos
    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return NodoArbol(valor)
    
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        
        return nodo
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        
        if nodo.valor == valor:
            return True
        
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    # Recorrido del arbol
    def recorrido_inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

    def recorrido_preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado
    
    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)

    def recorrido_postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado
    
    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierda, resultado)
            self._postorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    # Operaciones adicionales
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        # caso base
        if nodo is None:
            return None
    
        # buscar el nodo a eliminar
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            # caso 1: Nodo hoja (sin hijos)
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            
            # caso 2: Nodo con 1 hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            # caso 3:Nodo con 2 hijos
            # encontrar el sucesor inorden (el menor valor en el subarbol derecho)
            sucesor = self._encontrar_minimo(nodo.derecha)
            # reemplazar el valor del nodo actual con el del sucesor
            nodo.valor = sucesor.valor
            # eliminar el sucesor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        actual = nodo
        # bajar hasta el nodo más a la izquierda
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # métodos para encontrar el minimio y maximo
    def minimo(self):
        if self.raiz is None:
            return None
        return self._encontrar_minimo(self.raiz).valor
    
    def maximo(self):
        if self.raiz is None:
            return None
        
        actual = self.raiz
        # bajar hasta el nodo más a la derecha
        while actual.derecha is not None:
            actual = actual.derecha
        return actual.valor
    
    # calcular altura del arbol
    def altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        
        altura_izq =  self._altura_recursiva(nodo.izquierda)
        altura_der = self._altura_recursiva(nodo.derecha)

        return max(altura_izq, altura_der) + 1
    
    # verificar si el arbol esta balanceada
    def esta_balanceado(self):
        return self._verificar_balance(self.raiz) != -1
    
    def _verificar_balance(self, nodo):
        if nodo is None:
            return 0
        
        # verificar subarbol izquierdo
        altura_izq = self._verificar_balance(nodo.izquierda)
        if altura_izq == -1:
            return -1
        
        # verificar subarbol derecho
        altura_der = self._verificar_balance(nodo.derecha)
        if altura_der == -1:
            return -1
        
        # verficar diferencias de alturas
        if abs(altura_izq - altura_der) > 1:
            return -1
        
        # retornar altura del nodo actual
        return max(altura_izq, altura_der) + 1