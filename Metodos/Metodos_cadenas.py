# Los Metodos de cadenas son funciones predefinidas que se pueden usar para manipular y trabajar con cadenas de texto en Python. Aquí hay algunos ejemplos comunes de métodos de cadenas:

# DIR - devuelve la lista de atributos validos del objeto pasado.

# UPPER - convierte a Mayuscula
# LOWER - convierte a Minuscula 
# CAPITALIZE - primera eb Mayuscula

# FIND - metodo encuentra la primera aparicion del valor especificado, si no devuelve -1
# INDEX - metodo encuentra la primera aparicion del valor especificado, si no devuelve un error

# ISNUMERIC - si es numerico devulve true 
# ISALPHA - si es alfanumerico devuelve true

# COUNT - devuelve el numero de ocurrencias de una subcadena en la cadena dada

# ENDSWITH - verifica si una cadena comienza con
# STARTSWITH - verifica si una cadena termina con

# REPLACE - remplaza un valor por otro
# SPLIT - separa por el parametro dado.

cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido Maquinola"

# comvierte a Mayuscula
mayusc = cadena1.upper() #devuelve "HOLA SOY FELIPE"

# comvierte a Minuscula
minus = cadena1.lower() #devuelve "hola soy felipe"

# primera letra en mayuscuala 
primera_letra_mayusc = cadena1.capitalize() #devuelve "Hola soy felipe"

# buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("s") 

# buscamos una cadena en otra cadena, si no hay coincidencia lanza una exepcion
busqueda_index = cadena1.index("a") 

# si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric() #devuelve False

# si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha() #devuelve False

# contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencias = cadena1.count("F") 

# contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H") #devuelve True

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("H") #devuelve True

# remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(",", " ") 

# separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


# print(mayusc)
# print(minus)
# print(primera_letra_mayusc)
# print(busqueda_find)
# print(busqueda_index)
# print(es_numerico)
# print(es_alfanumerico)
# print(contar_coincidencias)
# print(contar_caracteres)
# print(empieza_con)
# print(termina_con)
# print(cadena_nueva)
print(cadena_separada[0])
