
#creando una funcion simople
#def saloudar():
#   print("Hola pipe, mi maestro ¿Como andas?")

#ejecutando la funcion simple
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo.lower()
    if(sexo == "mujer"):
        abjetivo = "reina"
    elif (sexo == "hombre"):
        abjetivo = "titan"
    else:
        abjetivo = "amor"
    print(f"Hola {nombre}, mi {abjetivo} ¿Como andas?")
    
saludar("Camila","mujer")
saludar("pipe","hombre")
saludar("Fran","no binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado paa crearla fue: {primer_numero}")