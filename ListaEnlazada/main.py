"""
                                                                    Linked List

Lista Enlazada:

Las listas enlazadas son estructuras de datos semejantes a los arrays(arreglos o listas en python) salvo que el acceso a un elemento no se hace
mediante un indice sino mediante un puntero

Lista Enlazada simple:

La lista enlazada basica es la lista enlazada simple la cual tiene un enlace por nodo, Este enlace apunta al siguiente nodo en la lista o al valor 
null o None si es el último nodo.

"""

from lista_simple_enlazada import ListaSimpleEnlazada

lista = ListaSimpleEnlazada()

lista.agregar_ultimo(12)
lista.agregar_ultimo(2)
lista.agregar_ultimo(25)
lista.agregar_ultimo(19)
lista.agregar_ultimo(30)

lista.eliminar_ultimo()

lista.recorrido()

# print("*********************")
# print(lista.primero.dato)
# print(lista.ultimo.dato)
print("*********************")
