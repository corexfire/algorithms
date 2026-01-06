"""
Graham Scan (Convex Hull)
-------------------------

1. English Description
----------------------
Finds the Convex Hull of a set of points in 2D space.
The Convex Hull is the smallest convex polygon containing all points.
This implementation uses the Graham Scan algorithm, which sorts points by polar angle and then builds the hull.

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(n) to store the hull.

2. Indonesian Description
-------------------------
Mencari Convex Hull (Selubung Cembung) dari sekumpulan titik dalam ruang 2D.
Convex Hull adalah poligon cembung terkecil yang memuat semua titik.
Implementasi ini menggunakan algoritma Graham Scan, yang mengurutkan titik berdasarkan sudut polar dan kemudian membangun hull.

Kompleksitas Waktu: O(n log n) karena pengurutan.
Kompleksitas Ruang: O(n) untuk menyimpan hull.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Core Concept / Konsep Utama**:
  - [EN] Sort points by angle relative to the bottom-leftmost point ("anchor").
  - [ID] Urutkan titik berdasarkan sudut relatif terhadap titik paling bawah-kiri ("anchor").
- **Stack Operation / Operasi Stack**:
  - [EN] Iterate through sorted points, push to stack, pop if a non-left (clockwise) turn is made.
  - [ID] Iterasi titik yang diurutkan, push ke stack, pop jika terjadi belokan non-kiri (searah jarum jam).
- **Geometric Primitives / Primitif Geometris**:
  - [EN] Uses cross product to determine turn direction (CCW, CW, or collinear).
  - [ID] Menggunakan cross product untuk menentukan arah belokan (CCW, CW, atau kolinear).

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Input Format / Format Input**:
  - [EN] `points`: A list of tuples `(x, y)`.
  - [ID] `points`: Sebuah list berisi tuple `(x, y)`.
- **Function Call / Pemanggilan Fungsi**:
  - [EN] `convex_hull(points)` returns the list of hull vertices in CCW order.
  - [ID] `convex_hull(points)` mengembalikan daftar titik hull dalam urutan CCW.
"""

import math
from typing import List, Tuple

Point = Tuple[int, int]

def polar_angle(p0: Point, p1: Point) -> float:
    """Returns the polar angle of p1 with respect to p0."""
    y_span = p1[1] - p0[1]
    x_span = p1[0] - p0[0]
    return math.atan2(y_span, x_span)

def distance_sq(p0: Point, p1: Point) -> int:
    """Returns the squared distance between p0 and p1."""
    return (p1[0] - p0[0])**2 + (p1[1] - p0[1])**2

def cross_product(o: Point, a: Point, b: Point) -> int:
    """
    Returns the cross product of vectors OA and OB.
    A positive cross product indicates a counter-clockwise turn,
    negative indicates a clockwise turn, and zero indicates collinear points.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points: List[Point]) -> List[Point]:
    """
    Computes the convex hull of a set of 2D points using Graham Scan.
    
    Args:
        points: List of (x, y) tuples
        
    Returns:
        List of points on the convex hull in counter-clockwise order
    """
    n = len(points)
    if n <= 2:
        return points

    # Step 1: Find the bottom-most point (and left-most if ties)
    start = min(points, key=lambda p: (p[1], p[0]))
    
    # Step 2: Sort the remaining points based on the polar angle they make with 'start'
    # If two points have same angle, the one closer to start comes first? 
    # Actually, we usually want the farthest one to keep the hull correct if collinear.
    # But for standard Graham scan, we process them in order.
    # To handle collinear points correctly, we might need to remove closer points 
    # or handle them carefully.
    
    # Sort key: (angle, distance)
    # math.atan2 returns value in (-pi, pi]
    sorted_points = sorted(points, key=lambda p: (polar_angle(start, p), distance_sq(start, p)))
    
    # Remove duplicates of start point if any (though logic above handles it, start will be first)
    # Actually, start point will have angle -pi or similar? No, atan2(0,0) is 0.
    # Let's ensure start is not duplicated in the sorted list if we pop it.
    
    # Alternative sorting approach:
    # Remove start from list, sort others, then prepend start
    other_points = [p for p in points if p != start]
    other_points.sort(key=lambda p: (polar_angle(start, p), distance_sq(start, p)))
    
    # If multiple points have same angle, we only keep the farthest one?
    # Standard implementation often keeps all, but logic in loop handles turns.
    # However, if we have collinear points at the end, it can be tricky.
    
    hull = [start]
    
    for p in other_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            # Pop if we make a clockwise or collinear turn (keeping only extreme points)
            # If we want to include collinear points on the edge, condition changes.
            # Usually strict convex hull excludes collinear points on edges (except endpoints).
            hull.pop()
        hull.append(p)
        
    return hull

if __name__ == "__main__":
    print("Graham Scan Convex Hull Tests...")
    
    # Square
    points1 = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
    # Expected: (0,0), (2,0), (2,2), (0,2) in CCW order (start is (0,0))
    hull1 = convex_hull(points1)
    print(f"Square points: {points1}")
    print(f"Hull: {hull1}")
    
    assert (0, 0) in hull1
    assert (2, 2) in hull1
    assert (1, 1) not in hull1 # Interior point
    
    # Triangle with points on edges
    points2 = [(0, 0), (4, 0), (2, 4), (2, 0), (1, 2), (3, 2)]
    # (2,0) is on bottom edge. (1,2) on left edge. (3,2) on right edge.
    # Depending on implementation, collinear points might be removed.
    # Our implementation removes them (<= 0 condition).
    hull2 = convex_hull(points2)
    print(f"Triangle points: {points2}")
    print(f"Hull: {hull2}")
    
    assert len(hull2) == 3
    assert (0, 0) in hull2
    assert (4, 0) in hull2
    assert (2, 4) in hull2
    
    # Collinear points
    points3 = [(0, 0), (1, 1), (2, 2), (3, 3)]
    hull3 = convex_hull(points3)
    print(f"Collinear points: {points3}")
    print(f"Hull: {hull3}")
    # Should be start and end
    assert (0, 0) in hull3
    assert (3, 3) in hull3
    
    print("All Graham Scan tests passed!")
