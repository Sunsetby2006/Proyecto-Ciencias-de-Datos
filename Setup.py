import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

try:
    datos = pd.read_csv("50_Startups.csv")
    print("Archivo encontrado")
except:
    print("Archivo no encontrado")

df = pd.DataFrame(datos)

# Regresion Lineal

X = df[['R&D Spend', 'Administration', 'Marketing Spend']]
y = df['Profit']

# Division de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Modelo OLS 
"""X_train = sm.add_constant(X_train, prepend=True)
modelo_OLS = sm.OLS(endog=y_train, exog=X_train)
modelo_OLS = modelo_OLS.fit()
print(modelo_OLS.summary())"""

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X = X_train, y = y_train)

print("\n ____ Informacion del modelo ____")
print(f"Intercepto: {modelo.intercept_}")
print(f"Coeficiente: {modelo.coef_}")
print("Coeficiente de determnacion R2: ",modelo.score(X_train, y_train))

# Error del test del modelo

predicciones = modelo.predict(X=X_test)
rmse = root_mean_squared_error(y_true=y_test, y_pred=predicciones)

print(f"Primeras 5 Predicciones: {predicciones[0:5]}")
print(f"Error mse de test es: {rmse}")

# Grafica de visualización

# Crear el gráfico de dispersión
valores_reales = y_test

# Grafica de datos reales vs datos predictivos
# gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(valores_reales.values, label='Valores Reales', color='blue', marker='o')
plt.plot(predicciones, label='Predicciones', color='red', linestyle='--', marker='x')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Valores Reales vs. Predicciones')
plt.legend()
plt.grid(True)
plt.show()

print(df.head())

print("\n ---- informacion de df-----")
print(df.info())

print("\n---- Datos nulos ----")
print(df.isnull().sum())