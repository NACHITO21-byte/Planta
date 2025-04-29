def newton_interpolation(x, y, x0):
    n = len(x)
    coef = y.copy()

    # Diferencias divididas
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    
    # Evaluar en x0
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (x0 - x[i]) + coef[i]
    return resultado

t = [5, 15, 25]
y = [3, 10, 25]
t_objetivo = 20

print("Newton P(20) =", newton_interpolation(t, y, t_objetivo))
