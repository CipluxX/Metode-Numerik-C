1. Import Library:
   - `numpy` digunakan untuk operasi matematika dan manipulasi array, terutama dalam pembuatan matriks koefisien dan vektor hasil.
   - `scipy.linalg` digunakan untuk metode-metode khusus dalam aljabar linear, seperti dekomposisi LU, Cholesky, dan solusi triangular.
2. Matriks Koefisien dan Vektor Hasil:
   - `A` adalah matriks koefisien dari sistem persamaan linear.
   - `b` adalah vektor hasil dari sistem persamaan linear.
3. Metode Matriks Balikan:
   - `np.linalg.inv(A)` digunakan untuk menghitung invers dari matriks koefisien `A`.
   - `np.dot(A_inv, b)` mengalikan matriks invers dengan vektor hasil untuk mendapatkan solusi sistem menggunakan metode matriks balikan.
4. Metode Dekomposisi LU Gauss:
   - `lu_factor(A)` menghitung faktorisasi LU dari matriks koefisien `A`.
   - `lu_solve((LU, piv), b)` menggunakan faktorisasi LU untuk menyelesaikan sistem persamaan linear.
5. Metode Dekomposisi Crout:
   - `cholesky(A)` menghitung dekomposisi Cholesky dari matriks koefisien `A`.
   - `solve_triangular(LU_crout, b, lower=True)` memecahkan sistem persamaan linear menggunakan dekomposisi Cholesky.
