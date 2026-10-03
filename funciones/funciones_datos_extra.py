#creando una funcion con tres parameros
# def frase(nombre,apellido,abjetivo):
#     return f'Hola {nombre} {apellido}, sos muy {abjetivo}'

# #utilizando keyword arguments
# frase_resultante = frase(abjetivo = "capo",nombre = "pipe",apellido ="dalto")
# print(frase_resultante)

#creando la misma funcion con un parametro opcional y n valor por defecto
def frase(nombre,apellido,abjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {abjetivo}'

frase_resultante = frase("pipe","dalto",abjetivo="inteligente")
print(frase_resultante)