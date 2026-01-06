"""
Description:
    [EN] Breadth-First Search (BFS) traverses a graph level by level starting from a source node. It is commonly used to compute shortest paths in unweighted graphs and to explore connected components.
    [ID] Pencarian Melebar Pertama (BFS) menelusuri graf per level mulai dari simpul sumber. BFS umum digunakan untuk menghitung jalur terpendek pada graf tanpa bobot dan mengeksplorasi komponen terhubung.

Implementation Details:
    [EN]
    - Maintains a FIFO queue to process nodes in increasing distance from the start.
    - Uses a visited set to prevent revisiting nodes and infinite loops.
    - Time complexity O(V + E); space O(V).
    [ID]
    - Menjaga antrian FIFO untuk memproses simpul berdasarkan jarak yang meningkat dari awal.
    - Menggunakan himpunan visited untuk mencegah kunjungan ulang dan loop tak hingga.
    - Kompleksitas waktu O(V + E); ruang O(V).

Usage Documentation:
    [EN]
    - Input: adjacency dictionary mapping node -> list of neighbors.
    - Call `bfs(graph, start_node)` to obtain the traversal order.
    [ID]
    - Input: dictionary ketetanggaan memetakan node -> daftar tetangga.
    - Panggil `bfs(graph, start_node)` untuk mendapatkan urutan kunjungan.

Examples:
    >>> graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['B', 'C', 'F'], 'F': ['E']}
    >>> bfs(graph, 'A')
    ['A', 'B', 'C', 'D', 'E', 'F']
"""
from typing import Dict, List, Set, Any, Deque
from collections import deque

# Representasi Graph menggunakan Dictionary: {Node: [Neighbors]}
Graph = Dict[Any, List[Any]]

def bfs(graph: Graph, start_node: Any) -> List[Any]:
    """
    Implementasi Breadth First Search (BFS).
    Menggunakan queue untuk melacak node yang akan dikunjungi.
    
    Args:
        graph: Adjacency list graph.
        start_node: Node awal traversal.
        
    Returns:
        List[Any]: Urutan node yang dikunjungi.
    """
    visited: Set[Any] = set()
    queue: Deque[Any] = deque([start_node])
    traversal_order: List[Any] = []
    
    visited.add(start_node)
    
    while queue:
        vertex = queue.popleft() # Ambil dari depan (FIFO)
        traversal_order.append(vertex)
        
        # Cek tetangga
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
    return traversal_order

if __name__ == "__main__":
    # Test cases
    print("Running BFS Tests...")
    
    # Graph sederhana
    # A -- B -- D
    # |    |
    # C -- E -- F
    graph_data = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['B', 'C', 'F'],
        'F': ['E']
    }
    
    start = 'A'
    result = bfs(graph_data, start)
    print(f"BFS from {start}: {result}")
    
    # Verifikasi level order (urutan pasti bisa bervariasi tergantung urutan list neighbor, 
    # tapi levelnya harus konsisten)
    # Level 0: A
    # Level 1: B, C
    # Level 2: D, E (dari B), E (dari C - visited)
    # Level 3: F
    # Possible valid BFS: A -> B -> C -> D -> E -> F or A -> C -> B -> E -> D -> F
    assert result[0] == 'A'
    assert set(result[1:3]) == {'B', 'C'}
    assert set(result[3:5]) == {'D', 'E'}
    assert result[5] == 'F'
    
    # Test case disconnected node (hanya akan traverse komponen terhubung)
    graph_disconnected = {
        'A': ['B'],
        'B': ['A'],
        'C': []
    }
    res_disc = bfs(graph_disconnected, 'A')
    print(f"BFS Disconnected from A: {res_disc}")
    assert 'C' not in res_disc
    
    print("All BFS tests passed!")
