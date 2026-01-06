"""
Fenwick Tree (Binary Indexed Tree) / Pohon Fenwick

English Description:
A Fenwick Tree, or Binary Indexed Tree (BIT), is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. It is space-efficient and easier to implement than a Segment Tree for prefix sum problems.

Indonesian Description:
Fenwick Tree, atau Binary Indexed Tree (BIT), adalah struktur data yang dapat memperbarui elemen dan menghitung jumlah awalan (prefix sum) secara efisien dalam tabel angka. Ini hemat ruang dan lebih mudah diimplementasikan daripada Segment Tree untuk masalah jumlah awalan.

Implementation Details:
- Update Operation / Operasi Pembaruan:
  [EN] Adds a value to an index by traversing up the tree using `index += index & (-index)`.
  [ID] Menambahkan nilai ke indeks dengan menelusuri pohon ke atas menggunakan `index += index & (-index)`.

- Query Operation / Operasi Kueri:
  [EN] Calculates prefix sum by traversing down the tree using `index -= index & (-index)`.
  [ID] Menghitung jumlah awalan dengan menelusuri pohon ke bawah menggunakan `index -= index & (-index)`.

- Time Complexity / Kompleksitas Waktu:
  [EN] O(log n) for both update and query operations.
  [ID] O(log n) untuk operasi pembaruan dan kueri.

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the tree array.
  [ID] O(n) untuk menyimpan array pohon.

Usage Documentation:
  [EN] Initialize `FenwickTree(size)`, then use `update(index, delta)` to modify values and `query(index)` to get prefix sums.
  [ID] Inisialisasi `FenwickTree(size)`, lalu gunakan `update(index, delta)` untuk mengubah nilai dan `query(index)` untuk mendapatkan jumlah awalan.

  >>> ft = FenwickTree(5)
  >>> ft.update(1, 10)
  >>> ft.update(2, 20)
  >>> ft.update(3, 30)
  >>> ft.query(2)
  30
  >>> ft.range_query(2, 3)
  50
"""

from typing import List

class FenwickTree:
    def __init__(self, size: int):
        """
        Initialize Fenwick Tree with a given size.
        Args:
            size: The number of elements in the array.
        """
        # 1-based indexing, so size + 1
        self.tree = [0] * (size + 1)

    def update(self, i: int, delta: int) -> None:
        """
        Adds delta to element at index i (1-based).
        
        Args:
            i: Index to update (1-based)
            delta: Value to add
        """
        while i < len(self.tree):
            self.tree[i] += delta
            # Add least significant bit
            i += i & (-i)

    def query(self, i: int) -> int:
        """
        Returns the prefix sum from 1 to i.
        
        Args:
            i: Index up to which sum is calculated (1-based)
            
        Returns:
            Prefix sum
        """
        s = 0
        while i > 0:
            s += self.tree[i]
            # Subtract least significant bit
            i -= i & (-i)
        return s

    def range_query(self, left: int, right: int) -> int:
        """
        Returns sum from left to right (inclusive).
        
        Args:
            left: Left index (1-based)
            right: Right index (1-based)
            
        Returns:
            Sum of elements in range [left, right]
        """
        if left > right:
            return 0
        return self.query(right) - self.query(left - 1)

if __name__ == "__main__":
    print("Fenwick Tree Tests...")
    
    # Array: [1, 2, 3, 4, 5]
    # Prefix sums: [1, 3, 6, 10, 15]
    
    ft = FenwickTree(5)
    
    # Update values
    ft.update(1, 1)
    ft.update(2, 2)
    ft.update(3, 3)
    ft.update(4, 4)
    ft.update(5, 5)
    
    # Test queries
    print(f"Query(5): {ft.query(5)}, Expected: 15")
    assert ft.query(5) == 15
    
    print(f"Query(3): {ft.query(3)}, Expected: 6")
    assert ft.query(3) == 6
    
    # Test range query
    # Sum from 2 to 4 (2+3+4 = 9)
    print(f"Range Query(2, 4): {ft.range_query(2, 4)}, Expected: 9")
    assert ft.range_query(2, 4) == 9
