from scipy.interpolate import lagrange

t = [5, 15, 25]
y = [3, 10, 25]
t_objetivo = 20

# Crear polinomio de Lagrange
polinomio = lagrange(t, y)
resultado = polinomio(t_objetivo)

print("Lagrange P(20) =", resultado)
