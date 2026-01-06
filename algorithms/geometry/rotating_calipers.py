"""
Rotating Calipers
=================

1. English Description
----------------------
The Rotating Calipers algorithm is an efficient method for solving a variety of geometric problems involving convex polygons. Its most common application is computing the **diameter** of a convex polygon (the maximum distance between any two points).

- **Logic**: The algorithm simulates rotating a pair of parallel supporting lines (calipers) around the convex polygon. As the lines rotate, they touch the polygon at antipodal pairs of vertices/edges. The maximum distance is always found between such antipodal pairs.
- **Prerequisite**: The input points must first be processed into a Convex Hull (e.g., using Graham Scan or Monotone Chain).
- **Time Complexity**: O(n) for the caliper rotation itself. The total complexity is dominated by the Convex Hull step, which is O(n log n).
- **Space Complexity**: O(n) to store the hull vertices.

2. Indonesian Description (Deskripsi Bahasa Indonesia)
------------------------------------------------------
Algoritma Rotating Calipers (Kaliper Berputar) adalah metode efisien untuk menyelesaikan berbagai masalah geometri yang melibatkan poligon cembung. Aplikasi yang paling umum adalah menghitung **diameter** poligon cembung (jarak maksimum antara dua titik mana pun).

- **Logika**: Algoritma ini mensimulasikan pemutaran sepasang garis pendukung paralel (kaliper) di sekeliling poligon cembung. Saat garis berputar, mereka menyentuh poligon pada pasangan titik sudut/sisi yang antipodal (berlawanan). Jarak maksimum selalu ditemukan di antara pasangan antipodal tersebut.
- **Prasyarat**: Titik-titik input harus diproses terlebih dahulu menjadi Convex Hull (misalnya, menggunakan Graham Scan atau Monotone Chain).
- **Kompleksitas Waktu**: O(n) untuk putaran kaliper itu sendiri. Total kompleksitas didominasi oleh langkah Convex Hull, yaitu O(n log n).
- **Kompleksitas Ruang**: O(n) untuk menyimpan titik-titik hull.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Use Cases / Kasus Penggunaan**: 
  - [EN] Collision detection in game physics (finding the width of objects).
  - [ID] Deteksi tabrakan dalam fisika game (mencari lebar objek).
  - [EN] Computing the minimum enclosing rectangle (bounding box) of an object.
  - [ID] Menghitung persegi panjang pembatas minimum (bounding box) dari sebuah objek.
  - [EN] Image processing and computer vision (shape analysis).
  - [ID] Pemrosesan citra dan visi komputer (analisis bentuk).
- **Key Function / Fungsi Utama**: 
  - [EN] `polygon_diameter(points)` computes the max distance.
  - [ID] `polygon_diameter(points)` menghitung jarak maksimum.
- **Input Format / Format Input**: 
  - [EN] List of `(x, y)` tuples representing points.
  - [ID] Daftar tuple `(x, y)` yang merepresentasikan titik-titik.
- **Output / Output**: 
  - [EN] Float value representing the diameter.
  - [ID] Nilai float yang merepresentasikan diameter.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Dependencies / Ketergantungan**: 
  - [EN] Requires `algorithms.geometry.convex_hull` for the preprocessing step.
  - [ID] Membutuhkan `algorithms.geometry.convex_hull` untuk langkah pra-pemrosesan.
- **How to Run / Cara Menjalankan**: 
  - [EN] Import `polygon_diameter` and pass a list of 2D points.
  - [ID] Impor `polygon_diameter` dan berikan daftar titik 2D.
- **Testing / Pengujian**: 
  - [EN] Includes test cases for Square, Rectangle, Triangle, and arbitrary points.
  - [ID] Mencakup kasus uji untuk Persegi, Persegi Panjang, Segitiga, dan titik acak.
"""

import math
import sys
import os

# Ensure we can import from algorithms package
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from algorithms.geometry.convex_hull import convex_hull, distance_sq, cross_product

