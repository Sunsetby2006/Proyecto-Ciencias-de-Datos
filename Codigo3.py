import matplotlib.pyplot as plt

Niveles = [1, 10, 25, 50, 70, 90, 100, 119] 
Poder = [19, 27, 39, 78, 99, 118, 125, 145] 

plt.scatter(Niveles, Poder, color='purple', marker='o')

plt.title('Niveles y poder de Sung Jinwoo')

plt.xlabel('Niveles')

plt.ylabel('Fuerza/Poder')

plt.grid(True, linestyle='--', alpha=0.5)

plt.show()