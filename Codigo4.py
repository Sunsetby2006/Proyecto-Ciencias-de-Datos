import pandas as pd

comentarios = [
    "La PC tiene muy buena calidad, pero es caro.",
    "Me encantó el diseño, se nota la calidad del producto.",
    "Los componentes son buenos, pero esperaba un mejor diseño.",
    "El diseño es único y muy bueno.",
    "Demasiado caro para lo que esperaba, aunque en general es bueno."
]

df = pd.DataFrame(comentarios, columns=['Comentario'])

print("\nComentarios de clientes sobre PC gamer:")
print(df)

palabras_clave = ["Bueno", "Caro", "Calidad", "Diseño"]
for palabra in palabras_clave:
    df[palabra] = df['Comentario'].str.contains(palabra, case=False, na=False)

print("\nAnálisis de palabras clave:")
print(df)

conteo = df[palabras_clave].sum()
print("\nFrecuencia de palabras clave en los comentarios:")
print(conteo)