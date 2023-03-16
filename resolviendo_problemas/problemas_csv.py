#cambiar el tipo de dto de una columna
import pandas as pd
df = pd.read_csv("resolviendo_problemas\\datos.csv")
#convertir a strin los datos de una columna
df['edad'] = df['edad'].astype(str)
print(type(df['edad']))
#reemplazando apellido x otro valor,,mostrando la columna apellido
df['apellido'].replace("Tangona","Carlos",inplace=True)
print(df['apellido'])

print(df)
#creando un csv con el dataframe resultante(limpio)
df.to_csv("resolviendo_problemas\\datos_limpios.csv")