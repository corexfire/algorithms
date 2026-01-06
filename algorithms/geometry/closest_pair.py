"""
Description:
    [EN] The Closest Pair of Points problem asks to find the pair of points with the smallest Euclidean distance among a set of points in a 2D plane. This implementation uses the divide and conquer approach to achieve O(n log n) time complexity, which is significantly faster than the O(n^2) brute force method.
    [ID] Masalah Pasangan Titik Terdekat meminta untuk menemukan pasangan titik dengan jarak Euclidean terkecil di antara sekumpulan titik dalam bidang 2D. Implementasi ini menggunakan pendekatan divide and conquer untuk mencapai kompleksitas waktu O(n log n), yang secara signifikan lebih cepat daripada metode brute force O(n^2).

Implementation Details:
    [EN]
    - The algorithm recursively divides the points into two halves.
    - It finds the closest pair in the left and right halves.
    - It then checks for a closer pair that spans across the dividing line (in the "strip").
    - Points are pre-sorted by x-coordinate and y-coordinate to optimize the recursion steps.
    [ID]
    - Algoritma secara rekursif membagi titik-titik menjadi dua bagian.
    - Ia menemukan pasangan terdekat di bagian kiri dan kanan.
    - Kemudian ia memeriksa pasangan yang lebih dekat yang merentang melintasi garis pemisah (dalam "strip").
    - Titik-titik diurutkan sebelumnya berdasarkan koordinat x dan koordinat y untuk mengoptimalkan langkah-langkah rekursi.

Usage Documentation:
    [EN]
    - The `closest_pair` function takes a list of tuples representing (x, y) coordinates.
    - Returns a tuple containing the minimum distance and the pair of points forming that distance.
    [ID]
    - Fungsi `closest_pair` menerima daftar tuple yang mewakili koordinat (x, y).
    - Mengembalikan tuple yang berisi jarak minimum dan pasangan titik yang membentuk jarak tersebut.

Examples:
    >>> points = [(0, 0), (3, 4), (1, 1), (7, 7)]
    >>> dist, pair = closest_pair(points)
    >>> print(f"{dist:.4f}")
    1.4142
"""

from typing import List, Tuple
import math

Point = Tuple[float, float]

def _dist(p1: Point, p2: Point) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def _closest_in_strip(strip: List[Point], d: float) -> Tuple[float, Tuple[Point, Point]]:
    strip.sort(key=lambda p: p[1])
    best = d
    best_pair: Tuple[Point, Point] = (strip[0], strip[0])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < best:
            dij = _dist(strip[i], strip[j])
            if dij < best:
                best = dij
                best_pair = (strip[i], strip[j])
            j += 1
    return best, best_pair

def _closest_rec(px: List[Point], py: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    n = len(px)
    if n <= 3:
        best = float("inf")
        best_pair = (px[0], px[0])
        for i in range(n):
            for j in range(i + 1, n):
                dij = _dist(px[i], px[j])
                if dij < best:
                    best = dij
                    best_pair = (px[i], px[j])
        return best, best_pair
    mid = n // 2
    mid_point = px[mid]
    Qx = px[:mid]
    Rx = px[mid:]
    Qy = [p for p in py if p[0] <= mid_point[0]]
    Ry = [p for p in py if p[0] > mid_point[0]]
    dl, pair_l = _closest_rec(Qx, Qy)
    dr, pair_r = _closest_rec(Rx, Ry)
    d = dl if dl < dr else dr
    best_pair = pair_l if dl < dr else pair_r
    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
    ds, pair_s = _closest_in_strip(strip, d) if strip else (d, best_pair)
    if ds < d:
        return ds, pair_s
    return d, best_pair

def closest_pair(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    if len(points) < 2:
        return float("inf"), ((0.0, 0.0), (0.0, 0.0))
    px = sorted(points, key=lambda p: (p[0], p[1]))
    py = sorted(points, key=lambda p: (p[1], p[0]))
    return _closest_rec(px, py)

if __name__ == "__main__":
    tests = [
        ([(0, 0), (3, 4), (7, 7), (1, 1)], math.sqrt(2)),
        ([(0, 0), (10, 10)], math.sqrt(200)),
        ([(2, 2), (2.5, 2.5), (9, 9), (9.1, 9.2)], math.sqrt(0.05)),
        ([(1, 1)], float("inf")),
    ]
    for pts, expected_dist in tests:
        d, pair = closest_pair(pts)
        print(f"Points: {pts}")
        print(f"Distance: {d}, Pair: {pair}")
        if expected_dist != float("inf"):
            assert abs(d - expected_dist) < 1e-9
        else:
            assert d == float("inf")
    print("All Closest Pair tests passed!")
