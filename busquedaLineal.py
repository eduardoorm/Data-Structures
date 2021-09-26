# # "Funcionamiento"
# 1:Recorrer cada elemento de la lista
# 2: ir comparando el elemento que se desea buscar con cada elemento de la lista
# en caso de sr encontrado, retornar el indice en el que se encuentra, en caso contrario retornar falso,None,etc

lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]

def busquedaLineal(dato):
    for i in range(len(lista)):
        if(lista[i]==dato):
            return i
        
    return None
        

def buscar(dato):
    if busquedaLineal(dato):
        print("Se encontro el número en el indice",busquedaLineal(dato))
    else:
        print("No se encontro el número")


buscar(2)
