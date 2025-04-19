import pandas as pd

data = {
    'Personaje': ['Goku', 'Asta', 'Nami', 'Ichigo Kurosaki', 'Taiga Aisaka', 'Rikka Takanashi', 'Naruto Uzumaki', 'Rukia Kuchiki', 'Sung Jinwoo'],
    'Poder': ['100,000,000,000', '40,000', '50', '100,000,000', '15', '10', '100,000', '600,000', '200,000,000,000']
}

df = pd.DataFrame(data)

print("DataFrame Original:")
print(df)

print("\nNiveles de poder antes de la normalización:")
print(df['Poder'].unique())

mapeo_categorias = {
    '200,000,000,000': 'Multiversal',
    '100,000,000,000': 'Universal',
    '40,000': 'Continental',
    '50': 'Sobre-humana',
    '100,000,000': 'Galaxia',
    '15': 'Humana',
    '10': 'humana',
    '100,000': 'Planetario',
    '600,000': 'Galaxia'
}

df['Poder'] = df['Poder'].replace(mapeo_categorias)

print("\nNiveles de poder después de la normalización:")
print(df['Poder'].unique())

print("\nDataFrame Después de la Normalización:")
print(df)
