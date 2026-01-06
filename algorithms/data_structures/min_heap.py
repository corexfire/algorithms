"""
Min Heap / Heap Minimum

English Description:
A Min Heap is a complete binary tree where the value of each node is less than or equal to the values of its children. The root node always contains the minimum element in the heap. It is typically implemented using an array.

Indonesian Description:
Min Heap adalah pohon biner lengkap di mana nilai setiap simpul lebih kecil atau sama dengan nilai anak-anaknya. Simpul akar selalu berisi elemen minimum dalam heap. Ini biasanya diimplementasikan menggunakan array.

Implementation Details:
- Array Representation / Representasi Array:
  [EN] For a node at index `i`, left child is at `2*i + 1`, right child at `2*i + 2`, and parent at `(i-1)//2`.
  [ID] Untuk simpul pada indeks `i`, anak kiri berada di `2*i + 1`, anak kanan di `2*i + 2`, dan induk di `(i-1)//2`.

- Heap Property / Properti Heap:
  [EN] Maintained via `_sift_up` (after insertion) and `_sift_down` (after extraction).
  [ID] Dipertahankan melalui `_sift_up` (setelah penyisipan) dan `_sift_down` (setelah ekstraksi).

- Time Complexity / Kompleksitas Waktu:
  [EN] Insert: O(log n). Extract Min: O(log n). Get Min: O(1).
  [ID] Sisipkan: O(log n). Ekstrak Min: O(log n). Ambil Min: O(1).

- Space Complexity / Kompleksitas Ruang:
  [EN] O(n) to store the elements.
  [ID] O(n) untuk menyimpan elemen.

Usage Documentation:
  [EN] Use `MinHeap()` to create. `insert(key)` to add, `extract_min()` to remove and return the smallest, `get_min()` to peek.
  [ID] Gunakan `MinHeap()` untuk membuat. `insert(key)` untuk menambah, `extract_min()` untuk menghapus dan mengembalikan yang terkecil, `get_min()` untuk mengintip.

  >>> heap = MinHeap()
  >>> heap.insert(3)
  >>> heap.insert(1)
  >>> heap.insert(5)
  >>> heap.get_min()
  1
  >>> heap.extract_min()
  1
  >>> heap.get_min()
  3
"""

from typing import List, Optional

class MinHeap:
    def __init__(self):
        """Initialize an empty Min Heap."""
        self.heap = []

    def parent(self, i: int) -> int:
        """Returns the index of the parent node."""
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        """Returns the index of the left child node."""
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        """Returns the index of the right child node."""
        return 2 * i + 2

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the heap.
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self) -> Optional[int]:
        """
        Removes and returns the minimum element from the heap.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def get_min(self) -> Optional[int]:
        """
        Returns the minimum element without removing it.
        """
        return self.heap[0] if self.heap else None

    def _sift_up(self, i: int) -> None:
        """
        Moves the element at index i up to its correct position.
        """
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _sift_down(self, i: int) -> None:
        """
        Moves the element at index i down to its correct position.
        """
        min_index = i
        l = self.left_child(i)
        r = self.right_child(i)

        # Check if left child exists and is smaller than current
        if l < len(self.heap) and self.heap[l] < self.heap[min_index]:
            min_index = l

        # Check if right child exists and is smaller than current smallest
        if r < len(self.heap) and self.heap[r] < self.heap[min_index]:
            min_index = r

        # If smallest is not current, swap and continue sifting down
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._sift_down(min_index)

    def is_empty(self) -> bool:
        """Returns True if the heap is empty."""
        return len(self.heap) == 0
        
    def size(self) -> int:
        """Returns the number of elements in the heap."""
        return len(self.heap)

if __name__ == "__main__":
    print("Min Heap Tests...")
    
    heap = MinHeap()
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)

    assert heap.extract_min() == 1
    assert heap.extract_min() == 2
    assert heap.extract_min() == 3
    assert heap.extract_min() == 4
    assert heap.extract_min() == 5
    
    print("All Min Heap tests passed!")
