"""
Description:
    [EN] Prim’s algorithm builds a Minimum Spanning Tree (MST) of a connected, weighted, undirected graph by greedily growing a tree from a start node using the cheapest edge crossing the cut.
    [ID] Algoritma Prim membangun Minimum Spanning Tree (MST) pada graf tak berarah berbobot dan terhubung dengan menumbuhkan pohon secara greedy dari simpul awal menggunakan sisi termurah yang melintasi batas (cut).

Implementation Details:
    [EN]
    - Uses a min-priority queue of edges (weight, from, to) seeded with the start node.
    - Maintains a visited set; at each step picks the cheapest edge to an unvisited vertex.
    - Time O(E log V) with a binary heap; space O(E).
    [ID]
    - Menggunakan antrian prioritas minimum berisi sisi (bobot, dari, ke) yang diinisialisasi dari simpul awal.
    - Menjaga himpunan visited; setiap langkah memilih sisi termurah ke simpul yang belum dikunjungi.
    - Waktu O(E log V) dengan binary heap; ruang O(E).

Usage Documentation:
    [EN]
    - Input: adjacency dictionary graph[u] = [(v, w), ...] for an undirected graph (store both directions).
    - Call `prim_mst(graph, start_node)` to get `(total_weight, mst_edges)` where edges are (u, v, w).
    [ID]
    - Input: dictionary ketetanggaan graph[u] = [(v, w), ...] untuk graf tak berarah (simpan dua arah).
    - Panggil `prim_mst(graph, start_node)` untuk mendapatkan `(total_weight, mst_edges)` dengan format sisi (u, v, w).

Examples:
    >>> graph = {0:[(1,2),(3,6)], 1:[(0,2),(2,3),(3,8),(4,5)], 2:[(1,3),(4,7)], 3:[(0,6),(1,8),(4,9)], 4:[(1,5),(2,7),(3,9)]}
    >>> prim_mst(graph, 0)[0]
    16
"""

import heapq
from typing import Dict, List, Tuple, Any, Optional

# Graph type alias: Dict[Node, List[Tuple[Neighbor, Weight]]]
Graph = Dict[Any, List[Tuple[Any, int]]]

def prim_mst(graph: Graph, start_node: Any) -> Tuple[int, List[Tuple[Any, Any, int]]]:
    """
    Mengimplementasikan algoritma Prim untuk mencari MST.
    
    Args:
        graph: Adjacency dictionary dimana key adalah node dan value adalah list of (neighbor, weight).
        start_node: Node awal untuk memulai algoritma.
        
    Returns:
        Tuple[int, List[Tuple[Any, Any, int]]]: (Total bobot MST, List edge MST)
        Edge format: (u, v, weight)
    """
    mst_weight = 0
    mst_edges = []
    visited = set()
    
    # Priority Queue: (weight, from_node, to_node)
    # Mulai dengan edge fiktif ke start_node dengan bobot 0
    pq = [(0, None, start_node)]
    
    while pq:
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
            
        visited.add(v)
        
        # Jika bukan node awal, tambahkan ke hasil MST
        if u is not None:
            mst_weight += weight
            mst_edges.append((u, v, weight))
            
        # Tambahkan neighbor ke priority queue
        if v in graph:
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (w, v, neighbor))
                    
    return mst_weight, mst_edges

if __name__ == "__main__":
    # Test Cases
    print("Running Prim's Algorithm Tests...")
    
    # Contoh Graph:
    # 0 --(2)--> 1
    # 0 --(6)--> 3
    # 1 --(3)--> 2
    # 1 --(8)--> 3
    # 1 --(5)--> 4
    # 2 --(7)--> 4
    # 3 --(9)--> 4
    
    # Representasi Graph (Undirected)
    # Perlu menambahkan edge dua arah
    graph_data = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    
    total_weight, edges = prim_mst(graph_data, 0)
    
    print(f"Total Weight MST: {total_weight}")
    print("Edges in MST:")
    for u, v, w in edges:
        print(f"{u} - {v} (weight: {w})")
        
    # Verifikasi Manual
    # MST yang diharapkan:
    # 0-1 (2)
    # 1-2 (3)
    # 1-4 (5)
    # 0-3 (6) -> Salah, 0-3 (6) vs 1-3 (8). Pilih 0-3.
    # Total: 2 + 3 + 5 + 6 = 16
    
    # Tunggu, mari kita trace manual:
    # Mulai 0. PQ: [(2, 0, 1), (6, 0, 3)]
    # Pop (2, 0, 1). MST: {(0,1)}. Visited: {0, 1}.
    # Add neighbors of 1: (3, 1, 2), (8, 1, 3), (5, 1, 4).
    # PQ: [(3, 1, 2), (5, 1, 4), (6, 0, 3), (8, 1, 3)]
    # Pop (3, 1, 2). MST: {(0,1), (1,2)}. Visited: {0, 1, 2}.
    # Add neighbors of 2: (7, 2, 4).
    # PQ: [(5, 1, 4), (6, 0, 3), (7, 2, 4), (8, 1, 3)]
    # Pop (5, 1, 4). MST: {(0,1), (1,2), (1,4)}. Visited: {0, 1, 2, 4}.
    # Add neighbors of 4: (9, 4, 3).
    # PQ: [(6, 0, 3), (7, 2, 4), (8, 1, 3), (9, 4, 3)]
    # Pop (6, 0, 3). MST: {(0,1), (1,2), (1,4), (0,3)}. Visited: {0, 1, 2, 4, 3}.
    # Semua visited. Selesai.
    # Total Weight: 2 + 3 + 5 + 6 = 16.
    
    assert total_weight == 16
    assert len(edges) == 4
    
    print("All Prim's Algorithm tests passed!")
