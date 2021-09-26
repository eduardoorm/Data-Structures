'''
Busqueda Binaria
Funcionamiento:
Buscar datos en una colección de datos
Ventajas:
Realiza menos comparaciones que el metodo de Busqueda Lineal

Requisitos antes de realizar dicho algoritmo:
Tener la lista ordenada de manera acendente(MENOR A MAYOR)

Algoritmo:
1: Calcular el punto medio, (izquierda + derecha)/2
2: Comparar el punto medio con el dato a buscar
3: Si es igual el dato al punto medio, retornar indice
4: si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio + 1
5: si el dato a buscar es mayor que el punto medio, derecha es igual al valor del medio - 1
6: se seguira ejecutando siempre y cuanto izquierda sea menor o igual a derecha
'''