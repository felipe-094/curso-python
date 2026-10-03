animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
       
#iterando dos lista del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo la lista 1: {numero}")
    print(f"recorriendo la lista 2: {animal}")
    

#forma no optima de recorrer una lista con su indice (no funciona en conjunto)
for num in range(len(numeros)):
    print(numeros[num])    
    
#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else: 
    print(f"el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos
