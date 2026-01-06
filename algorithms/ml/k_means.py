"""
K-Means Clustering
------------------

1. English Description
----------------------
K-Means clustering aims to partition `n` observations into `k` clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or centroids).
It is a popular method for cluster analysis in data mining.
This implementation uses Lloyd's algorithm (iterative refinement).

Time Complexity: O(n * k * d * i) where n=points, k=clusters, d=dimensions, i=iterations.
Space Complexity: O(n + k)

2. Indonesian Description
-------------------------
K-Means clustering bertujuan untuk mempartisi `n` observasi menjadi `k` kluster di mana setiap observasi termasuk dalam kluster dengan rata-rata terdekat (pusat kluster atau centroid).
Ini adalah metode populer untuk analisis kluster dalam data mining.
Implementasi ini menggunakan algoritma Lloyd (perbaikan berulang).

Kompleksitas Waktu: O(n * k * d * i) di mana n=titik, k=kluster, d=dimensi, i=iterasi.
Kompleksitas Ruang: O(n + k)

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Initialization / Inisialisasi**:
  - [EN] Randomly selects `k` points as initial centroids.
  - [ID] Secara acak memilih `k` titik sebagai centroid awal.
- **Assignment Step / Langkah Penugasan**:
  - [EN] Assigns each point to the nearest centroid based on Euclidean distance.
  - [ID] Menetapkan setiap titik ke centroid terdekat berdasarkan jarak Euclidean.
- **Update Step / Langkah Pembaruan**:
  - [EN] Recalculates centroids as the mean of all points assigned to the cluster.
  - [ID] Menghitung ulang centroid sebagai rata-rata dari semua titik yang ditugaskan ke kluster.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Arguments / Argumen**:
  - [EN] `points`: List of (x, y) tuples. `k`: Number of clusters. `max_iter`: Max iterations.
  - [ID] `points`: Daftar tuple (x, y). `k`: Jumlah kluster. `max_iter`: Maks iterasi.
- **Returns / Mengembalikan**:
  - [EN] `(centers, labels)`: Final centroids and list of cluster index for each point.
  - [ID] `(centers, labels)`: Centroid akhir dan daftar indeks kluster untuk setiap titik.
"""

from typing import List, Tuple
import random
import math

Point = Tuple[float, float]

def _distance(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def _mean(points: List[Point]) -> Point:
    if not points:
        return (0.0, 0.0)
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    n = len(points)
    return (sx / n, sy / n)

def k_means(points: List[Point], k: int, max_iter: int = 100, seed: int = 42) -> Tuple[List[Point], List[int]]:
    if k <= 0 or not points:
        return [], []
    random.seed(seed)
    centers = random.sample(points, min(k, len(points)))
    labels = [0] * len(points)
    for _ in range(max_iter):
        changed = False
        for i, p in enumerate(points):
            dists = [_distance(p, c) for c in centers]
            new_label = dists.index(min(dists))
            if labels[i] != new_label:
                labels[i] = new_label
                changed = True
        clusters = [[] for _ in range(len(centers))]
        for p, lbl in zip(points, labels):
            clusters[lbl].append(p)
        new_centers = [(_mean(cluster) if cluster else centers[i]) for i, cluster in enumerate(clusters)]
        if all(_distance(c, nc) < 1e-9 for c, nc in zip(centers, new_centers)):
            break
        centers = new_centers
        if not changed:
            break
    return centers, labels

if __name__ == "__main__":
    pts = [(1, 1), (1.5, 2), (3, 4), (5, 7), (3.5, 5), (4.5, 5), (3.5, 4.5)]
    centers, labels = k_means(pts, k=2, seed=0)
    print(f"Centers: {centers}")
    print(f"Labels: {labels}")
    assert len(centers) == 2
    assert len(labels) == len(pts)
    print("All K-Means tests passed!")
