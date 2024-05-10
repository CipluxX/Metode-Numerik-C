import numpy as np
from scipy.linalg import solve_triangular

# Matriks koefisien
A = np.array([[2, 1, -1], [4, 1, 0], [0, -2, 1]])

# Vektor hasil
b = np.array([3, 4, -1])

# Dekomposisi Crout
LU = np.linalg.cholesky(A)
y = solve_triangular(LU, b, lower=True)
x = solve_triangular(LU.T, y)

print("Metode Dekomposisi Crout:")
print("Solusi x:", x)
