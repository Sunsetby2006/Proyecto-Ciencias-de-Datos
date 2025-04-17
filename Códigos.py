import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns  

calificaciones = [70, 75, 65, 80, 85]
horas_estudio = [2, 3, 1, 4, 5]

plt.figure(figsize=(12, 7))

sns.set_style('whitegrid') 

plt.scatter(calificaciones, horas_estudio, color='crimson', s=100, edgecolor='black', label='Estudiantes')

for i, (calif, hora) in enumerate(zip(calificaciones, horas_estudio)):
    plt.text(calif + 0.5, hora + 0.1, f"Estudiante {i+1}", fontsize=9)

coef = np.polyfit(calificaciones, horas_estudio, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(calificaciones, poly1d_fn(calificaciones), color='blue', linestyle='--', label='Tendencia')

plt.title("Relación entre Calificaciones y Horas de Estudio", fontsize=16, fontweight='bold')
plt.xlabel("Calificaciones", fontsize=12)
plt.ylabel("Horas de Estudio", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.show()