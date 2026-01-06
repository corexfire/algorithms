"""
Matrix Chain Multiplication / Perkalian Rantai Matriks

English Description:
Matrix Chain Multiplication is an optimization problem concerning the most efficient way to multiply a given sequence of matrices.
The problem is not actually to perform the multiplications, but merely to decide the order of the parenthesizations of the matrix products involved.
The goal is to find the minimum number of scalar multiplications needed.

Indonesian Description:
Perkalian Rantai Matriks (Matrix Chain Multiplication) adalah masalah optimasi mengenai cara paling efisien untuk mengalikan urutan matriks yang diberikan.
Masalahnya sebenarnya bukan untuk melakukan perkalian, tetapi hanya untuk memutuskan urutan tanda kurung dari produk matriks yang terlibat.
Tujuannya adalah untuk menemukan jumlah minimum perkalian skalar yang diperlukan.

Implementation Details:
- DP Approach / Pendekatan DP:
  [EN] `m[i][j]` stores the minimum number of scalar multiplications needed to compute the matrix product `A[i]...A[j]`.
  [ID] `m[i][j]` menyimpan jumlah minimum perkalian skalar yang diperlukan untuk menghitung produk matriks `A[i]...A[j]`.
  
- Chain Length / Panjang Rantai:
  [EN] We iterate through chain lengths from 2 to n. For each length, we find the optimal split point `k`.
  [ID] Kita melakukan iterasi melalui panjang rantai dari 2 hingga n. Untuk setiap panjang, kita menemukan titik pemisahan optimal `k`.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n^3) where n is the number of matrices.
  [ID] O(n^3) di mana n adalah jumlah matriks.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n^2) to store the DP table.
  [ID] O(n^2) untuk menyimpan tabel DP.

Usage Documentation:
  [EN] Call `matrix_chain_multiplication(p)` where `p` is a list of dimensions. `p` has length n+1 for n matrices.
  [ID] Panggil `matrix_chain_multiplication(p)` di mana `p` adalah daftar dimensi. `p` memiliki panjang n+1 untuk n matriks.
  
  >>> matrix_chain_multiplication([1, 2, 3, 4])
  18
  >>> matrix_chain_multiplication([10, 20, 30])
  6000
"""
import sys
from typing import List

def matrix_chain_multiplication(p: List[int]) -> int:
    """
    Finds the minimum number of multiplications needed to multiply the chain of matrices.
    
    Args:
        p: List of dimensions. Matrix A[i] has dimension p[i-1] x p[i].
           Length of p is n+1 for n matrices.
        
    Returns:
        Minimum number of scalar multiplications
    """
    n = len(p) - 1
    
    # m[i][j] stores the minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j]
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # L is chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = sys.maxsize
            
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
    return m[1][n]

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 18),         # (1x2 * 2x3) * 3x4 = 6 + 12 = 18
        ([10, 20, 30], 6000),       # 10x20 * 20x30 = 6000
        ([10, 20, 30, 40, 30], 30000),
        ([40, 20, 30, 10, 30], 26000)
    ]
    
    for dims, expected in test_cases:
        result = matrix_chain_multiplication(dims)
        print(f"Dimensions: {dims} -> Min Multiplications: {result}, Expected: {expected}")
        assert result == expected
        
    print("All test cases passed!")
