# Los datos compuestos son aquellos que pueden contener varios valores, como las listas, tuplas, diccionarios y conjuntos. Estos tipos de datos nos permiten almacenar y organizar información de manera más compleja y estructurada.

#  creando una lista (se pueden modificar)
lista = ["Luis felipe", "Soy felipe", True,1.85]

#  creando una tupla (no se pueden modificar)
tupla = ("Luis felipe", "Soy felipe", True,1.85)

#  esto es valido para las listas
# lista[3] = "Maquinola"

# esto no es valido para las tuplas, ya que no se pueden modificar
# tupla[3] = "Maquinola" 

# print(lista[3]) 

# ------------------------ #
#  un set es una colección de elementos únicos, no ordenados y mutables. No permite elementos duplicados y no mantiene un orden específico y no accede a elementos por indices. Se utiliza para almacenar elementos únicos y realizar operaciones de conjunto como unión, intersección y diferencia.

# creando un conjunto (set)
conjunto = {"Luis felipe", "Soy felipe", True,1.85, "Soy felipe"}

# print(conjunto[3]) -> no puede acceder al elemento

#  ------------------------- #
#  un diccionario es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que puedes agregar, modificar o eliminar elementos después de su creación.

#creando un diccionario (dict)
diccionario = {
    'nombre': "Luis felipe",
    'canal': "Soy felipe",
    'esta_emocionado': True,
    'altura': 1.85,
    'dato_duplicado': "Soy felipe"
}
print(diccionario['altura'])  # Accediendo al valor asociado a la clave 'altura'