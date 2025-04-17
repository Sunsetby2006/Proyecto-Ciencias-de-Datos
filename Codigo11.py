Código:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DataFrame.
data = {
    'Panteones completados': [5, 3, 2, 4, 4, 1, 2, 5, 3, 1],
    'Horas de Juego': [102, 201, 158, 121, 203, 182, 172, 202, 206, 94]
}

df = pd.DataFrame(data)

# Gráfico de dispersión.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Horas de Juego', y='Panteones completados', data=df, color='blue', s=100, marker='o')
plt.title('Gráfico de Dispersión: Horas de Juego vs Panteones')
plt.xlabel('Horas de Juego')
plt.ylabel('Panteones')
plt.grid(True)
plt.show()

# Diagrama de caja.
plt.figure(figsize=(10, 6))
sns.boxplot(x='Panteones completados', data=df, color='lightblue')
plt.title('Diagrama de Caja de los Panteones Completados')
plt.xlabel('Panteones')
plt.grid(True)
plt.show()