"Expresiones Generadoras"
"Nos permite crear un generador de datos en base a una expresiòn"

#Imprimimos la expresión generadora
print("Imprimos la expresión generadora")
print(i for i in range(5))

#Obtenemos los datos asignandolos a una variable
print("Imprimimos como lista")
x= (i for i in range(5))

#Imprimimos como lista
print(list(x))


print("x:",x)
print("type(x)",type(x))
input()

#Obtenemos de nuevo los datos porque ya se consumieron
x= (i for i in range(5))

#Imprimimos los valores uno por uno
print	("Imprimimos los valores uno por uno")
try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print("Se ha alcanzado el final")


#Obtenemos los datos
x=(i**2 for i in range(5))

#Imprimimos como lista
print("Imprimimos la lista")
print(list(x))
input()
print()

#Obtenemos los datos
x=(i**2 for i in range(5))
#Imprimimos los valores uno por uno
print("Imprimimos los valores uno por uno")
try:
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print("Se ha alcanzado el final")

input()
print()

#Creamos una expresión generadora con letras
x = (i for i in 'abcdefgh')
print("Imprimimos la lista")
print(list(x))
input()
print()


#Creamos una expresión generadora con letras
x = (i for i in 'abcdefgh')
print("Imprimimos uno por uno con su ordinal(code ascii)")
try:
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
    letra = next(x)
    print(letra,ord(letra))
except StopIteration:
    print("Se ha alcanzado el final")

#Creamos un diccionario con la expresión generadora
diccionario = dict((i,ord(i)) for i in 'abcdefgh')
print("Imprimimos el diccionario")
print(diccionario)

#Ejecutamos una suma en base a los elementos generados
print("Imprimimos la Lista")
print(list(i*2 for i in range(5))) #aqui ya la convertimos en una lista y ya no necesitamos el print list() enla siguien linea

input()
print()

print("Imprimimos una suma a partir de la expresión generadora")
print(sum(i*2 for i in range(5)))


