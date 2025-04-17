import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('darkgrid')  

promedios_A = [85, 90, 78, 92, 88]
promedios_B = [80, 85, 79, 90, 87]
etiquetas = ['P1', 'P2', 'P3', 'P4', 'P5']

indice = np.arange(len(etiquetas))

plt.figure(figsize=(12, 6))

plt.plot(indice, promedios_A, marker='o', linestyle='-', linewidth=2.5,
         color='#6a0dad', label='Grupo A')

plt.plot(indice, promedios_B, marker='s', linestyle='--', linewidth=2.5,
         color='#228B22', label='Grupo B')

plt.xticks(indice, etiquetas, fontsize=11)
plt.yticks(fontsize=11)

plt.title('Comparación de Promedios - Grupo A vs Grupo B', fontsize=16, fontweight='bold')
plt.xlabel('Pruebas Parciales', fontsize=13)
plt.ylabel('Promedio Obtenido', fontsize=13)

plt.legend(fontsize=12, loc='lower right')
plt.grid(True, linestyle='--', alpha=0.7)

for i in range(len(etiquetas)):
    plt.text(indice[i], promedios_A[i] + 0.8, str(promedios_A[i]),
             ha='center', va='bottom', fontsize=10, color='#6a0dad')
    plt.text(indice[i], promedios_B[i] - 2.5, str(promedios_B[i]),
             ha='center', va='top', fontsize=10, color='#228B22')

plt.tight_layout()
plt.show()
