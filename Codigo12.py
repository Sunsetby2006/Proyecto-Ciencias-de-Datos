import pandas as pd

# DataFrame.
data = {
    'Videojuego': ['God Of War', 'Bioshock', 'Final Fantasy', 'Hollow Knight'],
    'Entregas': ['6', '4', '16', '2'],  # (string)
}

df = pd.DataFrame(data)

# DataFrame original y tipos de datos.
print("DataFrame original:")
print(df)
print("\nTipos de datos originales:")
print(df.dtypes)

# Cambiar tipo de la columna 'Entregas'.
df['Entregas'] = df['Entregas'].astype(int)

# DataFrame cambiado.
print("\nDataFrame después de convertir 'Entregas' a tipo entero:")
print(df)
print("\nTipos de datos después del cambio:")
print(df.dtypes)
