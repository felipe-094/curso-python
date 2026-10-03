# Los diccionarios en Python son estructuras de datos que almacenan pares de clave-valor. Son mutables, lo que significa que puedes modificar su contenido después de crearlos. Aquí hay algunos métodos comunes para trabajar con diccionarios:

# KEYS() -> devuelve las claves (tambien nos sirve para iterar)
# GET() -> devuelve el valor de una clave
# CLEAR() -> elimina todos los elementos 
# POP() -> elimina un elemento 
# ITEMS() -> para iterar el dict

diccionario = {
    "nombre" : 'felipe',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

# obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_clave = diccionario.get("subs")
# print(valor_de_clave)

# eliminando todo del diccionario
# diccionario.clear() 

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)