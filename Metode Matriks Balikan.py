import numpy as np

# Matriks koefisien
A = np.array([[2, 1, -1], [4, 1, 0], [0, -2, 1]])

# Vektor hasil
b = np.array([3, 4, -1])

# Matriks balikan
A_inv = np.linalg.inv(A)

# Solusi
x = np.dot(A_inv, b)

print("Metode Matriks Balikan:")
print("Solusi x:", x)
