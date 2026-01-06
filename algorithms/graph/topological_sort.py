"""
Description:
    [EN] Topological Sort orders the vertices of a Directed Acyclic Graph (DAG) such that for every edge u -> v, u appears before v. Commonly used in task scheduling, build systems, and dependency resolution.
    [ID] Topological Sort mengurutkan simpul pada Directed Acyclic Graph (DAG) sehingga untuk setiap sisi u -> v, u muncul sebelum v. Umum digunakan pada penjadwalan tugas, sistem build, dan resolusi dependensi.

Implementation Details:
    [EN]
    - DFS-based approach pushes a vertex to the stack after visiting all its descendants.
    - Reverse the stack to obtain the topological order.
    - Time O(V + E), space O(V).
    [ID]
    - Pendekatan berbasis DFS menambahkan simpul ke stack setelah mengunjungi semua turunannya.
    - Balikkan stack untuk memperoleh urutan topologis.
    - Waktu O(V + E), ruang O(V).

Usage Documentation:
    [EN]
    - Input: adjacency dictionary graph[u] = [v1, v2, ...].
    - Call `topological_sort(graph)` to get a list of vertices in topological order.
    [ID]
    - Input: dictionary ketetanggaan graph[u] = [v1, v2, ...].
    - Panggil `topological_sort(graph)` untuk memperoleh daftar simpul dalam urutan topologis.

Examples:
    >>> graph = {5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
    >>> order = topological_sort(graph)
    >>> set(order) == {0, 1, 2, 3, 4, 5}
    True
"""

from typing import Dict, List, Set, Any

Graph = Dict[Any, List[Any]]

def topological_sort(graph: Graph) -> List[Any]:
    """
    Melakukan Topological Sort pada DAG menggunakan DFS.
    
    Args:
        graph: Adjacency dictionary.
        
    Returns:
        List[Any]: List node dalam urutan topologis.
    """
    visited: Set[Any] = set()
    stack: List[Any] = []
    
    # Ambil semua node unik dari graph (baik key maupun value)
    nodes: Set[Any] = set(graph.keys())
    for neighbors in graph.values():
        for node in neighbors:
            nodes.add(node)
            
    def dfs(node: Any):
        visited.add(node)
        
        # Kunjungi semua neighbor yang belum dikunjungi
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        # Setelah semua neighbor diproses, tambahkan ke stack
        stack.append(node)
        
    for node in nodes:
        if node not in visited:
            dfs(node)
            
    # Hasil topological sort adalah reverse dari stack
    return stack[::-1]

if __name__ == "__main__":
    # Test cases
    print("Running Topological Sort Tests...")
    
    # Graph:
    # 5 -> 0, 5 -> 2
    # 4 -> 0, 4 -> 1
    # 2 -> 3
    # 3 -> 1
    graph_data = {
        5: [0, 2],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }
    
    result = topological_sort(graph_data)
    print(f"Topological Sort: {result}")
    
    # Verifikasi urutan
    # 5 harus sebelum 2 dan 0
    # 4 harus sebelum 0 dan 1
    # 2 harus sebelum 3
    # 3 harus sebelum 1
    
    pos = {node: i for i, node in enumerate(result)}
    
    assert pos[5] < pos[2]
    assert pos[5] < pos[0]
    assert pos[4] < pos[0]
    assert pos[4] < pos[1]
    assert pos[2] < pos[3]
    assert pos[3] < pos[1]
    
    print("All Topological Sort tests passed!")
