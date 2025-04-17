import matplotlib.pyplot as plt
import numpy as np

tallas = [38, 39, 40, 41, 42]
personas = [5, 8, 12, 15, 10]

plt.style.use('ggplot')
colores = plt.cm.viridis(np.linspace(0.3, 0.9, len(tallas)))

fig, ax = plt.subplots(figsize=(12, 6))
barras = ax.bar(tallas, personas, color=colores, edgecolor='black', width=0.6)

ax.set_title('Distribución de Tallas de Calzado', fontsize=16, fontweight='bold')
ax.set_xlabel('Talla de calzado', fontsize=13)
ax.set_ylabel('Cantidad de personas', fontsize=13)
ax.set_xticks(tallas)
ax.set_ylim(0, max(personas) + 5)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{int(altura)}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 5),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=11, fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()
