#creando diccionarios con dict()
diccionario = dict(nombre="pipe",apellido="quintero")

#las listas no pueden ser claves y usamos fronzenset para meter conjuntos
diccionario = {frozenset(["pipe", "rancio"]):"jasjasa"} 

#creando diccionarios con fromkeys() valor por defecto: none 
diccionario = dict.fromkeys(["nombre","apellido"]) #esto es una forma de crear diccionarios con mucho valores sin definir

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")



print(diccionario["apellido"])