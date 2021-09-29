'''
Busqueda Binaria
Funcionamiento:
Buscar datos en una colección de datos
Ventajas:
Realiza menos comparaciones que el metodo de Busqueda Lineal

Requisitos antes de realizar dicho algoritmo:
Tener la lista ordenada de manera acendente(MENOR A MAYOR)
Debe tener valores unicos

Algoritmo:
1: Calcular el punto medio, (izquierda + derecha)/2
2: Comparar el punto medio con el dato a buscar
3: Si es igual el dato al punto medio, retornar indice
4: si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio + 1
5: si el dato a buscar es mayor que el punto medio, derecha es igual al valor del medio - 1
6: se seguira ejecutando siempre y cuanto izquierda sea menor o igual a derecha
'''

lista = [0,88,72,21,14,16,90,35,47,6,68,12,10,54,41]
lista.sort()
print(lista)
#1 Buscar el punto medio (puntero)
#2 Comprobar si el punto medio es el valor que buscamos
#3 Si el número es menor al valor que buscamos aumentamos inicio 1 sobre el puntero
# Si el número es mayor al valor que buscamos disminuimos el final 1 bajo el puntero
#Si inicio mayor o igual que final entonces elnúmero no está en la lista

def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while (inicio <= final):
        puntero= (inicio+final)//2 #doble / = division entera
        print(f'inicio {inicio} + final {final}')
        print(puntero)
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None


def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f'El valor {valor} no se encontró'
    else:
        return f'El número {valor} se encuentra en la posición {res_busqueda}'


print(buscar_valor(16))