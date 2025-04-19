import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Datos
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [40255, 34500, 20010, 33300, 50250, 12005, 68148, 45899, 14999, 22755, 39400, 90500]
}

df = pd.DataFrame(data)

# Orden correcto de los meses para que se graficque bien
orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
               'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df['Mes'] = pd.Categorical(df['Mes'], categories=orden_meses, ordered=True)

# Crear colores desde la paleta crest
colores = sns.color_palette("crest", n_colors=len(df))

# Agregar una nueva columna de color en función del mes
df['Color'] = colores

# Gráfico
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Mes', weights='Ventas', kde=True, discrete=True, hue='Mes', palette=colores, edgecolor='black')

plt.title('Ventas de Xbox Series X por Mes en 2022', fontsize=16)
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
