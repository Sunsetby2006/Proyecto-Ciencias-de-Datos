import matplotlib.pyplot as plt

lenguajes = ["Python", "JavaScript", "Java", "C#", "Ruby", "Go", "Swift", "Kotlin", "PHP", "Rust", "Jupiter", "Otros"]
votos = [120, 95, 80, 60, 35, 40, 45, 30, 25, 50, 55, 20]

colors = plt.cm.viridis_r([i / len(votos) for i in range(len(votos))])

plt.figure(figsize=(12, 8))
barras = plt.bar(lenguajes, votos, color=colors)

plt.title("Preferencia de Lenguajes de Programación en 2025", fontsize=16, fontweight='bold')
plt.xlabel("Lenguajes", fontsize=12)
plt.ylabel("Número de Votos", fontsize=12)
plt.xticks(rotation=45, ha='right')

for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 2, str(int(altura)),
             ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig("lenguajes_preferidos_2025.png", dpi=300)
plt.savefig("lenguajes_preferidos_2025.pdf")

plt.show()