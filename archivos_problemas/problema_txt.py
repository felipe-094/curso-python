# tenemos dos listas una con nombre y apellido es decir una tiene nombre otra apellido
# tenemos que escribir los datos en un archivo de texto de forma optima con un for

#2 listas, una con nombres otra con apellidos 
nombres = ["felipe", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto","zing","Dalto","Robertix","tarado"]

#Registrar esta informacion en un TXT de forma optima

with open("archivos_problemas_resueltos\\nombre_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres,apellidos)]
    
