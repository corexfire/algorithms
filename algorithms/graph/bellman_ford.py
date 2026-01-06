"""
Description:
    [EN] Bellman-Ford computes single-source shortest paths on directed graphs that may contain negative edge weights. It can detect negative cycles: if reachable, shortest paths are undefined.
    [ID] Bellman-Ford menghitung jarak terpendek dari satu sumber pada graf berarah yang dapat memiliki bobot sisi negatif. Algoritma ini mendeteksi siklus negatif: jika dapat dijangkau, jalur terpendek tidak terdefinisi.

Implementation Details:
    [EN]
    - Relax all edges exactly |V|−1 times to propagate shortest distances.
    - Detect negative cycles by checking for improvements on a final pass.
    - Time O(V·E), space O(V).
    [ID]
    - Relaksasi semua sisi sebanyak |V|−1 kali untuk menyebarkan jarak terpendek.
    - Deteksi siklus negatif dengan memeriksa perbaikan pada satu iterasi akhir.
    - Waktu O(V·E), ruang O(V).

Usage Documentation:
    [EN]
    - Input: list of vertices and list of edges (u, v, weight).
    - Call `bellman_ford(vertices, edges, start_node)`; returns (distances or None, has_negative_cycle).
    [ID]
    - Input: daftar simpul dan daftar sisi (u, v, bobot).
    - Panggil `bellman_ford(vertices, edges, start_node)`; mengembalikan (jarak atau None, ada_siklus_negatif).

Examples:
    >>> vertices = [0, 1, 2]
    >>> edges = [(0, 1, 1), (1, 2, 2), (0, 2, 4)]
    >>> distances, has_cycle = bellman_ford(vertices, edges, 0)
    >>> print(distances)
    {0: 0, 1: 1, 2: 3}
"""
from typing import List, Tuple, Dict, Any, Optional

Edge = Tuple[Any, Any, float]

def bellman_ford(vertices: List[Any], edges: List[Edge], start_node: Any) -> Tuple[Optional[Dict[Any, float]], bool]:
    """
    Mengimplementasikan algoritma Bellman-Ford.
    
    Args:
        vertices: List of semua node dalam graph.
        edges: List of edges (u, v, weight).
        start_node: Node awal.
        
    Returns:
        Tuple[Optional[Dict[Any, float]], bool]: 
            - Dictionary jarak (None jika ada negative cycle).
            - Boolean yang bernilai True jika ada negative cycle.
    """
    # Inisialisasi jarak
    distances = {v: float('inf') for v in vertices}
    distances[start_node] = 0
    
    # Relax semua edges sebanyak V-1 kali
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                
    # Cek negative cycle (Relax satu kali lagi)
    has_negative_cycle = False
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            has_negative_cycle = True
            break
            
    if has_negative_cycle:
        return None, True
        
    return distances, False

if __name__ == "__main__":
    # Test Cases
    print("Running Bellman-Ford Tests...")
    
    # Test Case 1: Graph tanpa negative cycle
    # 0 -> 1 (4)
    # 0 -> 2 (5)
    # 1 -> 2 (-2)
    # 1 -> 3 (6)
    # 2 -> 3 (1)
    
    vertices = [0, 1, 2, 3]
    edges = [
        (0, 1, 4),
        (0, 2, 5),
        (1, 2, -2),
        (1, 3, 6),
        (2, 3, 1)
    ]
    
    dist, has_cycle = bellman_ford(vertices, edges, 0)
    
    print(f"Distances: {dist}")
    print(f"Has Negative Cycle: {has_cycle}")
    
    assert has_cycle == False
    assert dist[0] == 0
    assert dist[1] == 4
    assert dist[2] == 2 # 0 -> 1 -> 2 (4 + (-2) = 2) yang lebih baik dari 0 -> 2 (5)
    assert dist[3] == 3 # 0 -> 1 -> 2 -> 3 (4 + (-2) + 1 = 3)
    
    # Test Case 2: Graph dengan negative cycle
    # 0 -> 1 (1)
    # 1 -> 2 (-1)
    # 2 -> 0 (-1) -> Cycle 0-1-2 total bobot -1
    
    vertices_cycle = [0, 1, 2]
    edges_cycle = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 0, -1)
    ]
    
    dist_cycle, has_cycle_2 = bellman_ford(vertices_cycle, edges_cycle, 0)
    
    print(f"Distances (Cycle): {dist_cycle}")
    print(f"Has Negative Cycle: {has_cycle_2}")
    
    assert has_cycle_2 == True
    assert dist_cycle is None
    
    print("All Bellman-Ford tests passed!")
