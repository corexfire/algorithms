"""
Description:
    [EN] Floyd–Warshall computes shortest paths between all pairs of vertices in a weighted directed graph. Supports negative weights but not negative cycles, using dynamic programming to iteratively refine distances via intermediate vertices.
    [ID] Floyd–Warshall menghitung jalur terpendek untuk semua pasangan simpul pada graf berarah berbobot. Mendukung bobot negatif namun bukan siklus negatif, menggunakan pemrograman dinamis untuk menyempurnakan jarak melalui simpul perantara.

Implementation Details:
    [EN]
    - Recurrence: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all k.
    - Initialize dist from the adjacency matrix; use INF for no edge and 0 on the diagonal.
    - Time O(V^3), space O(V^2).
    [ID]
    - Rekurensi: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) untuk semua k.
    - Inisialisasi dist dari matriks ketetanggaan; gunakan INF untuk tanpa sisi dan 0 pada diagonal.
    - Waktu O(V^3), ruang O(V^2).

Usage Documentation:
    [EN]
    - Input: adjacency matrix graph[i][j] representing edge weights.
    - Call `floyd_warshall(graph)` to obtain the all-pairs shortest distance matrix.
    [ID]
    - Input: matriks ketetanggaan graph[i][j] yang merepresentasikan bobot sisi.
    - Panggil `floyd_warshall(graph)` untuk mendapatkan matriks jarak terpendek semua pasangan.

Examples:
    >>> INF = float('inf')
    >>> graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    >>> result = floyd_warshall(graph)
    >>> result[0][1], result[0][2], result[0][3], result[1][3]
    (5, 8, 9, 4)
"""

from typing import List, Any

# Konstanta Infinity
INF = float('inf')

def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
    """
    Mengimplementasikan algoritma Floyd-Warshall.
    
    Args:
        graph: Adjacency matrix VxV dimana graph[i][j] adalah bobot edge i->j.
               Jika tidak ada edge, graph[i][j] = INF.
               graph[i][i] harus 0.
        
    Returns:
        List[List[float]]: Matriks jarak terpendek.
    """
    V = len(graph)
    # Buat salinan graph untuk distance matrix
    dist = [row[:] for row in graph]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update jarak jika melalui node k lebih pendek
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
    return dist

if __name__ == "__main__":
    # Test Cases
    print("Running Floyd-Warshall Tests...")
    
    # Graph:
    # 0 -> 1 (5)
    # 0 -> 3 (10)
    # 1 -> 2 (3)
    # 2 -> 3 (1)
    
    # Representasi Matrix 4x4
    graph_data = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    
    result = floyd_warshall(graph_data)
    
    print("Shortest Distance Matrix:")
    for row in result:
        print(row)
        
    # Verifikasi Manual:
    # 0 -> 1 = 5
    # 0 -> 2 = 0 -> 1 -> 2 = 5 + 3 = 8
    # 0 -> 3 = min(10, 0 -> 1 -> 2 -> 3 = 5 + 3 + 1 = 9) -> 9
    
    assert result[0][1] == 5
    assert result[0][2] == 8
    assert result[0][3] == 9
    assert result[1][2] == 3
    assert result[1][3] == 4 # 1 -> 2 -> 3 = 3 + 1 = 4
    
    print("All Floyd-Warshall tests passed!")
