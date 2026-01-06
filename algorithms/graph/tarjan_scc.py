"""
Description:
    [EN] Tarjan’s algorithm computes Strongly Connected Components (SCCs) in a directed graph using a single DFS, maintaining discovery times and low-link values.
    [ID] Algoritma Tarjan menghitung Strongly Connected Components (SCC) pada graf berarah menggunakan satu DFS, menyimpan waktu penemuan dan nilai low-link.

Implementation Details:
    [EN]
    - Maintains arrays disc[u] and low[u]; a stack tracks the current DFS path.
    - When low[u] == disc[u], u is a root of an SCC; pop stack until u.
    - Runs in O(V + E) time.
    [ID]
    - Menjaga larik disc[u] dan low[u]; sebuah stack melacak jalur DFS saat ini.
    - Ketika low[u] == disc[u], u adalah akar SCC; pop stack sampai u.
    - Berjalan dalam O(V + E) waktu.

Usage Documentation:
    [EN]
    - Create `TarjanSCC(n)`, add directed edges with `add_edge(u, v)`.
    - Call `get_sccs()` to obtain a list of SCCs.
    [ID]
    - Buat `TarjanSCC(n)`, tambahkan sisi berarah dengan `add_edge(u, v)`.
    - Panggil `get_sccs()` untuk mendapatkan daftar SCC.

Examples:
    >>> g = TarjanSCC(5)
    >>> g.add_edge(1, 0); g.add_edge(0, 2); g.add_edge(2, 1); g.add_edge(0, 3); g.add_edge(3, 4)
    >>> sorted([sorted(c) for c in g.get_sccs()], key=lambda x: x[0])
    [[0, 1, 2], [3], [4]]
"""
from collections import defaultdict
from typing import List

class TarjanSCC:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def get_sccs(self) -> List[List[int]]:
        disc = [-1] * self.V
        low = [-1] * self.V
        on_stack = [False] * self.V
        stack: List[int] = []
        sccs: List[List[int]] = []

        def dfs(u: int):
            self.time += 1
            disc[u] = low[u] = self.time
            stack.append(u)
            on_stack[u] = True
            for v in self.graph[u]:
                if disc[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif on_stack[v]:
                    low[u] = min(low[u], disc[v])
            if low[u] == disc[u]:
                comp: List[int] = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp.append(w)
                    if w == u:
                        break
                sccs.append(comp)

        for i in range(self.V):
            if disc[i] == -1:
                dfs(i)
        return sccs

if __name__ == "__main__":
    g = TarjanSCC(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    sccs = g.get_sccs()
    sccs_sorted = [sorted(c) for c in sccs]
    sccs_sorted.sort(key=lambda x: x[0])
    print(f"SCCs: {sccs_sorted}")
    assert [0, 1, 2] in sccs_sorted
    assert [3] in sccs_sorted
    assert [4] in sccs_sorted
    print("All Tarjan SCC tests passed!")
