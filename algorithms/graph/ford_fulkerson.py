"""
Description:
    [EN] Ford–Fulkerson computes the maximum flow in a directed capacitated network by repeatedly finding augmenting paths in the residual graph and augmenting flow along them.
    [ID] Ford–Fulkerson menghitung aliran maksimum pada jaringan berkapasitas terarah dengan berulang kali menemukan jalur augmentasi pada graf residual dan menambah aliran di sepanjang jalur tersebut.

Implementation Details:
    [EN]
    - Uses DFS to find any augmenting path; for better complexity, use BFS (Edmonds–Karp).
    - Updates residual capacities on forward and reverse edges after augmentation.
    - Complexity depends on path selection: O(max_flow · E) here; Edmonds–Karp is O(V E^2).
    [ID]
    - Menggunakan DFS untuk menemukan jalur augmentasi apa pun; untuk kompleksitas lebih baik gunakan BFS (Edmonds–Karp).
    - Memperbarui kapasitas residual pada sisi maju dan balik setelah augmentasi.
    - Kompleksitas bergantung pemilihan jalur: O(max_flow · E) di sini; Edmonds–Karp O(V E^2).

Usage Documentation:
    [EN]
    - Create `FordFulkerson(n)` and add directed edges with capacities via `add_edge(u, v, capacity)`.
    - Call `max_flow(source, sink)` to get the maximum flow value.
    [ID]
    - Buat `FordFulkerson(n)` dan tambahkan sisi berarah dengan kapasitas melalui `add_edge(u, v, capacity)`.
    - Panggil `max_flow(source, sink)` untuk mendapatkan nilai aliran maksimum.

Examples:
    >>> g = FordFulkerson(6)
    >>> g.add_edge(0,1,16); g.add_edge(0,2,13); g.add_edge(1,2,10); g.add_edge(1,3,12)
    >>> g.add_edge(2,1,4); g.add_edge(2,4,14); g.add_edge(3,2,9); g.add_edge(3,5,20)
    >>> g.add_edge(4,3,7); g.add_edge(4,5,4)
    >>> g.max_flow(0, 5)
    23
"""

from typing import List, Dict

class FordFulkerson:
    def __init__(self, vertices: int):
        """
        Initialize graph with number of vertices.
        Vertices are 0-indexed.
        """
        self.V = vertices
        # graph[u][v] stores capacity of edge u->v
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u: int, v: int, capacity: int):
        """Adds a directed edge with capacity."""
        self.graph[u][v] = capacity

    def _dfs(self, u: int, t: int, visited: List[bool], flow: int, parent: List[int]) -> int:
        """
        DFS to find augmenting path from u to t.
        Returns the bottleneck capacity of the path found.
        """
        if u == t:
            return flow
        
        visited[u] = True
        
        for v in range(self.V):
            # If there is available capacity and v is not visited
            if not visited[v] and self.graph[u][v] > 0:
                parent[v] = u
                new_flow = min(flow, self.graph[u][v])
                bottleneck = self._dfs(v, t, visited, new_flow, parent)
                
                if bottleneck > 0:
                    return bottleneck
        
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        """
        Returns the maximum flow from source to sink.
        """
        # Create a residual graph (using the same structure as self.graph)
        # Since we modify self.graph directly in this simple implementation,
        # we might want to copy it if we need to preserve original graph.
        # But here we modify in place for simplicity of residual handling.
        # Note: If you need to reuse the graph, deep copy it first.
        
        # We'll use a copy for the residual graph to keep the original intact if needed later
        # But for standard Ford-Fulkerson, we work on residual capacities.
        # Let's assume self.graph IS the residual graph.
        
        # To make it reusable, let's copy capacities to a temp graph
        residual_graph = [row[:] for row in self.graph]
        
        parent = [-1] * self.V
        max_flow = 0
        
        while True:
            visited = [False] * self.V
            # Find an augmenting path using DFS
            # Ideally use BFS for Edmonds-Karp which is O(VE^2)
            # Here we implement basic Ford-Fulkerson with DFS
            
            # For pure Ford-Fulkerson with DFS:
            # We need to find *any* path with available capacity
            path_flow = self._dfs_find_path(residual_graph, source, sink, visited, float('inf'), parent)
            
            if path_flow == 0:
                break
                
            max_flow += path_flow
            
            # update residual capacities of the edges and reverse edges
            curr = sink
            while curr != source:
                prev = parent[curr]
                residual_graph[prev][curr] -= path_flow
                residual_graph[curr][prev] += path_flow
                curr = prev
                
        return max_flow

    def _dfs_find_path(self, r_graph, u, t, visited, flow, parent):
        if u == t:
            return flow
        visited[u] = True
        
        for v in range(self.V):
            if not visited[v] and r_graph[u][v] > 0:
                parent[v] = u
                new_flow = min(flow, r_graph[u][v])
                result = self._dfs_find_path(r_graph, v, t, visited, new_flow, parent)
                if result > 0:
                    return result
        return 0

if __name__ == "__main__":
    print("Ford-Fulkerson Max Flow Tests...")
    
    # Graph example:
    # 0 -> 1 (16)
    # 0 -> 2 (13)
    # 1 -> 2 (10)
    # 1 -> 3 (12)
    # 2 -> 1 (4)
    # 2 -> 4 (14)
    # 3 -> 2 (9)
    # 3 -> 5 (20)
    # 4 -> 3 (7)
    # 4 -> 5 (4)
    
    g = FordFulkerson(6)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)
    
    source = 0
    sink = 5
    
    print(f"Calculating Max Flow from {source} to {sink}...")
    max_flow_val = g.max_flow(source, sink)
    print(f"Max Flow: {max_flow_val}, Expected: 23")
    
    assert max_flow_val == 23
    
    # Simple case
    # 0 -> 1 (10)
    # 0 -> 2 (10)
    # 1 -> 3 (5)
    # 2 -> 3 (15)
    # 3 -> 4 (20)
    # Max flow should be 20 (limited by 0->1(10) + 0->2(10) = 20 coming out of 0)
    # Path 0->1->3->4 (5)
    # Path 0->2->3->4 (10) - bottleneck 2->3 capacity 15, wait.
    
    g2 = FordFulkerson(5)
    g2.add_edge(0, 1, 10)
    g2.add_edge(0, 2, 10)
    g2.add_edge(1, 3, 5)
    g2.add_edge(2, 3, 15)
    g2.add_edge(3, 4, 20)
    
    # 0->1->3->4: min(10, 5, 20) = 5
    # 0->2->3->4: min(10, 15, 20) = 10
    # Total = 15?
    # Wait, 1->3 is 5. 2->3 is 15.
    # Flow into 3 is 5 + 10 = 15.
    # Flow out of 3 is 20.
    # So max flow is 15.
    
    print(f"Calculating Max Flow for simple graph...")
    mf2 = g2.max_flow(0, 4)
    print(f"Max Flow: {mf2}, Expected: 15")
    assert mf2 == 15
    
    print("All Ford-Fulkerson tests passed!")
