#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")
df.columns = df.columns.str.strip().str.replace('"', '')

#convierte a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna 
# print(type(df['edad'][0]))

#remplazandolos los datos "quintero" por "Maestro" 
df['apellido'] = df['apellido'].str.strip().str.replace('"', '').str.lower()
df.loc[df['apellido'] == 'quintero', 'apellido'] = 'maestro'

#eliminandolas filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")