def polygon_diameter(points: list) -> float:
    """
    Computes the diameter of a set of 2D points (max distance between any pair).
    
    Args:
        points: List of (x, y) tuples.
        
    Returns:
        Maximum distance between any two points in the set.
    """
    if len(points) < 2:
        return 0.0
    if len(points) == 2:
        return math.sqrt(distance_sq(points[0], points[1]))
        
    # Step 1: Compute Convex Hull
    # The diameter of a set of points is the same as the diameter of its convex hull.
    hull = convex_hull(points)
    
    # convex_hull returns a closed loop implicitly or explicitly?
    # Based on convex_hull.py, it returns list of vertices. 
    # Usually Graham scan returns unique vertices.
    # Rotating calipers needs to iterate edges, so we treat it as cyclic.
    
    n = len(hull)
    if n <= 1: 
        return 0.0
    if n == 2:
        return math.sqrt(distance_sq(hull[0], hull[1]))
        
    # Step 2: Rotating Calipers
    # We want to find max distance between antipodal pairs.
    # We iterate through edges of the hull. For each edge, we find the point farthest from it.
    
    # Since cross_product corresponds to 2 * Area of triangle,
    # maximizing area is equivalent to maximizing height (distance to line).
    
    j = 1
    max_d2 = 0
    
    for i in range(n):
        p1 = hull[i]
        p2 = hull[(i + 1) % n]
        
        # Advance j while area of triangle (p1, p2, hull[j+1]) > area (p1, p2, hull[j])
        # Area is proportional to Cross Product of (p2-p1) and (hull[j]-p1)
        # But we need consistent orientation. Hull is CCW.
        
        while True:
            curr_p = hull[j % n]
            next_p = hull[(j + 1) % n]
            
            # Cross product (p1, p2, curr_p)
            area_curr = abs(cross_product(p1, p2, curr_p))
            # Cross product (p1, p2, next_p)
            area_next = abs(cross_product(p1, p2, next_p))
            
            if area_next > area_curr:
                j += 1
            else:
                break
                
        # Update max distance with distance between p1 and antipodal point,
        # and p2 and antipodal point.
        # Actually, the diameter pair must be one of the (vertex, vertex) pairs encountered.
        # The antipodal point to the edge p1-p2 is hull[j].
        # Candidates for diameter are (p1, hull[j]) and (p2, hull[j]).
        
        curr_idx = j % n
        d2_1 = distance_sq(p1, hull[curr_idx])
        d2_2 = distance_sq(p2, hull[curr_idx])
        
        max_d2 = max(max_d2, d2_1, d2_2)
        
    return math.sqrt(max_d2)

if __name__ == "__main__":
    print("Rotating Calipers (Diameter) Tests...")
    
    # Test Case 1: Square
    points1 = [(0, 0), (0, 1), (1, 1), (1, 0)]
    # Diagonal is sqrt(2) approx 1.414
    d1 = polygon_diameter(points1)
    print(f"Square (side 1): {d1}")
    assert abs(d1 - math.sqrt(2)) < 1e-9
    
    # Test Case 2: Rectangle 2x1
    points2 = [(0, 0), (2, 0), (2, 1), (0, 1)]
    # Diagonal is sqrt(2^2 + 1^2) = sqrt(5) approx 2.236
    d2 = polygon_diameter(points2)
    print(f"Rectangle (2x1): {d2}")
    assert abs(d2 - math.sqrt(5)) < 1e-9
    
    # Test Case 3: Triangle
    points3 = [(0, 0), (3, 0), (0, 4)]
    # Sides: 3, 4, 5. Max dist is 5.
    d3 = polygon_diameter(points3)
    print(f"Triangle (3-4-5): {d3}")
    assert abs(d3 - 5.0) < 1e-9
    
    # Test Case 4: Arbitrary points including interior
    points4 = [(0, 0), (10, 0), (5, 5), (2, 1), (8, 1)]
    # Diameter is distance between (0,0) and (10,0) = 10, or (0,0)-(5,5)=sqrt(50)~7.07, or (10,0)-(5,5)=7.07
    # Max is 10.
    d4 = polygon_diameter(points4)
    print(f"Arbitrary points: {d4}")
    assert abs(d4 - 10.0) < 1e-9
    
    print("All Rotating Calipers tests passed!")
