from scipy.interpolate import interp1d

t = [5, 15, 25]
y = [3, 10, 25]
t_objetivo = 20

# Spline lineal
spline = interp1d(t, y, kind='linear')
resultado = spline(t_objetivo)

print("Splines lineales P(20) =", resultado)
