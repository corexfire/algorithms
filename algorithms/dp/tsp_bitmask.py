"""
Traveling Salesman Problem (Bitmask DP)
=======================================

1. English Description
----------------------
The Traveling Salesman Problem (TSP) is a classic algorithmic problem in the fields of computer science and operations research. It asks: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"

This implementation uses Dynamic Programming (DP) with Bitmasking to solve the problem exactly.
- **Logic**: The state of our DP is defined by `(mask, i)`, where `mask` is an integer whose binary representation denotes the set of visited cities (if the j-th bit is set, city j has been visited), and `i` denotes the current city (last visited).
- **State Transition**: `dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist[i][j])` for all unvisited cities `j`.
- **Time Complexity**: O(n^2 * 2^n), where n is the number of cities. This arises because there are 2^n states for the mask, n states for the current city, and we iterate through n possible next cities.
- **Space Complexity**: O(n * 2^n) to store the DP table and parent pointers for path reconstruction.
- **Input**: An n x n adjacency matrix where `dist[i][j]` represents the distance/cost from city i to city j.
- **Output**: A tuple containing the minimum cost and the ordered list of city indices representing the path.

2. Indonesian Description (Deskripsi Bahasa Indonesia)
------------------------------------------------------
Masalah Pedagang Keliling (TSP) adalah masalah klasik dalam ilmu komputer dan riset operasi. Pertanyaannya adalah: "Diberikan daftar kota dan jarak antar setiap pasangan kota, manakah rute terpendek yang mengunjungi setiap kota tepat satu kali dan kembali ke kota asal?"

Implementasi ini menggunakan Pemrograman Dinamis (DP) dengan Bitmasking untuk menyelesaikan masalah secara eksak.
- **Logika**: Status DP didefinisikan oleh `(mask, i)`, di mana `mask` adalah integer yang representasi binernya menandakan himpunan kota yang telah dikunjungi (jika bit ke-j menyala, kota j telah dikunjungi), dan `i` adalah kota saat ini (terakhir dikunjungi).
- **Transisi Status**: `dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist[i][j])` untuk semua kota `j` yang belum dikunjungi.
- **Kompleksitas Waktu**: O(n^2 * 2^n), di mana n adalah jumlah kota. Ini karena terdapat 2^n kemungkinan mask, n kemungkinan kota saat ini, dan kita melakukan iterasi ke n kemungkinan kota berikutnya.
- **Kompleksitas Ruang**: O(n * 2^n) untuk menyimpan tabel DP dan pointer parent untuk rekonstruksi jalur.
- **Input**: Matriks ketetanggaan n x n di mana `dist[i][j]` merepresentasikan jarak/biaya dari kota i ke kota j.
- **Output**: Tuple yang berisi biaya minimum dan daftar indeks kota yang berurutan yang merepresentasikan jalur tersebut.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Use Cases / Kasus Penggunaan**: 
  - [EN] Logistics and delivery route optimization (for small number of stops).
  - [ID] Logistik dan optimasi rute pengiriman (untuk jumlah pemberhentian yang sedikit).
  - [EN] Manufacturing (e.g., minimizing movement of a drill press/laser cutter).
  - [ID] Manufaktur (misalnya, meminimalkan pergerakan mesin bor atau pemotong laser).
  - [EN] DNA sequencing (ordering fragments).
  - [ID] Pengurutan DNA (mengurutkan fragmen).
- **Performance / Performa**: 
  - [EN] Much faster than the naive O(n!) brute-force permutation approach.
  - [ID] Jauh lebih cepat daripada pendekatan permutasi brute-force naif O(n!).
  - [EN] Feasible for n up to ~20-22 on modern hardware.
  - [ID] Dapat dijalankan untuk n hingga ~20-22 pada perangkat keras modern.
- **Limitations / Batasan**: 
  - [EN] Exponential time and space complexity makes it unsuitable for large n.
  - [ID] Kompleksitas waktu dan ruang eksponensial membuatnya tidak cocok untuk n yang besar.
  - [EN] For large datasets, heuristic approaches (e.g., 2-opt, Simulated Annealing, Genetic Algorithms) or approximation algorithms (e.g., Christofides) are preferred.
  - [ID] Untuk dataset besar, pendekatan heuristik (misalnya 2-opt, Simulated Annealing, Algoritma Genetika) atau algoritma aproksimasi (misalnya Christofides) lebih disukai.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Implementation Steps / Langkah Implementasi**:
  1. [EN] Define your distance matrix `dist_matrix`.
     [ID] Tentukan matriks jarak Anda `dist_matrix`.
  2. [EN] Call `tsp_bitmask(dist_matrix)`.
     [ID] Panggil `tsp_bitmask(dist_matrix)`.
  3. [EN] The function returns `(min_cost, path)`.
     [ID] Fungsi mengembalikan `(min_cost, path)`.
- **Dependencies / Ketergantungan**: 
  - [EN] Python 3.6+ (uses type hints). No external libraries required.
  - [ID] Python 3.6+ (menggunakan type hints). Tidak ada pustaka eksternal yang diperlukan.
- **Testing / Pengujian**:
  - [EN] Run this file directly (`python tsp_bitmask.py`) to execute built-in test cases.
  - [ID] Jalankan file ini secara langsung (`python tsp_bitmask.py`) untuk mengeksekusi kasus uji bawaan.
  - [EN] Validate with known TSP datasets or manual calculations for small graphs.
  - [ID] Validasi dengan dataset TSP yang diketahui atau perhitungan manual untuk graf kecil.
"""

