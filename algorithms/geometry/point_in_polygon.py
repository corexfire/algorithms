"""
Description:
    [EN] The Point in Polygon algorithm determines whether a given point lies inside, outside, or on the boundary of a polygon. This implementation uses the Ray Casting algorithm (also known as the Even-Odd Rule), which works for both convex and concave polygons.
    [ID] Algoritma Titik dalam Poligon menentukan apakah titik tertentu terletak di dalam, di luar, atau pada batas poligon. Implementasi ini menggunakan algoritma Ray Casting (juga dikenal sebagai Aturan Genap-Ganjil), yang bekerja untuk poligon cembung maupun cekung.

Implementation Details:
    [EN]
    - The algorithm casts a ray from the point in a fixed direction (usually horizontal) and counts the number of intersections with the polygon's edges.
    - If the number of intersections is odd, the point is inside; if even, it is outside.
    - Handles edge cases where the ray passes through vertices.
    [ID]
    - Algoritma memancarkan sinar dari titik ke arah tetap (biasanya horizontal) dan menghitung jumlah perpotongan dengan sisi-sisi poligon.
    - Jika jumlah perpotongan ganjil, titik berada di dalam; jika genap, berada di luar.
    - Menangani kasus tepi di mana sinar melewati titik sudut.

Usage Documentation:
    [EN]
    - The `point_in_polygon` function takes a point (x, y) and a list of points representing the polygon vertices.
    - Returns `True` if the point is inside or on the boundary, and `False` otherwise.
    [ID]
    - Fungsi `point_in_polygon` menerima sebuah titik (x, y) dan daftar titik yang mewakili simpul-simpul poligon.
    - Mengembalikan `True` jika titik berada di dalam atau pada batas, dan `False` sebaliknya.

Examples:
    >>> square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    >>> point_in_polygon((2, 2), square)
    True
    >>> point_in_polygon((5, 5), square)
    False
"""

from typing import List, Tuple

Point = Tuple[float, float]

def point_in_polygon(point: Point, polygon: List[Point]) -> bool:
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        cond = (y1 > y) != (y2 > y)
        if cond:
            xinters = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if xinters == x:
                return True
            if xinters > x:
                inside = not inside
    return inside

if __name__ == "__main__":
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    assert point_in_polygon((2, 2), square) is True
    assert point_in_polygon((5, 5), square) is False
    assert point_in_polygon((4, 2), square) is True
    triangle = [(0, 0), (5, 0), (2.5, 5)]
    assert point_in_polygon((2.5, 2), triangle) is True
    assert point_in_polygon((5, 5), triangle) is False
    print("All Point in Polygon tests passed!")
