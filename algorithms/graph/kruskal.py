"""
Description:
    [EN] Kruskal’s algorithm finds a Minimum Spanning Tree (MST) of a connected, undirected, weighted graph by sorting edges by weight and greedily adding them if they don’t form a cycle.
    [ID] Algoritma Kruskal menemukan Minimum Spanning Tree (MST) dari graf tak berarah berbobot yang terhubung dengan mengurutkan sisi berdasarkan bobot dan menambahkannya secara greedy jika tidak membentuk siklus.

Implementation Details:
    [EN]
    - Sort all edges ascending by weight.
    - Use Disjoint Set Union (DSU) with path compression and union by rank to detect cycles.
    - Add an edge to MST when its endpoints are in different sets.
    - Time O(E log E) (or O(E log V)); space O(V + E).
    [ID]
    - Urutkan semua sisi menaik berdasarkan bobot.
    - Gunakan Disjoint Set Union (DSU) dengan path compression dan union by rank untuk mendeteksi siklus.
    - Tambahkan sisi ke MST saat kedua ujungnya berada pada himpunan yang berbeda.
    - Waktu O(E log E) (atau O(E log V)); ruang O(V + E).

Usage Documentation:
    [EN]
    - Input: number of vertices and list of edges (u, v, weight).
    - Call `kruskal(V, edges)` to get `(mst_edges, total_weight)`.
    [ID]
    - Input: jumlah simpul dan daftar sisi (u, v, bobot).
    - Panggil `kruskal(V, edges)` untuk mendapatkan `(mst_edges, total_weight)`.

Examples:
    >>> V = 5
    >>> E = [(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]
    >>> mst, cost = kruskal(V, E)
    >>> cost
    16
"""

from typing import List, Tuple

class DSU:
    """Disjoint Set Union (DSU) with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        """Finds the representative of the set containing i."""
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """Unions the sets containing i and j. Returns True if merged."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.rank[root_i] == self.rank[root_j]:
                    self.rank[root_i] += 1
            return True
        return False

def kruskal(vertices: int, edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Kruskal's algorithm to find Minimum Spanning Tree (MST).
    
    Args:
        vertices: Number of vertices (0 to vertices-1)
        edges: List of tuples (u, v, weight)
        
    Returns:
        Tuple containing:
        - List of edges in MST
        - Total weight of MST
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_weight = 0
    dsu = DSU(vertices)
    
    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            mst_weight += w
            
    return mst_edges, mst_weight

if __name__ == "__main__":
    # Test case
    # Graph:
    #     2    3
    # (0)--(1)--(2)
    #  |   / \   |
    # 6| 8/   \5 |7
    #  | /     \ |
    # (3)-------(4)
    #      9
    
    V = 5
    E = [
        (0, 1, 2), (0, 3, 6),
        (1, 2, 3), (1, 3, 8), (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]
    
    mst, cost = kruskal(V, E)
    print(f"MST Edges: {mst}")
    print(f"MST Cost: {cost}")
    
    # Expected MST: (0,1,2), (1,2,3), (1,4,5), (0,3,6) -> Cost: 16
    assert cost == 16
    assert len(mst) == V - 1
    
    print("All test cases passed!")
