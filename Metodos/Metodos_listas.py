#LIST - crea una lista

#LEN-cuenta la cantidad de elementos de una lista

# APPEND - agrega un elemento al final de la lista
# INSERT - agrega un elemento a la lista en el indice especificado
# EXTEND - agrega varios elementos a la lista

# POP- elimina un elemento de una lista, pide indice y devuelve valor
# REMOVE - remueve un elemento de una lista, pide valor
# CLEAR - elimina todos los elementos de una lista 

# SORT - ordena una lista de forma ascendente a descendente
# REVERSE - invierte el orden de los elementos de una lista

#  creando una lista con list()
lista = list([34,56,23,True,False]) 

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el antepenultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")

# eliminando todos los elementos de la lista
# lista.clear()

#ordenando la lista de forma ascendente(si usamos el parametro reverse=True lo ordena en reversa)
# lista.sort()

# invirtiendo los elementos de una lista
lista.reverse()

print(lista)