import numpy as np
from scipy.linalg import lu_solve, lu_factor

# Matriks koefisien
A = np.array([[2, 1, -1], [4, 1, 0], [0, -2, 1]])

# Vektor hasil
b = np.array([3, 4, -1])

# Dekomposisi LU
LU, piv = lu_factor(A)
x = lu_solve((LU, piv), b)

print("Metode Dekomposisi LU Gauss:")
print("Solusi x:", x)
