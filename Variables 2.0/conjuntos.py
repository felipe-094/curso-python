# los set son un tipo de dato en python que se utilizan para almacenar una colección de elementos únicos. A diferencia de las listas y tuplas, los set no permiten elementos duplicados y no mantienen un orden específico. Los set se definen utilizando llaves {} o la función set().

#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1,"Dato 3"}
print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) #verificando si el conjunto2 es un subconjunto del conjunto1
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)