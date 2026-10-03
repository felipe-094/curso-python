import re

# La cadena en la que se buscaran los patrones
text = "La fecha es 23/05/2021 y el telefono es +1-555-555-5555"

# El patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se reeplazara el patron
replacement = "fecha oculta"

# Reemplazar todas las apariciones del patron en la cadena texto
new_text = re.sub(pattern, replacement, text)

# imprimir el resultado
print("Texto modificado:", new_text)