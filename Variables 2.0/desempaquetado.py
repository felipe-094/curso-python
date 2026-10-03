# el desempaquetado de variables es una forma de asignar varias variables a la vez, utilizando una sola linea de codigo. Para esto, se necesita que el numero de variables a asignar sea igual al numero de elementos que se van a desempaquetar.

#creando una tupla
datos = ("cursos","Pipe",1000000)

#desempaquetando la tupla
nombre,apellido,suscriptores = datos

#mostrando resultados
print(suscriptores)
