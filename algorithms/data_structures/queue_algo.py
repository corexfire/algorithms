"""
Description:
    [EN] A queue is a linear data structure that follows the First In First Out (FIFO) principle. Elements are added at the rear and removed from the front. It is widely used in scheduling, buffering, and breadth-first search algorithms.
    [ID] Antrean adalah struktur data linear yang mengikuti prinsip First In First Out (FIFO). Elemen ditambahkan di belakang dan dihapus dari depan. Ini banyak digunakan dalam penjadwalan, penyangga (buffering), dan algoritma pencarian breadth-first.

Implementation Details:
    [EN]
    - The `Queue` class uses Python's `collections.deque` for efficient O(1) appends and pops from both ends.
    - Key operations include `enqueue` (add item), `dequeue` (remove item), `peek` (view front item), and `is_empty`.
    - Type hinting is used for clarity and better development experience.
    [ID]
    - Kelas `Queue` menggunakan `collections.deque` Python untuk penambahan dan penghapusan yang efisien O(1) dari kedua ujung.
    - Operasi kunci meliputi `enqueue` (tambah item), `dequeue` (hapus item), `peek` (lihat item depan), dan `is_empty`.
    - Type hinting digunakan untuk kejelasan dan pengalaman pengembangan yang lebih baik.

Usage Documentation:
    [EN]
    - Instantiate the `Queue` class.
    - Use `enqueue(item)` to add an element to the back of the queue.
    - Use `dequeue()` to remove and return the element at the front of the queue.
    - Use `peek()` to inspect the front element without removing it.
    - Use `is_empty()` to check if the queue has no elements.
    - Use `size()` to get the number of elements in the queue.
    [ID]
    - Buat instansi kelas `Queue`.
    - Gunakan `enqueue(item)` untuk menambahkan elemen ke belakang antrean.
    - Gunakan `dequeue()` untuk menghapus dan mengembalikan elemen di depan antrean.
    - Gunakan `peek()` untuk memeriksa elemen depan tanpa menghapusnya.
    - Gunakan `is_empty()` untuk memeriksa apakah antrean tidak memiliki elemen.
    - Gunakan `size()` untuk mendapatkan jumlah elemen dalam antrean.

Examples:
    >>> q = Queue()
    >>> q.enqueue("A")
    >>> q.enqueue("B")
    >>> q.peek()
    'A'
    >>> q.dequeue()
    'A'
    >>> q.size()
    1
"""

from typing import Any, Optional, Deque as DequeType
from collections import deque

class Queue:
    """Implementasi Queue menggunakan deque."""
    
    def __init__(self):
        self._items: DequeType[Any] = deque()
        
    def enqueue(self, item: Any) -> None:
        """Menambahkan item ke belakang queue."""
        self._items.append(item)
        
    def dequeue(self) -> Optional[Any]:
        """
        Menghapus dan mengembalikan item terdepan queue.
        Returns None jika queue kosong.
        """
        if self.is_empty():
            return None
        return self._items.popleft()
        
    def peek(self) -> Optional[Any]:
        """
        Melihat item terdepan tanpa menghapusnya.
        Returns None jika queue kosong.
        """
        if self.is_empty():
            return None
        return self._items[0]
        
    def is_empty(self) -> bool:
        """Memeriksa apakah queue kosong."""
        return len(self._items) == 0
        
    def size(self) -> int:
        """Mengembalikan jumlah item dalam queue."""
        return len(self._items)
    
    def __str__(self) -> str:
        return f"Queue({list(self._items)})"

if __name__ == "__main__":
    # Test cases Queue
    print("Running Queue Tests...")
    
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    
    print(f"Current Queue: {q}")
    
    assert q.peek() == "A", "Peek failed"
    assert q.dequeue() == "A", "Dequeue 1 failed"
    assert q.dequeue() == "B", "Dequeue 2 failed"
    assert q.size() == 1, "Size failed"
    assert q.peek() == "C", "Peek after dequeue failed"
    
    q.dequeue() # Remove C
    assert q.is_empty() == True, "Is Empty failed"
    assert q.dequeue() is None, "Dequeue empty failed"
    
    print("All Queue tests passed!")