from typing import List, Tuple, Optional

def tsp_bitmask(dist_matrix: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Solves TSP using Bitmask Dynamic Programming.
    
    Args:
        dist_matrix: Adjacency matrix where dist_matrix[i][j] is the distance from i to j.
        
    Returns:
        Tuple containing (minimum_cost, path).
        Path is a list of city indices visited in order, starting and ending at city 0.
    """
    n = len(dist_matrix)
    if n == 0:
        return 0, []
    
    # dp[mask][i] stores the minimum cost to visit cities in mask, ending at city i
    # mask is a bitmask representing the set of visited cities
    # i is the index of the last visited city
    # Initialize with infinity
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    # parent[mask][i] stores the previous city to reconstruct the path
    parent = [[-1] * n for _ in range(1 << n)]
    
    # Base case: Starting at city 0
    # mask 1 (binary 0...01) represents city 0 visited
    dp[1][0] = 0
    
    # Iterate through all subsets of cities (masks)
    for mask in range(1, 1 << n):
        # Iterate through all possible last cities i in the current subset
        for i in range(n):
            # If city i is in the current subset (mask)
            if (mask >> i) & 1:
                # Try to transition to a next city j
                for j in range(n):
                    # If city j is NOT in the current subset
                    if not ((mask >> j) & 1):
                        new_mask = mask | (1 << j)
                        new_cost = dp[mask][i] + dist_matrix[i][j]
                        
                        if new_cost < dp[new_mask][j]:
                            dp[new_mask][j] = new_cost
                            parent[new_mask][j] = i
                            
    # Find the minimum cost to return to the start city (0) from any city i
    # The mask must be (1 << n) - 1, meaning all cities visited
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    last_city = -1
    
    for i in range(1, n):
        cost = dp[full_mask][i] + dist_matrix[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i
            
    # If n=1, cost is 0 (distance from 0 to 0)
    if n == 1:
        return 0, [0, 0]
        
    if min_cost == float('inf'):
        return float('inf'), []
        
    # Reconstruct path
    path = []
    curr_mask = full_mask
    curr_city = last_city
    
    while curr_city != -1:
        path.append(curr_city)
        prev_city = parent[curr_mask][curr_city]
        curr_mask = curr_mask ^ (1 << curr_city)
        curr_city = prev_city
    
    # The path is constructed backwards from the last city to the start
    # We need to reverse it and append the return to start
    path = path[::-1] # [0, ..., last_city]
    path.append(0)    # [0, ..., last_city, 0]
    
    return min_cost, path

if __name__ == "__main__":
    print("TSP Bitmask DP Tests...")
    
    # Test Case 1: 4 Cities
    # 0 -> 1: 10, 0 -> 2: 15, 0 -> 3: 20
    # 1 -> 0: 10, 1 -> 2: 35, 1 -> 3: 25
    # 2 -> 0: 15, 2 -> 1: 35, 2 -> 3: 30
    # 3 -> 0: 20, 3 -> 1: 25, 3 -> 2: 30
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    cost, path = tsp_bitmask(dist_matrix)
    print(f"Test Case 1:")
    print(f"Matrix: {dist_matrix}")
    print(f"Min Cost: {cost}")
    print(f"Path: {path}")
    
    # Expected path: 0 -> 1 -> 3 -> 2 -> 0 = 10 + 25 + 30 + 15 = 80
    # Or 0 -> 2 -> 3 -> 1 -> 0 = 15 + 30 + 25 + 10 = 80
    assert cost == 80
    assert path[0] == 0 and path[-1] == 0
    assert len(path) == 5
    
    # Test Case 2: 3 Cities (Triangle)
    dist_matrix2 = [
        [0, 10, 20],
        [10, 0, 15],
        [20, 15, 0]
    ]
    cost2, path2 = tsp_bitmask(dist_matrix2)
    print(f"\nTest Case 2:")
    print(f"Min Cost: {cost2}")
    print(f"Path: {path2}")
    # 0 -> 1 -> 2 -> 0 = 10 + 15 + 20 = 45
    assert cost2 == 45
    
    print("\nAll TSP tests passed!")
