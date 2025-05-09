# -----------------------------
# Librerias
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

np.random.seed(42)
plt.style.use('ggplot')

# -----------------------------
# Simulación Gacha de Genshin Impact
# -----------------------------
n_intentos = 5000  # Datos simulados
Deseos = np.random.randint(1, 91, n_intentos)
Gano = np.zeros(n_intentos, dtype=bool)

# ----------------------------
# Probabilidades de pity
# ----------------------------
prob_base = 0.006  # 0.6%
prob_soft_pity = 0.02  # Incremento progresivo tras el intento 75

for i in range(n_intentos):
    if Deseos[i] == 90:
        Gano[i] = True  # Hard pity garantizado
    elif Deseos[i] >= 75:
        prob = min(prob_base + (Deseos[i] - 74) * prob_soft_pity, 1.0)
        Gano[i] = np.random.rand() < prob
    else:
        Gano[i] = np.random.rand() < prob_base

datos = pd.DataFrame({'Deseos': Deseos, 'Gano': Gano})
datos['soft_pity'] = (datos['Deseos'] >= 75).astype(int)  # No se incluye el hard_pity

# -----------------------------
# Gráfico de Deseos
# -----------------------------
prob_observada = datos.groupby('Deseos')['Gano'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(prob_observada['Deseos'], prob_observada['Gano'], 'r-', label='Datos simulados')
plt.axvline(x=75, color='black', linestyle='--', label='Soft pity (75)')
plt.axvline(x=90, color='orange', linestyle='--', label='Hard pity (90)')
plt.axhline(y=prob_base, color='blue', linestyle=':', label='Prob. base (0.6%)')
plt.xlabel('Intentos acumulados')
plt.ylabel('Probabilidad de ganar')
plt.title('Sistema Gachapon de Genshin Impact (Simulación)')
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# Modelo Logístico (Sin Hard pity)
# -----------------------------
X = datos[['Deseos', 'soft_pity']]
y = datos['Gano']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = sm.add_constant(X_train)

modelo = sm.Logit(y_train, X_train)
modelo_fit = modelo.fit()
print(modelo_fit.summary())

# -----------------------------
# Gráfico: Probabilidad Predicha
# -----------------------------
X_pred = pd.DataFrame({'Deseos': np.arange(1, 91)})
X_pred['soft_pity'] = (X_pred['Deseos'] >= 75).astype(int)
X_pred = sm.add_constant(X_pred)

preds = modelo_fit.predict(X_pred)

plt.figure(figsize=(12, 6))
plt.plot(X_pred['Deseos'], preds, 'g-', label='Modelo logístico', linewidth=2)
plt.scatter(prob_observada['Deseos'], prob_observada['Gano'], color='red', label='Datos reales', alpha=0.5)
plt.axvline(x=75, color='black', linestyle='--')
plt.axvline(x=90, color='orange', linestyle='--')
plt.xlabel('Intentos acumulados')
plt.ylabel('Probabilidad predicha')
plt.title('Ajuste del Modelo Logístico')
plt.legend()
plt.grid(True)
plt.show()

