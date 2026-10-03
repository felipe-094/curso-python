#creando una funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
       a = input("Numero 1: ")
       b = input("Numero 2: ")
       #intentando convertirlos a entero y bsumarlos
       try:
        resultado = int(a) + int(b)
        #si lanzo una exepcion, pedirle que ingrese los datos 
       except ValueError as e:
         print("Te pedi un numero salame, no te hagas el gracioso")
         print(f"ERROR {e}")
        #si todo salio bien terminamos el bucle
       else:
        break
        #si todo salio bien terminamos el bucle 
       finally:    
           print("Manejo de exepcion finalizado")
    
    #mostrando el resultado
    return resultado

print(sumar_dos())