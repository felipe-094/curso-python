import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre 
nombres = df["nombre"]


df.columns = df.columns.str.strip().str.replace('"', '')

#ordenando el dataframe  por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obtenidendo data estadistica de dataframe con describe()
df_info = df.describe()

#accediendo a un elemento especifico con loc
#accediendo a ala edad de la fila 2 loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico con loc
##accediendo a ala edad de la fila 2 iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"] 

#accediendo a todos los apellidos con iloc 
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc 
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc 
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)