"""
Stoer-Wagner Minimum Cut Algorithm
----------------------------------

1. English Description
----------------------
The Stoer-Wagner algorithm solves the Global Minimum Cut problem in an undirected weighted graph.
It finds a partition of the vertices into two non-empty sets such that the sum of weights of edges crossing the partition is minimized.
It is more general than s-t min-cut (Max-Flow Min-Cut) as it doesn't require specific source/sink nodes.

Time Complexity: O(V * E + V^2 log V) with Fibonacci heap, O(V^3) with simple array/adjacency matrix (used here).
Space Complexity: O(V^2) for adjacency matrix.

2. Indonesian Description
-------------------------
Algoritma Stoer-Wagner menyelesaikan masalah Potongan Minimum Global (Global Minimum Cut) dalam graf berbobot tak berarah.
Ini mencari partisi simpul menjadi dua himpunan tidak kosong sedemikian rupa sehingga jumlah bobot tepi yang melintasi partisi diminimalkan.
Ini lebih umum daripada s-t min-cut karena tidak memerlukan simpul sumber/tujuan tertentu.

Kompleksitas Waktu: O(V^3) dengan matriks ketetanggaaan sederhana (digunakan di sini).
Kompleksitas Ruang: O(V^2) untuk matriks ketetanggaaan.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Minimum Cut Phase / Fase Potongan Minimum**:
  - [EN] Similar to Prim's algorithm ("Maximum Adjacency Search"). Grows a set of vertices by adding the most tightly connected one.
  - [ID] Mirip dengan algoritma Prim ("Pencarian Adjacency Maksimum"). Menumbuhkan set simpul dengan menambahkan yang paling terhubung erat.
- **Contraction / Kontraksi**:
  - [EN] The last two vertices added in a phase are merged into one super-vertex.
  - [ID] Dua simpul terakhir yang ditambahkan dalam fase digabungkan menjadi satu super-vertex.
- **Global Minimum / Minimum Global**:
  - [EN] Tracks the "cut-of-the-phase" and updates the global minimum if smaller.
  - [ID] Melacak "potongan-fase" dan memperbarui minimum global jika lebih kecil.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Input Data / Data Input**:
  - [EN] `adj`: Adjacency matrix where `adj[i][j]` is the weight of edge `(i, j)`.
  - [ID] `adj`: Matriks ketetanggaaan di mana `adj[i][j]` adalah bobot tepi `(i, j)`.
- **Execution / Eksekusi**:
  - [EN] `stoer_wagner_min_cut(adj)` returns the weight of the minimum cut. Note: Modifies `adj` in place.
  - [ID] `stoer_wagner_min_cut(adj)` mengembalikan bobot potongan minimum. Catatan: Memodifikasi `adj` di tempat.
"""

from typing import List

def stoer_wagner_min_cut(adj: List[List[int]]) -> int:
    n = len(adj)
    vertices = list(range(n))
    best = float("inf")
    while len(vertices) > 1:
        used = [False] * n
        weights = [0] * n
        prev = -1
        for _ in range(len(vertices)):
            sel = -1
            for v in vertices:
                if not used[v] and (sel == -1 or weights[v] > weights[sel]):
                    sel = v
            if used[sel]:
                break
            used[sel] = True
            if _ == len(vertices) - 1:
                if weights[sel] < best:
                    best = weights[sel]
                if prev != -1:
                    for v in range(n):
                        adj[prev][v] += adj[sel][v]
                        adj[v][prev] = adj[prev][v]
                    vertices.remove(sel)
                break
            prev = sel
            for v in range(n):
                if not used[v]:
                    weights[v] += adj[sel][v]
    return best

if __name__ == "__main__":
    adj = [
        [0, 3, 0, 3],
        [3, 0, 4, 0],
        [0, 4, 0, 2],
        [3, 0, 2, 0],
    ]
    mcut = stoer_wagner_min_cut([row[:] for row in adj])
    assert mcut == 5
    print("All Stoer–Wagner tests passed!")
