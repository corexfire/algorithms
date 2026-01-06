"""
Segment Tree
------------

1. English Description
----------------------
A Segment Tree is a versatile data structure used for storing information about intervals or segments.
It allows querying which of the stored segments contain a given point, but strictly speaking, it is used for range queries and point updates.
Common queries include range sum, range minimum/maximum, etc.

Time Complexity: O(n) for build, O(log n) for query and update.
Space Complexity: O(4n) ~ O(n) for the tree array.

2. Indonesian Description
-------------------------
Segment Tree adalah struktur data serbaguna yang digunakan untuk menyimpan informasi tentang interval atau segmen.
Ini memungkinkan kueri segmen mana yang disimpan yang berisi titik tertentu, tetapi secara tegas, ini digunakan untuk kueri rentang dan pembaruan titik.
Kueri umum termasuk jumlah rentang (range sum), minimum/maksimum rentang, dll.

Kompleksitas Waktu: O(n) untuk build, O(log n) untuk query dan update.
Kompleksitas Ruang: O(4n) ~ O(n) untuk array tree.

3. Implementation Details (Detail Implementasi)
-----------------------------------------------
- **Structure / Struktur**:
  - [EN] A binary tree where each node represents an interval. The root represents the whole array.
  - [ID] Pohon biner di mana setiap node mewakili interval. Root mewakili seluruh array.
- **Operations / Operasi**:
  - [EN] **Build**: Recursively build left and right children, then combine values.
  - [ID] **Build**: Membangun anak kiri dan kanan secara rekursif, lalu menggabungkan nilai.
  - [EN] **Update**: Find the leaf node corresponding to the index, update it, and recalculate path to root.
  - [ID] **Update**: Temukan node daun yang sesuai dengan indeks, perbarui, dan hitung ulang jalur ke root.
  - [EN] **Query**: Combine results from nodes that are fully contained within the query range.
  - [ID] **Query**: Gabungkan hasil dari node yang sepenuhnya dimuat dalam rentang kueri.

4. Usage Documentation (Dokumentasi Penggunaan)
-----------------------------------------------
- **Class / Kelas**:
  - [EN] `SegmentTree(arr)`: Initializes the tree with array `arr`.
  - [ID] `SegmentTree(arr)`: Menginisialisasi pohon dengan array `arr`.
- **Methods / Metode**:
  - [EN] `.update(idx, val)`: Updates `arr[idx]` to `val`.
  - [ID] `.update(idx, val)`: Memperbarui `arr[idx]` menjadi `val`.
  - [EN] `.query(l, r)`: Returns the sum (or other metric) of subarray `arr[l...r]`.
  - [ID] `.query(l, r)`: Mengembalikan jumlah (atau metrik lain) dari subarray `arr[l...r]`.
"""

from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        # Ukuran tree maks 4*n
        self.tree = [0] * (4 * self.n)
        self.arr = arr
        self._build(1, 0, self.n - 1)
        
    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self._build(2 * node, start, mid)
            self._build(2 * node + 1, mid + 1, end)
            # Contoh ini untuk Range Sum Query
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
            
    def update(self, idx: int, val: int):
        """Update nilai array di index idx menjadi val."""
        self._update(1, 0, self.n - 1, idx, val)
        
    def _update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self._update(2 * node, start, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
            
    def query(self, l: int, r: int) -> int:
        """Mengambil jumlah dari range [l, r] (inklusif)."""
        return self._query(1, 0, self.n - 1, l, r)
        
    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return 0 # Identitas penjumlahan
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node, start, mid, l, r)
        p2 = self._query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2

if __name__ == "__main__":
    # Test Cases
    print("Running Segment Tree Tests...")
    
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    
    # Sum of arr[1..3] = 3 + 5 + 7 = 15
    assert st.query(1, 3) == 15
    
    # Update arr[1] = 10
    st.update(1, 10)
    # New array: [1, 10, 5, 7, 9, 11]
    
    # Sum of arr[1..3] = 10 + 5 + 7 = 22
    assert st.query(1, 3) == 22
    
    # Sum of arr[0..5] = 1 + 10 + 5 + 7 + 9 + 11 = 43
    assert st.query(0, 5) == 43
    
    print("All Segment Tree tests passed!")
