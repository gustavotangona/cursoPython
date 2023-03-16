import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\gritos.csv")
print(df)
#creando el grafico
sns.lineplot(x="fecha",y="gritos",data=df)
#creando un punto en el momento de mas gritos
plt.plot("01-09",17,"o")
plt.show()
