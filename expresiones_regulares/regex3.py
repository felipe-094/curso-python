import re

text = "reemplazo todas las vocales porel asteriscos"

new_text = re.sub("[aeiou]", "*", text)

print(new_text)