# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


# Clase Lista enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Verifica si la lista esta vacia
    def vacio(self):
        if self.cabeza is None:
            print("Esta vacia")
        else:
            print("Lista no vacia")

    # Insertar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Insertar al final
    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    # Insertar antes de un elemento X
    def insertarAntes(self, x, data):
        if self.cabeza is None:
            print("Lista vacia")
            return

        # Si el primero es el que buscamos
        if self.cabeza.data == x:
            self.agregarInicio(data)
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente

        print("Elemento no encontrado")

    # Insertar despues de un elemento X
    def insertarDespues(self, x, data):
        actual = self.cabeza

        while actual is not None:
            if actual.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente

        print("Elemento no encontrado")

    # Eliminar el primero
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("Lista vacia")
            return

        self.cabeza = self.cabeza.siguiente

    # Eliminar el ultimo
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("Lista vacia")
            return

        # Si solo hay un nodo
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = None

    # Buscar elemento por valor
    def buscar(self, valor):
        actual = self.cabeza

        while actual is not None:
            if actual.data == valor:
                print("Verdadero")
                return
            actual = actual.siguiente

        print("Falso")

    # Contar elementos
    def contar(self):
        cont = 0
        actual = self.cabeza

        while actual is not None:
            cont += 1
            actual = actual.siguiente

        print("Cantidad de elementos:", cont)


