# 1 ALUMNO ES PROFESOR
# 1 ALUMNO ES ASISTENTE

#(A)
#Pedir la edad de los compañeros que 
#vinieron hoy a clase y ordenar
#los datos de menor a mayor

#(B)
#El mayor es el profesor y el
#menor el asistente:
#¿Quien es quien?

#falto el profesor y los pibes van a armar la clase 

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

#funcion para obtener al asistente y al profesor segun la edad. 
def obtener_compañeros(cantidad_de_compañeros):
    
   #creando la lista conlos compañeros 
   compañeros = []
   
   #ejecutando un for para pedir informacion de cada compañero
   for i in range(cantidad_de_compañeros):
    nombre = input("ingrese el nombre del compañero: ")
    edad = int(input("ingrese la edad del compañero: "))
    compañero = (nombre,edad)
    
    #agregando la informacion a la lista 
    compañeros.append(compañero)
    
   #ordenandolos de menor a mayor segun su edad  
   compañeros.sort(key=lambda x:x[1])
   
   #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre 
   #para definir al asistente y al profesor 
   asistente = compañeros[0][0]
   profesor = compañeros[-1][0]
   
   #retornamos una tupla
   return asistente,profesor

#desempaquetamos los que nos retorna la funcion 
asistente,profesor = obtener_compañeros(5)

#mostrando resultado
print(f"El profesor es {profesor} y su asistente es {asistente}")