
"""
0/1 Knapsack Problem / Masalah Ransel 0/1

English Description:
The 0/1 Knapsack Problem is a classic dynamic programming problem.
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
In the 0/1 Knapsack problem, each item can either be selected (1) or not selected (0); fractional items are not allowed.
This module provides two implementations: a standard O(n*W) space approach and a space-optimized O(W) approach.

Indonesian Description:
Masalah Ransel 0/1 (Knapsack Problem) adalah masalah pemrograman dinamis klasik.
Diberikan sekumpulan barang, masing-masing dengan berat dan nilai, tentukan jumlah setiap barang yang akan dimasukkan ke dalam koleksi sehingga total berat kurang dari atau sama dengan batas yang diberikan dan total nilai sebesar mungkin.
Dalam masalah Ransel 0/1, setiap barang dapat dipilih (1) atau tidak dipilih (0); barang pecahan tidak diperbolehkan.
Modul ini menyediakan dua implementasi: pendekatan ruang standar O(n*W) dan pendekatan ruang yang dioptimalkan O(W).

Implementation Details:
- Standard DP Approach / Pendekatan DP Standar:
  [EN] Uses a 2D table `dp[i][w]` representing the max value using first `i` items with capacity `w`.
  [ID] Menggunakan tabel 2D `dp[i][w]` yang merepresentasikan nilai maksimum menggunakan `i` barang pertama dengan kapasitas `w`.
  
- Space Optimized Approach / Pendekatan Optimasi Ruang:
  [EN] Uses a 1D array `dp[w]` updated in reverse order to avoid using the same item multiple times for the same capacity level.
  [ID] Menggunakan array 1D `dp[w]` yang diperbarui dalam urutan terbalik untuk menghindari penggunaan barang yang sama berkali-kali untuk tingkat kapasitas yang sama.
  
- Time Complexity / Kompleksitas Waktu:
  [EN] O(n * W) where n is the number of items and W is the capacity.
  [ID] O(n * W) di mana n adalah jumlah barang dan W adalah kapasitas.
  
- Space Complexity / Kompleksitas Ruang:
  [EN] O(n * W) for standard approach, O(W) for optimized approach.
  [ID] O(n * W) untuk pendekatan standar, O(W) untuk pendekatan yang dioptimalkan.

Usage Documentation:
  [EN] Import the function and pass weights list, values list, and capacity.
  [ID] Impor fungsi dan berikan daftar berat, daftar nilai, dan kapasitas.
  
  >>> weights = [10, 20, 30]
  >>> values = [60, 100, 120]
  >>> capacity = 50
  >>> knapsack_01(weights, values, capacity)
  220
"""
from typing import List

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Implementasi 0/1 Knapsack menggunakan Dynamic Programming (Bottom-Up).
    
    Args:
        weights: List berat item.
        values: List nilai item.
        capacity: Kapasitas maksimum tas.
        
    Returns:
        int: Nilai total maksimum.
    """
    n = len(values)
    
    # Inisialisasi tabel DP (n+1) x (capacity+1) dengan 0
    # dp[i][w] menyimpan nilai max untuk i item pertama dengan kapasitas w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight = weights[i-1]
            value = values[i-1]
            
            if weight <= w:
                # Opsi:
                # 1. Masukkan item ke tas -> value + dp[i-1][sisa kapasitas]
                # 2. Tidak masukkan item -> dp[i-1][kapasitas sama]
                dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])
            else:
                # Item terlalu berat untuk kapasitas w saat ini
                dp[i][w] = dp[i-1][w]
                
    return dp[n][capacity]

def knapsack_01_space_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Versi Space Optimized dari 0/1 Knapsack.
    Hanya menggunakan array 1D.
    Kompleksitas Ruang: O(W)
    """
    n = len(values)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Iterasi mundur untuk menghindari penggunaan hasil dari item yang sama pada iterasi ini
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
            
    return dp[capacity]

if __name__ == "__main__":
    # Test cases
    print("Running 0/1 Knapsack Tests...")
    
    # Items:
    # 1. W: 10, V: 60
    # 2. W: 20, V: 100
    # 3. W: 30, V: 120
    # Cap: 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    # Greedy (Fractional) result was 240
    # 0/1 Options:
    # A+B = 30W, 160V
    # A+C = 40W, 180V
    # B+C = 50W, 220V (Max)
    expected = 220
    
    res_dp = knapsack_01(weights, values, capacity)
    res_opt = knapsack_01_space_optimized(weights, values, capacity)
    
    print(f"Max Value (DP): {res_dp}")
    print(f"Max Value (Optimized): {res_opt}")
    
    assert res_dp == expected, "Standard DP failed"
    assert res_opt == expected, "Optimized DP failed"
    
    print("All 0/1 Knapsack tests passed!")
