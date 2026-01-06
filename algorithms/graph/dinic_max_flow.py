"""
Description:
    [EN] Dinic’s algorithm computes maximum flow using BFS to build level graphs and DFS to send blocking flows, achieving better performance on many networks.
    [ID] Algoritma Dinic menghitung aliran maksimum menggunakan BFS untuk membangun level graph dan DFS untuk mengirim blocking flow, memberikan kinerja lebih baik pada banyak jaringan.

Implementation Details:
    [EN]
    - Level graph via BFS ensures edges go from level i to i+1.
    - DFS pushes flow along admissible edges until blocking flow is reached.
    - Runs in O(E V^2) in general; faster on unit networks.
    [ID]
    - Level graph melalui BFS memastikan sisi berjalan dari level i ke i+1.
    - DFS mendorong aliran sepanjang sisi yang admissible hingga blocking flow tercapai.
    - Berjalan O(E V^2) secara umum; lebih cepat pada jaringan unit.

Usage Documentation:
    [EN]
    - Create `Dinic(n)`, add edges with `add_edge(u, v, cap)`.
    - Call `max_flow(s, t)` to obtain the maximum flow value.
    [ID]
    - Buat `Dinic(n)`, tambahkan sisi dengan `add_edge(u, v, cap)`.
    - Panggil `max_flow(s, t)` untuk memperoleh nilai aliran maksimum.

Examples:
    >>> g = Dinic(4)
    >>> g.add_edge(0, 1, 100); g.add_edge(0, 2, 100); g.add_edge(1, 2, 1); g.add_edge(1, 3, 100); g.add_edge(2, 3, 100)
    >>> g.max_flow(0, 3)
    200
"""
from collections import deque
from typing import List

class Dinic:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[dict]] = [[] for _ in range(n)]
        self.level = [0] * n
        self.it = [0] * n

    def add_edge(self, u: int, v: int, cap: int):
        a = {"to": v, "rev": None, "cap": cap}
        b = {"to": u, "rev": None, "cap": 0}
        a["rev"] = len(self.adj[v])
        b["rev"] = len(self.adj[u])
        self.adj[u].append(a)
        self.adj[v].append(b)

    def bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                if e["cap"] > 0 and self.level[e["to"]] < 0:
                    self.level[e["to"]] = self.level[u] + 1
                    q.append(e["to"])
        return self.level[t] >= 0

    def dfs(self, u: int, t: int, f: int) -> int:
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            e = self.adj[u][i]
            if e["cap"] > 0 and self.level[e["to"]] == self.level[u] + 1:
                d = self.dfs(e["to"], t, min(f, e["cap"]))
                if d > 0:
                    e["cap"] -= d
                    rev = self.adj[e["to"]][e["rev"]]
                    rev["cap"] += d
                    return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

if __name__ == "__main__":
    g = Dinic(4)
    g.add_edge(0, 1, 100)
    g.add_edge(0, 2, 100)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 100)
    g.add_edge(2, 3, 100)
    mf = g.max_flow(0, 3)
    print(f"Max flow: {mf}")
    assert mf == 200
    print("All Dinic's Max Flow tests passed!")
