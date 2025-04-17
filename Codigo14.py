import pandas as pd
from datetime import datetime

# Ejemplo de DataFrame con una columna de fechas
data = {'fecha': ['2025-01-08','2025-02-14','2025-03-21','2025-04-01','2025-04-10','2025-04-15','2025-04-16','2025-04-05']}
df = pd.DataFrame(data)

# Convertir la columna 'fecha' a tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Fecha de análisis
fecha_analisis = datetime(2025, 5,25)

# Filtrar las filas con fechas anteriores a la fecha de análisis
df_validado = df[df['fecha'] < fecha_analisis]

# Mostrar el DataFrame validado
print(df_validado)
