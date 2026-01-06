"""
Rod Cutting Problem (Dynamic Programming)
-----------------------------------------

1. English Description
----------------------
The Rod Cutting problem is a classic optimization problem where a rod of length `n` is cut into smaller pieces.
Each piece length has a specific price. The goal is to determine the best way to cut the rod to maximize total revenue.
This implementation uses Dynamic Programming to solve the problem efficiently and can also reconstruct the optimal cuts.

Time Complexity: O(n^2) - Nested loops to find optimal cuts for each length up to n.
Space Complexity: O(n) - To store DP table and cut reconstruction array.

2. Indonesian Description
-------------------------
Masalah Pemotongan Batang (Rod Cutting) adalah masalah optimasi klasik di mana batang sepanjang `n` dipotong menjadi potongan-potongan yang lebih kecil.
Setiap panjang potongan memiliki harga tertentu. Tujuannya adalah menentukan cara terbaik untuk memotong batang guna memaksimalkan total pendapatan.
Implementasi ini menggunakan Pemrograman Dinamis untuk menyelesaikan masalah secara efisien dan juga dapat merekonstruksi potongan yang optimal.

Kompleksitas Waktu: O(n^2) - Loop bersarang untuk menemukan potongan optimal untuk setiap panjang hingga n.
Kompleksitas Ruang: O(n) - Untuk menyimpan tabel DP dan array rekonstruksi potongan.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Algorithm Variant / Varian Algoritma**:
  - [EN] Unbounded Knapsack style DP (bottom-up).
  - [ID] DP gaya Unbounded Knapsack (bottom-up).
- **Key Logic / Logika Utama**:
  - [EN] `dp[i] = max(prices[j] + dp[i-j-1])` for all valid cuts `j`.
  - [ID] `dp[i] = max(prices[j] + dp[i-j-1])` untuk semua potongan `j` yang valid.
- **Data Structures / Struktur Data**:
  - [EN] `dp` array for max values, `cut` array for solution reconstruction.
  - [ID] Array `dp` untuk nilai maksimal, array `cut` untuk rekonstruksi solusi.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Usage / Penggunaan**:
  - [EN] Call `rod_cut(prices, n)` where `prices` is a list of prices for length 1, 2, ..., and `n` is the total length.
  - [ID] Panggil `rod_cut(prices, n)` di mana `prices` adalah daftar harga untuk panjang 1, 2, ..., dan `n` adalah total panjang.
- **Output / Keluaran**:
  - [EN] Returns a tuple `(max_profit, list_of_cuts)`.
  - [ID] Mengembalikan tuple `(max_profit, list_of_cuts)`.
"""

from typing import List, Tuple

def rod_cut(prices: List[int], n: int) -> Tuple[int, List[int]]:
    dp = [0] * (n + 1)
    cut = [0] * (n + 1)
    for i in range(1, n + 1):
        best = 0
        best_j = 0
        for j in range(1, i + 1):
            val = prices[j - 1] + dp[i - j]
            if val > best:
                best = val
                best_j = j
        dp[i] = best
        cut[i] = best_j
    res = []
    length = n
    while length > 0:
        res.append(cut[length])
        length -= cut[length]
    return dp[n], res

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    val, cuts = rod_cut(prices, 8)
    assert val == 22
    assert sum(cuts) == 8
    print("All Rod Cutting tests passed!")
