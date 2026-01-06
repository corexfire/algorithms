"""
Description:
    [EN] Dijkstra’s algorithm computes the shortest-path distances from a source node in a weighted graph with non‑negative edge weights. It uses a min-priority queue to always expand the current closest node.
    [ID] Algoritma Dijkstra menghitung jarak lintasan terpendek dari sebuah node sumber pada graf berbobot dengan bobot tepi non‑negatif. Ia menggunakan antrian prioritas minimum untuk selalu mengembangkan node terdekat saat ini.

Implementation Details:
    [EN]
    - Uses Python `heapq` as a min-priority queue storing (distance, node).
    - Performs relaxation when a shorter path to a neighbor is found.
    - Ignores stale heap entries by comparing popped distance with the current best distance.
    [ID]
    - Menggunakan `heapq` Python sebagai antrian prioritas minimum yang menyimpan (jarak, node).
    - Melakukan relaksasi saat ditemukan jalur lebih pendek ke tetangga.
    - Mengabaikan entri heap yang usang dengan membandingkan jarak yang di-pop dengan jarak terbaik saat ini.

Usage Documentation:
    [EN]
    - Input: adjacency dict mapping node -> list of (neighbor, weight).
    - Call `dijkstra(graph, start_node)` to obtain a dict of shortest distances.
    - Unreachable nodes are omitted from the result.
    [ID]
    - Input: dictionary ketetanggaan memetakan node -> daftar (tetangga, bobot).
    - Panggil `dijkstra(graph, start_node)` untuk mendapatkan dictionary jarak terpendek.
    - Node yang tidak terjangkau tidak muncul pada hasil.

Examples:
    >>> graph = {'A':[('B',1),('D',4)], 'B':[('C',3),('E',2)], 'C':[], 'D':[('E',1)], 'E':[('C',5)]}
    >>> dist = dijkstra(graph, 'A')
    >>> dist['A'], dist['B'], dist['D'], dist['E'], dist['C']
    (0, 1, 4, 3, 4)
"""

import heapq
from typing import Dict, List, Tuple, Any, Optional

# Graph direpresentasikan sebagai Dict[Node, List[Tuple[Neighbor, Weight]]]
Graph = Dict[Any, List[Tuple[Any, int]]]

def dijkstra(graph: Graph, start_node: Any) -> Dict[Any, int]:
    """
    Implementasi Dijkstra menggunakan Priority Queue (heapq).
    
    Args:
        graph: Adjacency dictionary di mana key adalah node dan value adalah 
               list of tuples (neighbor, weight).
        start_node: Node awal.
        
    Returns:
        Dict[Any, int]: Dictionary berisi jarak terpendek dari start_node ke setiap node.
                        Jarak ke node yang tidak terjangkau tidak dimasukkan (atau bisa dianggap infinity).
    """
    # Jarak ke semua node diinisialisasi tak hingga, kecuali start_node = 0
    # Kita gunakan dictionary untuk menyimpan jarak terpendek yang ditemukan sejauh ini
    distances: Dict[Any, int] = {start_node: 0}
    
    # Priority queue menyimpan tuple (jarak, node)
    # Diinisialisasi dengan start_node dengan jarak 0
    pq: List[Tuple[int, Any]] = [(0, start_node)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # Jika jarak yang diambil dari PQ lebih besar dari jarak yang sudah dicatat, skip
        # (Ini terjadi karena kita bisa push node yang sama berkali-kali dengan jarak berbeda)
        if current_dist > distances.get(current_node, float('inf')):
            continue
            
        # Eksplorasi tetangga
        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                
                # Jika ditemukan jalur yang lebih pendek
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    
    return distances

if __name__ == "__main__":
    # Test cases
    print("Running Dijkstra Tests...")
    
    # Graph:
    # A --(1)--> B --(3)--> C
    # |          |          ^
    # (4)        (2)        (1)
    # v          v          |
    # D --(1)--> E --(5)----|
    
    graph_data: Graph = {
        'A': [('B', 1), ('D', 4)],
        'B': [('C', 3), ('E', 2)],
        'C': [],
        'D': [('E', 1)],
        'E': [('C', 5)]
    }
    
    start = 'A'
    distances = dijkstra(graph_data, start)
    print(f"Shortest paths from {start}: {distances}")
    
    # Verifikasi manual:
    # A -> A = 0
    # A -> B = 1
    # A -> D = 4
    # A -> E: min(A->B->E (1+2=3), A->D->E (4+1=5)) = 3
    # A -> C: min(A->B->C (1+3=4), A->E->C (3+5=8)) = 4
    
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert distances['C'] == 4
    assert distances['D'] == 4
    assert distances['E'] == 3
    
    # Test case node terisolasi
    graph_iso: Graph = {
        'A': [('B', 10)],
        'B': [],
        'C': []
    }
    dist_iso = dijkstra(graph_iso, 'A')
    assert 'C' not in dist_iso # C tidak terjangkau
    assert dist_iso['B'] == 10
    
    print("All Dijkstra tests passed!")
