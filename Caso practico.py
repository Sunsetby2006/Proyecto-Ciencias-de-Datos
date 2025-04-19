# Caso práctico - Análisis para Carlos: Búsqueda del mejor condominio en Airbnb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
df = pd.read_csv('Base_de_datos.csv')

# 1. Filtrar condominios según los requisitos de Carlos
condominios = df[
    (df["property_type"] == "Condominium") & 
    (df["log_price"] <= df["log_price"].quantile(0.75)) &  # Precio menor al percentil 75
    (df["bathrooms"] >= 1) &  # Mínimo 1 baño (corrección: ahora filtra por baños)
    (df["number_of_reviews"] > 90) &  # Más de 90 reseñas
    (df["review_scores_rating"] > 90)  # Evaluación mayor a 90
][
    ["id", "log_price", "property_type", "room_type", "neighbourhood", 
     "number_of_reviews", "bedrooms", "bathrooms", "review_scores_rating"]
]

# 2. Identificar los barrios más populares (proxy para centralidad/seguridad)
top_vecindarios = condominios["neighbourhood"].value_counts().nlargest(5).index

# 3. Visualización: Precio mediano por barrio (Top 5)
plt.figure(figsize=(10, 6))
sns.barplot(
    data=condominios[condominios["neighbourhood"].isin(top_vecindarios)],
    x="neighbourhood", 
    y="log_price", 
    estimator="median",
    palette="viridis"
)
plt.title("Precio Mediano por Barrio (Top 5 más ofertados)", fontsize=14)
plt.xlabel("Barrio", fontsize=12)
plt.ylabel("Precio (logarítmico)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Visualización: Relación precio vs. número de baños
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=condominios, 
    x="bathrooms", 
    y="log_price",
    palette="coolwarm"
)
plt.title("Distribución de Precios por Número de Baños", fontsize=14)
plt.xlabel("Número de baños", fontsize=12)
plt.ylabel("Precio (logarítmico)", fontsize=12)
plt.tight_layout()
plt.show()

# 5. Mejores opciones para Carlos: 
# - Priorizar barrios del top 5 (centrales/seguros)
# - Ordenar por precio bajo y alta evaluación
mejores_opciones = condominios[
    condominios["neighbourhood"].isin(top_vecindarios)
].sort_values(
    ["log_price", "review_scores_rating"], 
    ascending=[True, False]
)

# Convertir log_price a precio normal para mejor interpretación
mejores_opciones["price_approx"] = round(np.exp(mejores_opciones["log_price"]), 2)

# Mostrar las 10 mejores opciones
print("\nTop 10 mejores condominios para Carlos:")
print(mejores_opciones[[
    "neighbourhood", "price_approx", "bathrooms", 
    "bedrooms", "review_scores_rating", "number_of_reviews"
]].head(10).to_string(index=False))