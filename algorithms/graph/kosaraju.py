"""
Description:
    [EN] Kosaraju’s algorithm finds Strongly Connected Components (SCCs) in a directed graph. An SCC is a maximal set of vertices where every vertex is reachable from every other within the set.
    [ID] Algoritma Kosaraju menemukan Strongly Connected Components (SCC) pada graf berarah. SCC adalah himpunan maksimal simpul di mana setiap simpul dapat menjangkau simpul lain di dalam himpunan tersebut.

Implementation Details:
    [EN]
    - First DFS to compute finish times and push vertices onto a stack.
    - Build the transpose graph by reversing all edges.
    - Second DFS in stack order on the transpose to collect SCCs.
    - Runs in O(V + E) time and O(V + E) space.
    [ID]
    - DFS pertama untuk menghitung waktu selesai dan menempatkan simpul ke dalam stack.
    - Bangun graf transpose dengan membalik semua sisi.
    - DFS kedua mengikuti urutan stack pada graf transpose untuk mengumpulkan SCC.
    - Berjalan dalam O(V + E) waktu dan O(V + E) ruang.

Usage Documentation:
    [EN]
    - Create `Kosaraju(n)` with number of vertices.
    - Add directed edges using `add_edge(u, v)`.
    - Call `get_sccs()` to obtain a list of SCCs (each SCC is a list of vertices).
    [ID]
    - Buat `Kosaraju(n)` dengan jumlah simpul.
    - Tambahkan sisi berarah menggunakan `add_edge(u, v)`.
    - Panggil `get_sccs()` untuk mendapatkan daftar SCC (setiap SCC adalah daftar simpul).

Examples:
    >>> g = Kosaraju(5)
    >>> g.add_edge(1, 0); g.add_edge(0, 2); g.add_edge(2, 1); g.add_edge(0, 3); g.add_edge(3, 4)
    >>> sccs = g.get_sccs()
    >>> sorted([sorted(s) for s in sccs], key=lambda x: x[0])
    [[0, 1, 2], [3], [4]]
"""

from collections import defaultdict
from typing import List, Dict, Set

class Kosaraju:
    def __init__(self, vertices: int):
        """
        Initialize graph with number of vertices.
        Vertices are 0-indexed.
        """
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        """Adds a directed edge from u to v."""
        self.graph[u].append(v)

    def _fill_order(self, v: int, visited: List[bool], stack: List[int]):
        """
        DFS to fill the stack with vertices in order of finishing times.
        """
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self._fill_order(i, visited, stack)
        stack.append(v)

    def _get_transpose(self):
        """
        Returns the transpose of the graph.
        """
        g = Kosaraju(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def _dfs_util(self, v: int, visited: List[bool], component: List[int]):
        """
        DFS utility for the second pass (on transposed graph).
        """
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited, component)

    def get_sccs(self) -> List[List[int]]:
        """
        Returns a list of Strongly Connected Components.
        Each SCC is a list of vertex indices.
        """
        stack = []
        visited = [False] * self.V

        # Step 1: Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self._fill_order(i, visited, stack)

        # Step 2: Create a reversed graph
        gr = self._get_transpose()

        # Step 3: Process all vertices in order defined by stack
        visited = [False] * self.V
        sccs = []
        
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr._dfs_util(i, visited, component)
                sccs.append(component)
                
        return sccs

if __name__ == "__main__":
    print("Kosaraju's Algorithm Tests...")
    
    # Create a graph
    # 0 -> 2
    # 2 -> 1
    # 1 -> 0
    # 0 -> 3
    # 3 -> 4
    g = Kosaraju(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    print("SCCs in graph:")
    sccs = g.get_sccs()
    for scc in sccs:
        print(scc)
        
    # Expected SCCs:
    # {0, 1, 2} form a cycle
    # {3} is separate (can't go back to 0, 1, 2)
    # {4} is separate (can't go back to 3)
    
    # Since order depends on stack, we sort for validation
    sccs_sorted = [sorted(scc) for scc in sccs]
    sccs_sorted.sort(key=lambda x: x[0])
    
    print(f"Sorted SCCs: {sccs_sorted}")
    
    # Validating
    # Note: Depending on iteration order, we should get [0, 1, 2], [3], [4]
    # Check lengths
    assert len(sccs) == 3
    assert [0, 1, 2] in sccs_sorted
    assert [3] in sccs_sorted
    assert [4] in sccs_sorted
    
    print("All Kosaraju's Algorithm tests passed!")
