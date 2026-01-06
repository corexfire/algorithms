"""
Line Segment Intersection
-------------------------

1. English Description
----------------------
Determines if two line segments intersect and calculates the intersection point.
It handles general cases as well as collinear cases for segment intersection.
Useful in computational geometry, collision detection, and computer graphics.

Time Complexity: O(1)
Space Complexity: O(1)

2. Indonesian Description
-------------------------
Menentukan apakah dua segmen garis berpotongan dan menghitung titik potongnya.
Ini menangani kasus umum serta kasus kolinear untuk persimpangan segmen.
Berguna dalam geometri komputasi, deteksi tabrakan, dan grafika komputer.

Kompleksitas Waktu: O(1)
Kompleksitas Ruang: O(1)

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Orientation / Orientasi**:
  - [EN] Uses cross product to determine if points are clockwise, counter-clockwise, or collinear.
  - [ID] Menggunakan cross product untuk menentukan apakah titik searah jarum jam, berlawanan arah jarum jam, atau kolinear.
- **Intersection Check / Cek Persimpangan**:
  - [EN] Checks if endpoints of one segment lie on opposite sides of the other segment.
  - [ID] Memeriksa apakah titik akhir satu segmen terletak di sisi yang berlawanan dari segmen lainnya.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Functions / Fungsi**:
  - [EN] `segments_intersect(p1, p2, q1, q2)`: Returns `True` if segment `p1-p2` intersects `q1-q2`.
  - [ID] `segments_intersect(p1, p2, q1, q2)`: Mengembalikan `True` jika segmen `p1-p2` memotong `q1-q2`.
  - [EN] `intersection_point(p1, p2, q1, q2)`: Returns the `(x, y)` point where lines intersect (or None if parallel).
  - [ID] `intersection_point(p1, p2, q1, q2)`: Mengembalikan titik `(x, y)` di mana garis berpotongan (atau None jika sejajar).
"""

from typing import Tuple, Optional

Point = Tuple[float, float]

def _orientation(a: Point, b: Point, c: Point) -> float:
    return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])

def _on_segment(a: Point, b: Point, c: Point) -> bool:
    return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])

def segments_intersect(p1: Point, p2: Point, q1: Point, q2: Point) -> bool:
    o1 = _orientation(p1, p2, q1)
    o2 = _orientation(p1, p2, q2)
    o3 = _orientation(q1, q2, p1)
    o4 = _orientation(q1, q2, p2)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    if o1 == 0 and _on_segment(p1, p2, q1):
        return True
    if o2 == 0 and _on_segment(p1, p2, q2):
        return True
    if o3 == 0 and _on_segment(q1, q2, p1):
        return True
    if o4 == 0 and _on_segment(q1, q2, p2):
        return True
    return False

def intersection_point(p1: Point, p2: Point, q1: Point, q2: Point) -> Optional[Point]:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (px, py)

if __name__ == "__main__":
    assert segments_intersect((0, 0), (4, 4), (0, 4), (4, 0)) is True
    ip = intersection_point((0, 0), (4, 4), (0, 4), (4, 0))
    print(f"Intersection: {ip}")
    assert ip == (2.0, 2.0)
    assert segments_intersect((0, 0), (1, 0), (0, 1), (1, 1)) is False
    assert segments_intersect((0, 0), (2, 2), (1, 1), (3, 3)) is True
    assert intersection_point((0, 0), (2, 2), (1, 1), (3, 3)) is None
    print("All Line Intersection tests passed!")
