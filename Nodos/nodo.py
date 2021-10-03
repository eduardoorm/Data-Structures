"""
En programación, concretamente en estructura de datos, un nodo es uno de los elementos de una lista enlazada, de un árbol o de un grafo. Cada nodo
será una estructura o registro que dispondrá de varios campos, y al menos uno de esos campos será un puntero o referencia a otro nodo,
de forma que, conocido un nodo,  a partir de esa referencia, será posible en teoría tener acceso a otros nodos de la estructura.
"""

from os import system 
system("cls")


class Nodo():

    def __init__(self,dato,siguiente = None):
        self.dato= dato
        self.siguiente = siguiente

    def __str__(self):
        return str(self.dato)

    
def reccorrer(nodo):
    while nodo != None:
        print(nodo.dato)
        nodo = nodo.siguiente


nodo4 = Nodo(12)
nodo3 = Nodo(45,nodo4)
nodo2 = Nodo(67,nodo3)
nodo1 = Nodo(89,nodo2)

reccorrer(nodo1)

