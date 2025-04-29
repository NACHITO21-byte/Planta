import numpy as np

t = np.array([5, 15, 25])
y = np.array([3, 10, 25])
t_objetivo = 20

# Ajuste lineal: y = mt + b
m, b = np.polyfit(t, y, 1)
resultado = m * t_objetivo + b

print("Regresión lineal P(20) =", resultado)
