from nodo import Nodo  


class ListaSimpleEnlazada():

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = Nodo(dato)
            #Opción a la linea de arriba:
            #self.primero = Nodo(dato)
            #self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            """
            Otra forma:
            aux= Nodo(dato)
            self.ultimo.siguiente = aux
            self.ultimo = aux
            """
    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux= aux.siguiente
        aux.siguiente = None
        self.ultimo = aux
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

        

    