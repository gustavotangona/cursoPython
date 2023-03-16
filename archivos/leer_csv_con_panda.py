import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
#le ponemos el nombre DF (data frame) xq no es el archivo en realidad...es justamente el data frame

#obteniendo los datos de la columna nombre
nombres = df["name"]
print(df)

#ordenando el df por la edad 
df_orden_ascendente = df.sort_values("age")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("age",ascending=False)
print(df_orden_ascendente)
print(df_orden_descendente)

#accediendo a la primer fila con Head
primer_fila = df.head(1)
print(primer_fila)

#accediendo a la ultima fila con Tail
ultimas_filas = df.tail(2)
print(ultimas_filas)








                    
                      
