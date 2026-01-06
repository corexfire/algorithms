"""
Description:
    [EN] A* search finds a lowest-cost path from start to goal using best-first expansion guided by a heuristic. It is complete and optimal when the heuristic is admissible and consistent.
    [ID] Pencarian A* menemukan jalur berbiaya terendah dari awal ke tujuan menggunakan ekspansi terbaik-pertama yang dipandu heuristik. A* lengkap dan optimal jika heuristiknya admissible dan konsisten.

Implementation Details:
    [EN]
    - Node cost f = g + h where g is path cost so far and h is heuristic to goal.
    - Uses a min-priority queue (open list) and a closed set to avoid re-expansion.
    - This implementation allows 8-direction moves and uses squared Euclidean distance for h.
    [ID]
    - Biaya node f = g + h, dengan g biaya jalur sejauh ini dan h heuristik ke tujuan.
    - Menggunakan antrian prioritas minimum (open list) dan himpunan tertutup untuk menghindari re-ekspansi.
    - Implementasi ini mengizinkan gerakan 8-arah dan memakai jarak Euclidean kuadrat untuk h.

Usage Documentation:
    [EN]
    - Input: 2D grid maze with 0 for free cell and 1 for wall, start and end coordinates.
    - Call `a_star_search(maze, start, end)` to get a list of positions or None if unreachable.
    [ID]
    - Input: grid 2D maze dengan 0 untuk sel bebas dan 1 untuk tembok, koordinat awal dan akhir.
    - Panggil `a_star_search(maze, start, end)` untuk memperoleh daftar posisi atau None bila tak terjangkau.

Examples:
    >>> maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    >>> start, end = (0, 0), (2, 2)
    >>> a_star_search(maze, start, end)
    [(0, 0), (0, 1), (1, 2), (2, 2)]
"""
from typing import List, Tuple, Dict, Set, Optional
import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to end
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def a_star_search(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze.
    0 represents a walkable path, 1 represents a wall.
    
    Args:
        maze: 2D grid representing the map
        start: (row, col) tuple
        end: (row, col) tuple
        
    Returns:
        List of (row, col) tuples representing the path, or None if no path found
    """
    
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = set()

    # Add the start node
    heapq.heappush(open_list, start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            # Heuristic: Euclidean distance
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            is_in_open = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    is_in_open = True
                    break
            
            if is_in_open:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)
            
    return None

if __name__ == "__main__":
    # Test cases
    maze = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end = (7, 6)

    path = a_star_search(maze, start, end)
    print(f"Path found: {path}")
    
    assert path is not None
    assert path[0] == start
    assert path[-1] == end
    
    # Verify path validity (simplified)
    for pos in path:
        r, c = pos
        assert maze[r][c] == 0
        
    print("All test cases passed!")
