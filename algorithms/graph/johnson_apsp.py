"""
Johnson's Algorithm for All-Pairs Shortest Paths
================================================

1. English Description
----------------------
Johnson's algorithm finds the shortest paths between all pairs of vertices in a weighted directed graph. It allows for negative edge weights (unlike Dijkstra) but detects negative cycles (like Bellman-Ford).

- **Logic**:
  1. Add a dummy source connected to all vertices with weight 0.
  2. Run Bellman-Ford to find shortest paths `h(v)` from dummy source. If negative cycle, abort.
  3. Reweight edges: `w'(u, v) = w(u, v) + h(u) - h(v)`. This ensures all weights are non-negative.
  4. Run Dijkstra's algorithm from every vertex using reweighted edges.
  5. Adjust distances back to original weights.
- **Time Complexity**: O(V * E * log V) (using binary heap Dijkstra) or O(V^2 * log V + V * E). This is better than Floyd-Warshall O(V^3) for sparse graphs.
- **Space Complexity**: O(V + E).

2. Indonesian Description (Deskripsi Bahasa Indonesia)
------------------------------------------------------
Algoritma Johnson mencari jalur terpendek antara semua pasangan simpul dalam graf berarah berbobot. Algoritma ini mengizinkan bobot sisi negatif (tidak seperti Dijkstra) tetapi mendeteksi siklus negatif (seperti Bellman-Ford).

- **Logika**:
  1. Tambahkan sumber dummy yang terhubung ke semua simpul dengan bobot 0.
  2. Jalankan Bellman-Ford untuk mencari jalur terpendek `h(v)` dari sumber dummy. Jika ada siklus negatif, batalkan.
  3. Hitung ulang bobot: `w'(u, v) = w(u, v) + h(u) - h(v)`. Ini memastikan semua bobot menjadi non-negatif.
  4. Jalankan algoritma Dijkstra dari setiap simpul menggunakan bobot baru.
  5. Sesuaikan jarak kembali ke bobot asli.
- **Kompleksitas Waktu**: O(V * E * log V) (menggunakan binary heap Dijkstra) atau O(V^2 * log V + V * E). Ini lebih baik daripada Floyd-Warshall O(V^3) untuk graf jarang (sparse).
- **Kompleksitas Ruang**: O(V + E).

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Use Cases / Kasus Penggunaan**: 
  - [EN] Routing in sparse networks where edge weights can be negative (e.g., financial arbitrage graphs, resource allocation).
  - [ID] Routing dalam jaringan jarang di mana bobot sisi bisa negatif (misalnya, graf arbitrase keuangan, alokasi sumber daya).
- **Performance / Performa**: 
  - [EN] Superior to Floyd-Warshall when the graph is sparse (E << V^2).
  - [ID] Lebih unggul daripada Floyd-Warshall ketika graf jarang (E << V^2).
- **Limitations / Batasan**: 
  - [EN] Fails if the graph contains a negative weight cycle.
  - [ID] Gagal jika graf mengandung siklus bobot negatif.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Input / Input**: 
  - [EN] Adjacency list `Graph = Dict[Any, List[Tuple[Any, int]]]`.
  - [ID] Daftar ketetanggaan `Graph = Dict[Any, List[Tuple[Any, int]]]`.
- **Output / Output**: 
  - [EN] Dictionary of dictionaries `dist[source][target] = distance`.
  - [ID] Kamus dari kamus `dist[source][target] = distance`.
- **Dependencies / Ketergantungan**: 
  - [EN] Uses `heapq` for Dijkstra. Internal `_bellman_ford` and `_dijkstra` implementations included.
  - [ID] Menggunakan `heapq` untuk Dijkstra. Implementasi internal `_bellman_ford` dan `_dijkstra` disertakan.
"""

from typing import Any, Dict, List, Tuple

Graph = Dict[Any, List[Tuple[Any, int]]]

def _bellman_ford(vertices: List[Any], edges: List[Tuple[Any, Any, int]], start: Any):
    dist = {v: float("inf") for v in vertices}
    dist[start] = 0
    for _ in range(len(vertices) - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None, True
    return dist, False

def _dijkstra(graph: Graph, start: Any) -> Dict[Any, int]:
    import heapq
    dist: Dict[Any, int] = {start: 0}
    pq: List[Tuple[int, Any]] = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def johnson_apsp(graph: Graph) -> Dict[Any, Dict[Any, int]]:
    vertices = list(graph.keys())
    for v in vertices:
        for u, _ in graph.get(v, []):
            if u not in vertices:
                vertices.append(u)
    edges: List[Tuple[Any, Any, int]] = []
    for u in vertices:
        for v, w in graph.get(u, []):
            edges.append((u, v, w))
    super_source = object()
    vertices2 = vertices + [super_source]
    edges2 = edges + [(super_source, v, 0) for v in vertices]
    dist, has_cycle = _bellman_ford(vertices2, edges2, super_source)
    if has_cycle or dist is None:
        raise ValueError("Negative cycle detected")
    h = dist
    reweighted: Graph = {}
    for u in vertices:
        reweighted[u] = []
        for v, w in graph.get(u, []):
            rw = w + h[u] - h[v]
            reweighted[u].append((v, rw))
    result: Dict[Any, Dict[Any, int]] = {}
    for s in vertices:
        d = _dijkstra(reweighted, s)
        result[s] = {}
        for t, val in d.items():
            result[s][t] = val - h[s] + h[t]
    return result

if __name__ == "__main__":
    g: Graph = {
        'A': [('B', 1), ('C', 2)],
        'B': [('C', -2)],
        'C': [('D', 2)],
        'D': []
    }
    apsp = johnson_apsp(g)
    assert apsp['A']['B'] == 1
    assert apsp['A']['C'] == -1
    assert apsp['A']['D'] == 1
    print("All Johnson APSP tests passed!")
