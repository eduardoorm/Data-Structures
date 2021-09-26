#Ordenamiento por Slección

# Es un algoritmo que consiste en ordenar los elementos de manera acendente o descendente
#Funcionamiento
#Buscar el dato mas pequeño de la lista
#Intercambiarlo por el acutal
#Seguir buscando el dato mas pequeño de la lista
#Intercambiarlo por el actual
#Esto se repetira sucesivamente

lista = [4,2,6,8,5,7,0]

menor=0
for i in range(len(lista)):
    min = i
    for j in range(i,len(lista)):
        if(lista[j]<lista[min]):
            min=j
    aux= lista[i]
    lista[i]=lista[min]
    lista[min] = aux

print(lista)




