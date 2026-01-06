"""
Description:
    [EN] Depth-First Search (DFS) explores a graph by going as deep as possible along each branch before backtracking. It can be implemented recursively or iteratively with a stack and is useful for topological sorting, cycle detection, and connected components.
    [ID] Pencarian Mendalam Pertama (DFS) menelusuri graf dengan menyelam sedalam mungkin pada setiap cabang sebelum mundur. Dapat diimplementasikan secara rekursif atau iteratif dengan stack dan berguna untuk topological sort, deteksi siklus, serta komponen terhubung.

Implementation Details:
    [EN]
    - Recursive version leverages the call stack to backtrack.
    - Iterative version uses an explicit LIFO stack to manage traversal.
    - Time O(V + E), space O(V) for visited and stack/recursion.
    [ID]
    - Versi rekursif memanfaatkan call stack untuk backtracking.
    - Versi iteratif menggunakan stack LIFO eksplisit untuk mengelola traversal.
    - Waktu O(V + E), ruang O(V) untuk visited dan stack/rekursi.

Usage Documentation:
    [EN]
    - Input: adjacency dictionary mapping node -> list of neighbors.
    - Call `dfs_recursive(graph, start_node)` or `dfs_iterative(graph, start_node)` to get visited order.
    [ID]
    - Input: dictionary ketetanggaan memetakan node -> daftar tetangga.
    - Panggil `dfs_recursive(graph, start_node)` atau `dfs_iterative(graph, start_node)` untuk urutan kunjungan.

Examples:
    >>> graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['B', 'C', 'F'], 'F': ['E']}
    >>> result = dfs_recursive(graph, 'A')
    >>> len(result) == 6
    True
"""
from typing import Dict, List, Set, Any

# Representasi Graph menggunakan Dictionary: {Node: [Neighbors]}
Graph = Dict[Any, List[Any]]

def dfs_recursive(graph: Graph, start_node: Any, visited: Set[Any] = None) -> List[Any]:
    """
    Implementasi DFS secara rekursif.
    """
    if visited is None:
        visited = set()
        
    visited.add(start_node)
    path = [start_node]
    
    if start_node in graph:
        for neighbor in graph[start_node]:
            if neighbor not in visited:
                path.extend(dfs_recursive(graph, neighbor, visited))
                
    return path

def dfs_iterative(graph: Graph, start_node: Any) -> List[Any]:
    """
    Implementasi DFS secara iteratif menggunakan stack.
    Catatan: Urutan kunjungan mungkin berbeda dengan rekursif tergantung urutan push ke stack.
    """
    visited = set()
    stack = [start_node]
    path = []
    
    while stack:
        vertex = stack.pop() # Ambil dari belakang (LIFO)
        
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            
            # Tambahkan neighbor ke stack (reverse order agar yang pertama di list diproses duluan jika diinginkan)
            if vertex in graph:
                for neighbor in reversed(graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
    return path

if __name__ == "__main__":
    # Test cases
    print("Running DFS Tests...")
    
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
    
    # Test Recursive
    start = 'A'
    res_rec = dfs_recursive(graph_data, start)
    print(f"DFS Recursive from {start}: {res_rec}")
    
    # Validasi path (Salah satu kemungkinan path yang valid)
    # A -> B -> D -> E -> F -> C (jika B dipilih sebelum C)
    # Pastikan semua node yang terhubung dikunjungi
    expected_nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
    assert set(res_rec) == expected_nodes, "Recursive DFS failed to visit all connected nodes"
    
    # Test Iterative
    res_iter = dfs_iterative(graph_data, start)
    print(f"DFS Iterative from {start}: {res_iter}")
    assert set(res_iter) == expected_nodes, "Iterative DFS failed to visit all connected nodes"
    
    # Test Disconnected
    graph_disconnected = {
        '1': ['2'],
        '2': ['1'],
        '3': []
    }
    res_disc = dfs_recursive(graph_disconnected, '1')
    assert '3' not in res_disc
    
    print("All DFS tests passed!")
