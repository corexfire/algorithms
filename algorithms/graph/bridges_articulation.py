"""
Description:
    [EN] Bridge and Articulation Point detection in undirected graphs using DFS and low-link values. A bridge is an edge whose removal increases the number of connected components; an articulation point is a vertex whose removal increases components.
    [ID] Deteksi Bridge dan Titik Artikulas (Articulation Point) pada graf tak berarah menggunakan DFS dan nilai low-link. Bridge adalah sisi yang jika dihapus menambah jumlah komponen terhubung; titik artikulas adalah simpul yang jika dihapus menambah komponen.

Implementation Details:
    [EN]
    - Uses discovery times (disc) and low-link values (low) to identify bridges and articulation points.
    - Bridge condition: low[v] > disc[u] for edge u–v.
    - Articulation conditions: root with >1 children; or for non-root, low[v] >= disc[u].
    [ID]
    - Menggunakan waktu penemuan (disc) dan nilai low-link (low) untuk mengidentifikasi bridge dan titik artikulas.
    - Kondisi bridge: low[v] > disc[u] untuk sisi u–v.
    - Kondisi artikulas: root dengan >1 anak; atau untuk non-root, low[v] >= disc[u].

Usage Documentation:
    [EN]
    - Create `GraphUndirected(n)`, add undirected edges with `add_edge(u, v)`.
    - Call `find_bridges()` and `find_articulation_points()` to get results.
    [ID]
    - Buat `GraphUndirected(n)`, tambahkan sisi tak berarah dengan `add_edge(u, v)`.
    - Panggil `find_bridges()` dan `find_articulation_points()` untuk mendapatkan hasil.

Examples:
    >>> g = GraphUndirected(5)
    >>> g.add_edge(0,1); g.add_edge(1,2); g.add_edge(2,0); g.add_edge(1,3); g.add_edge(3,4)
    >>> bridges = g.find_bridges(); aps = g.find_articulation_points()
    >>> (3,4) in bridges or (4,3) in bridges, 1 in aps and 3 in aps
    (True, True)
"""
from collections import defaultdict
from typing import List, Tuple

class GraphUndirected:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_bridges(self) -> List[Tuple[int, int]]:
        visited = [False] * self.V
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        bridges: List[Tuple[int, int]] = []

        def dfs(u: int):
            visited[u] = True
            self.time += 1
            disc[u] = low[u] = self.time
            for v in self.graph[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((u, v))
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        for i in range(self.V):
            if not visited[i]:
                dfs(i)
        return bridges

    def find_articulation_points(self) -> List[int]:
        visited = [False] * self.V
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        ap = [False] * self.V

        def dfs(u: int):
            visited[u] = True
            self.time += 1
            disc[u] = low[u] = self.time
            children = 0
            for v in self.graph[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        for i in range(self.V):
            if not visited[i]:
                dfs(i)
        return [i for i, val in enumerate(ap) if val]

if __name__ == "__main__":
    g = GraphUndirected(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    bridges = g.find_bridges()
    aps = g.find_articulation_points()
    print(f"Bridges: {bridges}")
    print(f"Articulation Points: {aps}")
    assert (3, 4) in bridges or (4, 3) in bridges
    assert 1 in aps and 3 in aps
    print("All Bridges & Articulation Points tests passed!")
