#creando una funcion que muestre la serie de fibonacci entre 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
           fibonacci_lista.append(b)
           a,b = b,a+b
           
resultado = fibonacci(33)
print(resultado)

#def → palabra clave para crear una función
#fibonacci → nombre de la función
#num → parámetro (el valor que le vas a pasar)

#a = 0
#b = 1
#Estos son los dos primeros numeros de fibonacci

#fibonacci_lista = [0]
#Creas una lista
# Ya contiene el primer número: 0
# Aquí se van a guardar los resultados

#for i in range(num):
#range(num) genera números desde 0 hasta num - 1
# El bucle se repite num veces (en este caso, 33 veces)
# i no se usa realmente, solo sirve para repetir

#if b > num: return fibonacci_lista

#Esto es clave:
# Si b es mayor que num:
# se detiene la función inmediatamente
# devuelve la lista
# return = “termina todo y devuelve esto”

#else:
    # fibonacci_lista.append(b)

#Si b NO es mayor que num
# entonces se agrega a la lista
# append() = agregar elemento a la lista

#a,b = b,a+b
#Esto es lo más importante del algoritmo:
# a toma el valor de b
# b toma el valor de a + b
# Es lo que genera la secuencia de Fibonacci



