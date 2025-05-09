import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
style.use('ggplot')  # Establece el estilo de los gráficos
# Datos de kills, muertes y asistencias
kills = [15,12,10,24,5,11,11,11,12,12,12,8,5,10,0,31]
muertes = [17,16,18,12,7,20,10,12,16,18,14,12,4,13,7,20]
asistencias = [5,5,3,8,1,4,4,1,4,4,1,3,2,3,2,5]
# Crear el DataFrame con los datos
dataframe = pd.DataFrame({'kills': kills, 'muertes': muertes, 'asistencias': asistencias})
# GRÁFICA DE DISPERSIÓN
fig, ax = plt.subplots(figsize=(6, 3.84))  # Crear el gráfico de dispersión
ax.scatter(dataframe['muertes'], dataframe['kills'], color='#72afd6')  # Dibujar los puntos en el gráfico
ax.set_title('Distribución de kills y muertes')  # Título del gráfico
ax.set_xlabel('Muertes')  # Etiqueta para el eje X
ax.set_ylabel('Kills')  # Etiqueta para el eje Y
plt.grid(True)  # Activar la cuadrícula en el gráfico
plt.show()  # Mostrar el gráfico
# CORRELACIÓN PEARSON
corr_test = pearsonr(x=dataframe['muertes'], y=dataframe['kills'])  # Calcular la correlación de Pearson
print("Coeficiente de correlacion de Pearson:", corr_test[0])  # Imprimir el coeficiente de correlación
print("P-Value:", corr_test[1])  # Imprimir el p-valor de la correlación
# REGRESIÓN LINEAL
X = dataframe[['muertes']]  # Variable independiente
y = dataframe['kills']  # Variable dependiente
# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.8,
    random_state=1234,
    shuffle=True
)
# statsmodels
datos_train = pd.DataFrame({'muertes': X_train.values.flatten(), 'kills': y_train.values})  # Crear el DataFrame de entrenamiento
# Crear y ajustar el modelo de regresión lineal usando fórmula
modelo_formula = smf.ols(formula='muertes ~ kills', data=datos_train)
modelo_formula = modelo_formula.fit()  # Ajustar el modelo
print(modelo_formula.summary())  # Imprimir el resumen del modelo
# statsmodels con matrices
X_train_matrix = sm.add_constant(X_train, prepend=True)  # Añadir la constante para el modelo de regresión
# Crear y ajustar el modelo de regresión lineal con matrices
modelo = sm.OLS(endog=y_train, exog=X_train_matrix)
modelo = modelo.fit()  # Ajustar el modelo
print(modelo.summary())  # Imprimir el resumen del modelo
# GRÁFICA DE REGRESIÓN
plt.figure(figsize=(6, 4))  # Crear un gráfico de regresión
plt.scatter(X_train['muertes'], y_train, color='#72afd6', label='Datos de entrenamiento')  # Graficar los datos de entrenamiento
plt.plot(X_train['muertes'], modelo.predict(X_train_matrix), color='#d671c0', label='Regresión lineal')  # Graficar la línea de regresión
plt.xlabel('Muertes')  # Etiqueta para el eje X
plt.ylabel('Kills')  # Etiqueta para el eje Y
plt.title('Regresión lineal: kills vs muertes')  # Título del gráfico
plt.legend()  # Mostrar leyenda
plt.grid(True)  # Activar la cuadrícula
plt.show()  # Mostrar el gráfico
# PREDICCIONES Y ERROR
# Calcular las predicciones en el conjunto de entrenamiento
predicciones = modelo.get_prediction(exog=X_train_matrix).summary_frame(alpha=0.05)
print(predicciones.head(4))  # Imprimir las primeras 4 predicciones
# Preparar el conjunto de prueba con una constante añadida
X_test_matrix = sm.add_constant(X_test, prepend=True)
# Realizar las predicciones en el conjunto de prueba
predicciones_test = modelo.predict(exog=X_test_matrix)
# Calcular el error cuadrático medio (RMSE)
rmse = np.sqrt(mean_squared_error(y_true=y_test, y_pred=predicciones_test))
print(f"\nEl error (RMSE) en test es: {rmse:.2f}")  # Imprimir el error RMSE en el conjunto de prueba