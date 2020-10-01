class Nodo():
    
    def __init__(self,elemento):
        self.anterior = None
        self.elemento = elemento
        self.siguiente = None

    def obtener_elemento(self):
        return self.elemento

class Lista():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def obtener_vacio(self):
        if self.primero == None:
            return True

    def agregar_nodo_principio(self,elemento):
        nuevo = Nodo(elemento)
        if self.obtener_vacio() == True:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

    def agregar_nodo_final(self,elemento):
        nuevo = Nodo(elemento)
        if self.obtener_vacio() == True:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def eliminar_nodo_principio(self):
        if self.obtener_vacio():
            print("lista vacia")

        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("nodo eliminada, lista vacia")
        else:
            temporal = self.primero
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            temporal = None
            print("elemento eliminado")

    def eliminar_nodo_ultimo(self):

        if self.obtener_vacio():
            print("lista vacia")
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("Nodo eliminado,lista vacia")
        else:
            temporal = self.ultimo
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            temporal = None
            print("ultimo elemento borrado")
                
    def agregar_nodo_despues(self,elemento,referencia):
        nuevo = Nodo(elemento)

        if self.obtener_vacio():
            print("lista vacia")
            return

        temp = self.primero
        while True:
            if temp.obtener_elemento() == referencia:
                nuevo.siguiente = temp.siguiente
                nuevo.anterior = temp
                temp.siguiente = nuevo
                nuevo.siguiente.anterior = nuevo
                temp = None
                break
            else:
                temp = temp.siguiente
                if temp == self.ultimo:
                    break


    def obtener_primero(self):
        if self.obtener_vacio():
            print("lista vacia")
        else:
            return self.primero

    def obtener_ultimo(self):
        if self.obtener_vacio():
            print("lista vacia")
        else:
            return self.ultimo

    def imprimir_lista(self):

        if self.obtener_vacio():
            print("lista vacia")
        else:
            temporal = self.primero
            while True:
                print(temporal.obtener_elemento())
                if temporal == self.ultimo:
                    break
                else:
                    temporal = temporal.siguiente

    def imprimir_lista_rever(self):
        if self.obtener_vacio():
            print("lista vacia")
        else:
            temporal = self.ultimo
            while True:
                print(temporal.obtener_elemento())
                if temporal == self.primero:
                    break
                else:
                    temporal = temporal.anterior

