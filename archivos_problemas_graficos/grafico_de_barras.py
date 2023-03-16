import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\juan_ingresos.csv")
print(df)
#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)
#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()
print(f'El total de ingresos de Juan es de ${total_ingresos} mensuales')
#mostrando el grafico

plt.show()